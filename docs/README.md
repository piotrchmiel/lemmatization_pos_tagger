# Dokumentacja projektowa

Dokumentacja projektowa znajduje się w pliku `report.pdf`.
Aby wygenerować plik z dokumentacją należy wywołać komendę:
```
make
```
Pliki pośrednie można usunąć komendą `make clean`.

## Kompilacja dokumentu
```
frontpage.tex ------------------\
project-about.tex ---------------\
                                  \
installation.md --\                \
usage.md ----------> app-docs.tex --> report.pdf
                                  /
data-and-classifiers.tex --------/
efficiency.tex -----------------/
```
