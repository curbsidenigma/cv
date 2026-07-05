.PHONY: all clean watch

all:
	latexmk -pdf cv.tex

watch:
	latexmk -pdf -pvc cv.tex

clean:
	latexmk -C
