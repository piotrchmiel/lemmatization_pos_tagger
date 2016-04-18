# Zastotoswanie Informatyki W Gospodarce

Projekt dotyczy stworzenia modułu znakującego części mowy oraz lematyzatora języka polskiego przy wykorzystaniu metody "deeplearning".

## Rozpoczęcie pracy:

Wymagany Python 3.5. Opcjonalnie `venv` do pracy w wirtualnym środowisku - wbudowany w Pythona 3 (http://docs.python.org/3/library/venv.html).

    python3 -m venv env
    source env/bin/activate
    which pip3 # dla pewności możesz sprawdzić jaką teraz ścieżkę wskazuje pip3

Instalacja pakietów:

    pip3 install -r requirements.txt

Aby dezaktywować wirtualne środowisko wykonaj: `deactivate` lub po prostu wyjdź z shella: `exit`.

**Uwaga:**
W przypadku instalacji przez `pip` pod Linuksem, potrzebny jest kompilator `gcc-fortran`. Proces instalacji można przyśpieszyć poprzez ręczną instalację paczek ze skompilowanych źródeł.

### Instalacja korpusów:

Korpusy z powodu takiego, że są ogromnych rozmiarów wyleciały z repo i można je zaciągnąć uruchamiając skrypt instalacyjny, który rozpakowywuje korpus PWr z pliku kpwr-1.2.6-disamb.7z a korpus polski pobiera ze źródła. Uruchomienie:

	installCorpuses.sh

### Instalacja NLTK:

Do tokenizacji słów w podanym tekście użyto NLTK. W celu instalacji w interpreterze należy użyć następujących komend:

	>>> import nltk
	>>> nltk.download()

## Wirtualna maszyna udostępniona przez prowadzącego

    IP : 156.17.135.57
    Login : tomekw
    Hasło : 1qaz@WSX

## Internal backlog
Zadania znajdują się na Trello: [nasza tablica](https://trello.com/b/XU09b2u5/zastosowanie-informatyki-w-gospodarce-projekt-deeplearning-lematyzacja-pos-tagging)

## Technologie
   - Python 3.5 ([Dokumentacja](http://docs.python.org/3.5/))
   - Scikit Learn 0.17.1 ([Dokumentacja](http://http://scikit-learn.org/0.17/documentation.html))
   - Scikit Neural Network 0.6.1 ([Dokumentacja](https://scikit-neuralnetwork.readthedocs.org/en/latest/))
   - Joblib 0.9.4 ([Dokumentacja](https:/pythonhosted.org/joblib/))
   - NLTK 3.2 ([Dokumentacja](http://www.nltk.org))
   - Beautiful Soup 4.4.1 ([Dokumentacja](https://www.crummy.com/software/BeautifulSoup/bs4/doc/))
   - Pylint 1.5.4 ([Dokumentacja](http://www.pylint.org))
   - Numpy 1.11.0 ([Dokumentacja](http://www.numpy.org))
   - Scipy 0.17.0 ([Dokumentacja](http://www.scipy.org))

## Wyniki dokładności modeli w bazie

| **Nazwa Algorytmu**          | **Dokładność [%] - korpus uczący PWr** | **Dokładność [%] - korpus uczący national** |
|:----------------------------:|:--------------------------------------:|:-------------------------------------------:|
| Support Vector Machine       | 56.468 | 54.949 |
| Decision Trees               | 57.246 | 55.671 |
| Stochastic Gradient Descent  | 53.627 | 53.121 |
| Logistic Regression          | 55.571 | 55.307 |
| Naive Bayes                  | 54.141 | 52.813 |
| K Neighbors                  | 50.168 | 50.255 |
| Neural Networks              | 55.801 | 54.692 |
