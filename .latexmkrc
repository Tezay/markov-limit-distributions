$out_dir = 'out';
$aux_dir = 'out';
$pdf_mode = 1;

$pdflatex = 'pdflatex %O -interaction=nonstopmode -file-line-error -synctex=1 -output-directory=out %S';
$biber    = 'biber %O --input-directory=out --output-directory=out %B';

$clean_ext .= ' synctex.gz';
