report.pdf: report.tex app-docs.tex
	pdflatex -synctex=1 -interaction=nonstopmode report.tex
	pdflatex -synctex=1 -interaction=nonstopmode report.tex

app-docs.tex: installation.md usage.md
	pandoc -o app-docs.tex installation.md usage.md

clean:
	rm *.log *.out *.toc *.gz *.aux app-docs.tex
