# CV

[![Build CV](https://github.com/curbsidenigma/cv/actions/workflows/build.yml/badge.svg)](https://github.com/curbsidenigma/cv/actions/workflows/build.yml)
[![Live PDF](https://img.shields.io/badge/CV-live%20PDF-blue)](https://curbsidenigma.github.io/cv/cv.pdf)
[![Made with LaTeX](https://img.shields.io/badge/Made%20with-LaTeX-008080?logo=latex&logoColor=white)](https://www.latex-project.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

My curriculum vitae, written in LaTeX.

## Structure

```
cv.tex                 # main document — preamble, personal data, section includes
src/
  header.tex           # name, title, contact line
  sections/            # one file per CV section (edit these)
    summary.tex
    experience.tex
    education.tex
    skills.tex
    projects.tex
scripts/check_pdf.py   # PDF quality checks shared by local builds and CI
```

## Build

Requires a TeX distribution (TeX Live / MiKTeX) with `latexmk` and pdfLaTeX.
Packages used: `cmap`, `fontenc`, `inputenc`, `lmodern` (Latin Modern fonts),
`geometry`, `enumitem`, `titlesec`, `hyperref`, `xcolor`, and `glyphtounicode`.
PDF checks also require Python 3 and Poppler (`pdfinfo`, `pdftotext`).

On Debian/Ubuntu:

```bash
sudo apt-get update
sudo apt-get install make latexmk texlive-latex-base texlive-latex-recommended texlive-latex-extra lmodern python3 poppler-utils
```

```bash
make          # build cv.pdf
make check    # build and validate the one-page PDF
make watch    # rebuild on save
make clean    # remove build artifacts
```

Or directly: `latexmk -pdf cv.tex`.

`make check` rejects extra pages, overfull boxes, missing glyphs, missing
sections, and author/title metadata that do not match the extracted text.
It checks the five section headings listed in `scripts/check_pdf.py`; update
that list when renaming or adding sections. Review the PDF visually as well:
these checks do not guarantee its appearance or compatibility with every ATS.

## Published PDF

On every push to `main`, CI builds and validates `cv.pdf`, then deploys it to
GitHub Pages. This link serves the latest successfully deployed PDF:

```
https://curbsidenigma.github.io/cv/cv.pdf
```

Enable it once under **Settings → Pages → Build and deployment → Source:
GitHub Actions**. Pull requests still build the PDF (as a downloadable
workflow artifact) but do not deploy.

New runs cancel older runs for the same branch or pull request. The workflow
can also be started manually from the Actions tab; only `main` deploys.

Actions are pinned to commit SHAs and Dependabot proposes monthly updates.
The TeX Live image is pinned by digest in `.github/workflows/build.yml`.
To update it, inspect `docker buildx imagetools inspect
ghcr.io/xu-cheng/texlive-full:latest`, replace the digest, and review the PDF
artifact from a passing pull-request build before merging. Local TeX versions
may differ from CI, so byte-identical local and CI PDFs are not guaranteed.

## Editing

Personal details (name, email, links) live at the top of `cv.tex`.
Content lives in `src/sections/`. Add a new section by creating a file
there and `\input`-ing it from `cv.tex`.

## License

See [LICENSE](LICENSE).
