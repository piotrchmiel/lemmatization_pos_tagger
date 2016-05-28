# Przygotowanie środowiska

Wymagany [Python 3.5](https://www.python.org/downloads/).


## Wirtualne środowisko (opcjonalnie)

    $ python3 -m venv env               # instalacja venv
    $ source env/bin/activate           # aktywacja venv

      ... praca w wirtualnym środowisku ...

    $ deactivate                        # deaktywacja venv


## Instalacja pakietów
Podczas instalacji pakietów pod Linuksem, potrzebny jest kompilator `gcc-fortran`.

    $ pip3 install -r requirements.txt


## Instalacja korpusów
Należy uruchomić skrypt instalacyjny, który rozpakowywuje korpus PWr z pliku kpwr-1.2.6-disamb.7z, a korpus polski pobiera ze źródła.

	$ ./installCorpuses.sh


## Instalacja NLTK
Do tokenizacji słów w podanym tekście użyto NLTK. Dwie opcje instalacji:

1. Interaktywna instalacja w interpreterze:
```
>>> import nltk
>>> nltk.download()
```
2. Instalacja poprzez linię komend:
```
$ sudo python -m nltk.downloader -d /usr/local/share/nltk_data all
```
Dane NLTK zostaną zainstalowane w katalogu `/usr/local/share/nltk_data`.


## Instalacja CUDA
1. Pobranie paczki instalującej repozytorium Nvidii ze strony: https://developer.nvidia.com/cuda-downloads, testowana wersja: Linux Ubuntu 14.04, architektura x86_64, paczka deb (local).
2. Instalacja repozytorium w systemie:
```
$ dpkg -i cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb
```
3. Instalacja sterowników i środowiska CUDA:
```
$ apt-get update && apt-get install -y cuda
```
4. Restart maszyny w celu załadowania sterowników Nvidii zamiast Nouveau.
5. Instalacja Nvidia cuDNN (biblioteki wspomagające sieci neuronowe): należy umieścić zawartość archiwum `cudnn-7.0-linux-x64-v4.0-prod.tgz` w folderze `/usr/local/cuda`. Do ściągnięcia ze strony https://developer.nvidia.com/rdp/form/cudnn-download-survey.
6. Instalacja modułu `tensorflow` dla Pythona ze strony: https://www.tensorflow.org.
