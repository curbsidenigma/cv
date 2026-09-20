.PHONY: all check clean watch

all:
	latexmk -xelatex cv.tex

check: all
	python3 scripts/check_pdf.py

watch:
	latexmk -xelatex -pvc cv.tex

clean:
	latexmk -C
