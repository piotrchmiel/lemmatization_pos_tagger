# Korzystanie z programu

## Konfiguracja środowiska
Należy dodać folder `src` z kodem programu do zmiennej środowiskowej `PYTHONPATH`:

    $ export PYTHONPATH="${PYTHONPATH}:${PWD}/src"

Aby wykonać powyższą komendę wraz z włączeniem `venv`, wystarczy pobrać zawartość pliku `prepare` do shella poprzez:

    $ source prepare


## Tagger - uczenie klasyfikatorów

    $ python3 src/tagger_trainer.py -h  # więcej o ustawianiu ilości rdzeni
    $ python3 src/tagger_trainer.py

Domyślnie podczas uczenia używane są wszystkie rdzenie procesora - jeden rdzeń na algorytm. Logi związane z uczeniem zapisywane są do pliku `tagger_factory.log`.


## Testowanie taggera

    $ python3 src/tagger_tester.py  # pojedyncze słowo
    $ python3 src/text_tagger.py    # tekst

Skrypt zapyta się o słowo/tekst do klasyfikacji.


## Uruchomienie benchmarka

    $ python3 src/benchmark.py
