# **W CELU POPRAWNEGO ŚCIĄGNIĘCIA REPOZYTORIUM WYMAGANY JEST [GIT-LFS](https://git-lfs.github.com/)**

# lemmatization_pos_tagger
ZIWG Projekt

## Rozpoczęcie pracy:

Wymagany Python 3.5. Instalacja pakietów:
    
	pip3 install -r requirements.txt

## Instalacja korpusów:

Korpusy z powodu takiego, że są ogromnych rozmiarów wyleciały z repo i można je zaciągnąć uruchamiając skrypt instalacyjny, który rozpakowywuje korpus PWr z pliku kpwr-1.2.6-disamb.7z a korpus polski pobiera ze źródła. Uruchomienie:

	./installCorpuses.sh
	
## Instalacja NLTK:

Do tokenizacji slów w podanym tekscie użyto NLTK. W celu instalacji w interpreterze należy użyć następujących komand:
	
	>>> import nltk
	>>> nltk.download()

### Wstępne wyniki 10000 ze zbioru

Support Vector Machine PWr Tagger      : 55.35<br />
Decision Tree PWr Tagger               : 53.449999999999996<br />
Stochastic Gradient Descent PWr Tagger : 47.78<br />
Logistic Regression PWr Tagger         : 53.43<br />
Naive Bayes PWr Tagger                 : 46.78<br />
K Neighbors PWr Tagger                 : 50.129999999999995<br />
Neural Networks PWr Tagger             : 52.21<br />
