.PHONY: all check clean watch

all:
	latexmk -pdf cv.tex

check: all
	python3 scripts/check_pdf.py

watch:
	latexmk -pdf -pvc cv.tex

clean:
	latexmk -C
