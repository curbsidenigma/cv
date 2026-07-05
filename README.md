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
```

## Build

Requires a TeX distribution (TeX Live / MiKTeX) with `latexmk`.
Only standard packages are used (`titlesec`, `enumitem`, `hyperref`,
`geometry`, `xcolor`) — a medium TeX Live install is enough, no extra
font packages required.

```bash
make          # build cv.pdf
make watch    # rebuild on save
make clean    # remove build artifacts
```

Or directly: `latexmk -pdf cv.tex`.

## Published PDF

On every push to `main`, CI builds `cv.pdf` and deploys it to GitHub Pages,
giving a permanent, always-current link:

```
https://curbsidenigma.github.io/cv/cv.pdf
```

Enable it once under **Settings → Pages → Build and deployment → Source:
GitHub Actions**. Pull requests still build the PDF (as a downloadable
workflow artifact) but do not deploy.

## Editing

Personal details (name, email, links) live at the top of `cv.tex`.
Content lives in `src/sections/`. Add a new section by creating a file
there and `\input`-ing it from `cv.tex`.

## License

See [LICENSE](LICENSE).
