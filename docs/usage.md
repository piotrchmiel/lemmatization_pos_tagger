# Korzystanie z programu

## Konfiguracja środowiska
Należy dodać folder zawierający projekt do zmiennej środowiskowej `PYTHONPATH`.
Jeśli akurat się w nim znajdujemy (jest on katalogiem bieżącym), można to zrobić np. poprzez:

    $ export PYTHONPATH="${PYTHONPATH}:${PWD}"


Aby wykonać powyższą komendę wraz z włączeniem `venv`, wystarczy pobrać zawartość pliku `prepare` do shella poprzez:

    $ source prepare

## Konwersja plików xml do csv
Projekt zawiera skrypt umożliwiający konwersję plików xmlowych do formatu csv:

    $ python3 src/scripts/csv_creator.py -h
    usage: csv_creator.py [-h] (--use_pwr | --use_national) [--extract_base_words]
    optional arguments:
    -h, --help            show this help message and exit
    --use_pwr             Use pwr corpus
    --use_national        Use national corpus
    --extract_base_words  Save words with their base form


## Tagger - uczenie klasyfikatorów

    $ python3 src/tagger_trainer.py -h  # więcej o ustawianiu liczby rdzeni
    $ python3 src/tagger_trainer.py

Domyślnie podczas uczenia używane są wszystkie rdzenie procesora - jeden rdzeń na algorytm. Logi związane z uczeniem zapisywane są do pliku `tagger_factory.log`.


## Testowanie taggera

    $ python3 src/tagger_tester.py  # pojedyncze słowo
    $ python3 src/text_tagger.py    # tekst

Skrypt zapyta się o słowo/tekst do klasyfikacji.


## Uruchomienie benchmarka

    $ python3 src/benchmark.py
