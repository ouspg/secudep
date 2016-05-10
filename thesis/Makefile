pdf: dt.tex di.bib
	@sort abbreviations.tex > abbreviations_sorted.tex
	pdflatex dt.tex
	bibtex dt
	pdflatex dt.tex
	pdflatex dt.tex

	@if [ $$? -eq 0 ]; \
	then \
	  mv dt.pdf thesis.pdf; \
	  echo "====================================="; \
	  echo "PDF generation compiled: thesis.pdf"; \
	  echo "====================================="; \
	fi

clean:
	rm abbreviations_sorted.tex thesis.pdf dt.toc dt.log dt.blg dt.bbl dt.aux
