"""Validate the compiled one-page CV using Poppler and the LaTeX log."""

import os
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ("Summary", "Skills", "Experience", "Publications", "Education & Certifications")


def run_tool(*args):
    return subprocess.run(
        args,
        cwd=ROOT,
        env={**os.environ, "LC_ALL": "C"},
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout


def check_pdf():
    for name in ("cv.pdf", "cv.log"):
        if not (ROOT / name).is_file() or (ROOT / name).stat().st_size == 0:
            raise ValueError(f"Missing or empty {name}; run make first.")

    info = run_tool("pdfinfo", "-enc", "UTF-8", "cv.pdf")
    metadata = dict(
        line.split(":", 1) for line in info.splitlines() if ":" in line
    )
    if metadata.get("Pages", "").strip() != "1":
        raise ValueError("The CV must fit on exactly one page.")

    log = (ROOT / "cv.log").read_text(encoding="utf-8", errors="replace")
    problems = re.findall(
        r"^.*(?:Overfull \\[hv]box|Missing character:|LaTeX Error:).*$",
        log,
        flags=re.MULTILINE,
    )
    if problems:
        raise ValueError("LaTeX layout or character errors:\n" + "\n".join(problems))

    text = run_tool("pdftotext", "-enc", "UTF-8", "-layout", "cv.pdf", "-")
    if not text.strip() or "\ufffd" in text:
        raise ValueError("The PDF text is empty or contains replacement characters.")
    for section in SECTIONS:
        if not re.search(rf"^\s*{re.escape(section)}\s*$", text, re.MULTILINE):
            raise ValueError(f"Missing section in extracted text: {section}")

    author = metadata.get("Author", "").strip()
    title = metadata.get("Title", "").strip()
    normalized_text = " ".join(text.split())
    if not author or " ".join(author.split()) not in normalized_text:
        raise ValueError("PDF author metadata must match the visible name.")
    prefix = author + " — "
    if not title.startswith(prefix) or not title[len(prefix):].strip():
        raise ValueError("PDF title metadata must contain the name and role.")
    if " ".join(title[len(prefix):].split()) not in normalized_text:
        raise ValueError("PDF title metadata must match the visible role.")


if __name__ == "__main__":
    try:
        check_pdf()
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"PDF check failed: {error}", file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            print(error.stderr.strip(), file=sys.stderr)
        sys.exit(1)
    print("PDF checks passed: one page, no overflow, readable text and matching metadata.")
