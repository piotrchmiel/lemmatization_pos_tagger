from collections import Counter
from os import path, walk, mkdir
from pickle import dump
from bs4 import BeautifulSoup
from src.settings import CORPUS_DIR, SUFFIX_FILE, SUFFIX_DIR

def get_words(filename):
    with open(filename) as file_handler:
        tokens = BeautifulSoup(file_handler.read(), 'xml').find_all('tok')
        for token in tokens:
            word = token.orth.string
            if word is not None and len(word) != 1:
                yield word
                base = token.base.string
                if base is not None and len(base) != 1 and base != word:
                    yield base


def find_xml_files(folder_name):
    for root, dirs, files in walk(folder_name):
        for filename in files:
            if filename.endswith(".xml") and not filename.endswith(".rel.xml"):
                yield path.join(root, filename)


def main():
    one_letter_suffixes = Counter()
    two_letter_suffixes = Counter()
    three_letter_suffixes = Counter()
    four_letter_suffixes = Counter()

    if path.exists(CORPUS_DIR):
        for filename in find_xml_files(CORPUS_DIR):
            for word in get_words(filename):
                one_letter_suffixes[word[-1:]] += 1
                if len(word) > 2:
                    two_letter_suffixes[word[-2:]] += 1
                if len(word) > 3:
                    three_letter_suffixes[word[-3:]] += 1
                if len(word) > 4:
                    four_letter_suffixes[word[-4:]] += 1

        if not path.exists(SUFFIX_DIR):
            mkdir(SUFFIX_DIR)

        with open(SUFFIX_FILE, 'wb') as file_handler:
            dump([one_letter_suffixes, two_letter_suffixes, three_letter_suffixes, four_letter_suffixes], file_handler)
    else:
        print("There is no Corpus Path!")

if __name__ == '__main__':
    main()