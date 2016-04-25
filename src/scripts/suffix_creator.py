from collections import Counter
from os import path, walk, mkdir
from pickle import dump

from bs4 import BeautifulSoup
from urllib.parse import urlparse

from src.settings import PWR_CORPUS_DIR, SUFFIX_FILE, SUFFIX_DIR


def get_words(filename):
    with open(filename, encoding="utf8") as file_handler:
        tokens = BeautifulSoup(file_handler.read(), 'xml').find_all('tok')
        for token in tokens:
            word = token.orth.string
            if word is not None and len(word) != 1:
                yield word
                base = token.base.string
                if base is not None and len(base) != 1 and base != word:
                    yield base


def find_xml_files(folder_name):
    for root, _, files in walk(folder_name):
        for filename in files:
            if filename.endswith(".xml") and not filename.endswith(".rel.xml"):
                yield path.join(root, filename)


def main():
    suffixes = []

    if path.exists(PWR_CORPUS_DIR):
        for filename in find_xml_files(PWR_CORPUS_DIR):
            for word in get_words(filename):
                if bool(urlparse(word).scheme):  # we do not want URLs contaminating suffixes
                    continue
                for suffix_length in range(1, len(word)):
                    if len(suffixes) < suffix_length:
                        suffixes.append(Counter())
                    suffixes[suffix_length - 1][word[-suffix_length:]] += 1

        if not path.exists(SUFFIX_DIR):
            mkdir(SUFFIX_DIR)

        with open(SUFFIX_FILE, 'wb') as file_handler:
            dump(suffixes, file_handler)
    else:
        print("You are trying to cheat on me again. Where's the Corpus directory?")


if __name__ == '__main__':
    main()
