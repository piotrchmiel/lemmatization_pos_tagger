# Korzystanie z programu

## Konfiguracja środowiska
Należy dodać folder `src` z kodem programu do zmiennej środowiskowej `PYTHONPATH`:

    $ export PYTHONPATH="${PYTHONPATH}:${PWD}/src"

Aby wykonać powyższą komendę wraz z włączeniem `venv`, wystarczy pobrać zawartość pliku `prepare` do shella poprzez:

    $ source prepare


## Tagger - uczenie klasyfikatorów

    $ python src/tagger_trainer.py -h  # więcej o ustawianiu ilości rdzeni
    $ python src/tagger_trainer.py

Domyślnie podczas uczenia używane są wszystkie rdzenie procesora - jeden rdzeń na algorytm. Logi związane z uczeniem zapisywane są do pliku `tagger_factory.log`.
