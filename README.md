# lemmatization_pos_tagger
ZIWG Projekt

## Rozpoczęcie pracy:

Wymagany Python 3.5. Opcjonalnie `virtualenv` do pracy w wirtualnym środowisku.

    virtualenv env
    source env/bin/activate
    which pip3 # dla pewności możesz sprawdzić jaką teraz ścieżkę wskazuje pip3

Instalacja pakietów:

    pip3 install -r requirements.txt

Aby dezaktywować wirtualne środowisko wykonaj: `deactivate` lub po prostu wyjdź z shella: `exit`.

**Uwaga:**  
W przypadku instalacji przez `pip` pod Linuksem, potrzebny jest kompilator `gcc-fortran`. Proces instalacji można przyśpieszyć poprzez ręczną instalację paczek ze skompilowanych źródeł.

## Instalacja korpusów:

Korpusy z powodu takiego, że są ogromnych rozmiarów wyleciały z repo i można je zaciągnąć uruchamiając skrypt instalacyjny, który rozpakowywuje korpus PWr z pliku kpwr-1.2.6-disamb.7z a korpus polski pobiera ze źródła. Uruchomienie:

	installCorpuses.sh

## Instalacja NLTK:

Do tokenizacji słów w podanym tekście użyto NLTK. W celu instalacji w interpreterze należy użyć następujących komend:

	>>> import nltk
	>>> nltk.download()

### Wstępne wyniki 10000 ze zbioru

| Tagger                                 | Wynik |
| -------------------------------------- |:-----:|
| Support Vector Machine PWr Tagger      | 55.35 |
| Decision Tree PWr Tagger               | 53.45 |
| Stochastic Gradient Descent PWr Tagger | 47.78 |
| Logistic Regression PWr Tagger         | 53.43 |
| Naive Bayes PWr Tagger                 | 46.78 |
| K Neighbors PWr Tagger                 | 50.13 |
| Neural Networks PWr Tagger             | 52.21 |
