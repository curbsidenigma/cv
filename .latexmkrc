$pdf_mode = 1;          # build PDF via pdflatex
$pdflatex = 'pdflatex -file-line-error -halt-on-error -interaction=nonstopmode -synctex=1 %O %S';
$clean_ext = 'synctex.gz run.xml bbl bcf';
