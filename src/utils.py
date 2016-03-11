from pickle import load, dump
from os import walk, path
from bs4 import BeautifulSoup


def save_classifier(file_location, classifier):
    with open(file_location, 'wb') as file_handler:
            dump(classifier, file_handler)


def load_classifier(file_location):
    with open(file_location, 'rb') as file_handler:
        classifier = load(file_handler)
    return classifier


class PosFeatureExtractor(object):
    def __init__(self, one_letter_suffixes, two_letters_suffixes, three_letters_suffixes, four_letters_suffixes):
        self.common_suffixes = [word for word, _ in one_letter_suffixes]
        self.common_suffixes.extend([word for word, _ in two_letters_suffixes])
        self.common_suffixes.extend([word for word, _ in three_letters_suffixes])
        self.common_suffixes.extend([word for word, _ in four_letters_suffixes])
        self.common_suffixes = set(self.common_suffixes)

    def pos_features(self, word):
        features = {}
        for suffix in self.common_suffixes:
            if word.lower().endswith(suffix):
                features['endswith({})'.format(suffix)] = True
        return features


class SuffixUnpacker(object):
    def __init__(self, name_of_pickle_file):
        with open(name_of_pickle_file, "rb") as file_handler:
            self.suffixes = load(file_handler)

    def extract_n_best_one_letter(self,n):
        return self.suffixes[0].most_common(n)

    def extract_n_best_two_letters(self,n):
        return self.suffixes[1].most_common(n)

    def extract_n_best_three_letters(self,n):
        return self.suffixes[2].most_common(n)

    def extract_n_best_four_letter(self,n):
        return self.suffixes[3].most_common(n)


class XmlReader(object):
    def __init__(self, folder_name):
        self.folder = folder_name

    def extract_words_and_tags(self):
        for filename in self.find_xml_files():
            for word, ctag in self.get_words(filename):
                yield word, ctag

    def get_words(self, filename):
        with open(filename) as file_handler:
            tokens = BeautifulSoup(file_handler.read(), 'xml').find_all('tok')
            for token in tokens:
                word = token.orth.string
                try:
                    base = token.lex.base.string
                    ctag = token.lex.ctag.string
                except:
                    continue

                if ctag is not None:
                    if word is not None and len(word) != 1:
                        yield word, ctag

                        if base is not None and len(base) != 1 and base != word:
                            yield base, ctag

    def find_xml_files(self):
        for root, dirs, files in walk(self.folder):
            for filename in files:
                if filename.endswith(".xml") and not filename.endswith(".rel.xml"):
                    yield path.join(root, filename)