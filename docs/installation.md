# Przygotowanie środowiska

Wymagany [Python 3.5](http://docs.python.org/3.5/) oraz [PIP](https://pip.pypa.io/en/stable/).


## Wirtualne środowisko (opcjonalnie)

    $ python3 -m venv env               # instalacja venv
    $ source env/bin/activate           # aktywacja venv

      ... praca w wirtualnym środowisku ...

    $ deactivate                        # deaktywacja venv


## Instalacja pakietów
Podczas instalacji pakietów pod Linuksem, potrzebny jest kompilator `gcc-fortran`.

    $ pip3 install -r requirements.txt


## Instalacja korpusów
Należy uruchomić skrypt instalacyjny, który rozpakowywuje korpus PWr z pliku kpwr-1.2.6-disamb.7z a korpus polski pobiera ze źródła.

	$ ./installCorpuses.sh


## Instalacja NLTK
Do tokenizacji słów w podanym tekście użyto NLTK. W celu instalacji w interpreterze należy użyć następujących komend:

	>>> import nltk
	>>> nltk.download()
