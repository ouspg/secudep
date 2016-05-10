#!/bin/sh

# Convert to unix-style line endings. Git allows checking files out with
# CRLF line terminators if that is needed.

dos2unix boxedminipage.sty
dos2unix di.bib
dos2unix di.bst
dos2unix di.sty
dos2unix dithesis.cls
dos2unix dt.tex
dos2unix introduction.tex
dos2unix lastpage.dtx
dos2unix lastpage.ins
dos2unix lastpage.sty
dos2unix multibbl.sty

# Use UTF-8. No one should be using ISO-8859-1 anymore
# for new documents.
recode ISO-8859-1..UTF8 di.bib
recode ISO-8859-1..UTF8 di.sty
recode ISO-8859-1..UTF8 dt.tex

sed -i.bak s/latin1/utf8/ dt.tex
rm dt.tex.bak
