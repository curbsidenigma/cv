$pdf_mode = 5;          # build PDF via XeLaTeX for the bundled Nunito Sans fonts
$xelatex = 'xelatex -file-line-error -halt-on-error -interaction=nonstopmode -synctex=1 %O %S';
$clean_ext = 'synctex.gz run.xml bbl bcf';
