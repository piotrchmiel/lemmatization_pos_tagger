from pickle import load, dump
from os import walk, path
from bs4 import BeautifulSoup
from csv import DictWriter, DictReader, QUOTE_MINIMAL

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

    @staticmethod
    def tag_mapper(word):
        PARTS_OF_SPEECH = {
            'subst': 'rzeczownik',
            'depr': 'rzeczownik deprecjatywny',
            'num': 'liczebnik główny',
            'numcol': 'liczebnik zbiorowy',
            'adj': 'przymiotnik',
            'adja': 'przymiotnik przyprzym.',
            'adjp': 'przymiotnik poprzyimkowy',
            'adjc': 'przymiotnik predykatywny',
            'adv': 'przysłówek',
            'ppron12': 'zaimek nietrzecioosobowy',
            'ppron3': 'zaimek trzecioosobowy',
            'siebie': 'zaimek siebie ',
            'fin': 'forma nieprzeszła',
            'bedzie': 'forma przyszła być ',
            'aglt': 'aglutynant być ',
            'praet': 'pseudoimiesłów',
            'impt': 'rozkaźnik',
            'imps': 'bezosobnik',
            'inf': 'bezokolicznik',
            'pcon': 'im. przys. współczesny',
            'pant': 'im. przys. uprzedni',
            'ger': 'odsłownik',
            'pact': 'im. przym. czynny',
            'ppas': 'im. przym. bierny',
            'winien': 'winien',
            'pred': 'predykatyw',
            'prep': 'przyimek',
            'conj': 'spójnik współrzędny',
            'comp': 'spójnik podrzędny',
            'qub': 'kublik',
            'brev': 'skrót',
            'burk': 'burkinostka',
            'interj': 'wykrzyknik',
            'interp': 'interpunkcja',
            'xxx': 'ciało obce',
            'ign': 'forma nierozpoznana'
        }
        return PARTS_OF_SPEECH[word.split(':')[0]]


class SuffixUnpacker(object):
    def __init__(self, name_of_pickle_file):
        with open(name_of_pickle_file, "rb") as file_handler:
            self.suffixes = load(file_handler)

    def extract_n_best_one_letter(self, n):
        return self.suffixes[0].most_common(n)

    def extract_n_best_two_letters(self, n):
        return self.suffixes[1].most_common(n)

    def extract_n_best_three_letters(self, n):
        return self.suffixes[2].most_common(n)

    def extract_n_best_four_letters(self, n):
        return self.suffixes[3].most_common(n)


class XmlReader(object):
    def __init__(self, folder_name, national_corpus=False):
        self.folder = folder_name
        self.national_corpus = national_corpus

    def extract_words_and_tags(self):
        for filename in self.find_xml_files():
            for word, ctag in self.get_words(filename):
                yield word, ctag

    def get_words(self, filename):
        with open(filename) as file_handler:
            tokens_str = 'tok' if not self.national_corpus else 'seg'
            tokens = BeautifulSoup(file_handler.read(), 'xml').find_all(tokens_str)
            for token in tokens:
                if self.national_corpus:
                    word = token.find('f', attrs={'name': 'orth'}).find('string').string
                    try:
                        base = token.find('f', attrs={'name': 'base'}).find('string').string
                        ctag = PosFeatureExtractor.tag_mapper(':'.join(token.find('f', attrs={'name': 'disamb'}).
                                                                       find('f', attrs={'name': 'interpretation'}).
                                                                       find('string').string.split(':')[1:]))
                    except:
                        continue
                else:
                    word = token.orth.string
                    try:
                        base = token.lex.base.string
                        ctag = PosFeatureExtractor.tag_mapper(token.lex.ctag.string)
                    except:
                        continue

                if ctag is not None:
                    if word is not None and len(word) != 1:
                        yield word, ctag

                        if base is not None and len(base) != 1 and base != word:
                            yield base, ctag

    def find_xml_files(self):
        for root, _, files in walk(self.folder):
            for filename in files:
                query = False
                if self.national_corpus:
                    query = filename == "ann_morphosyntax.xml"
                else:
                    query = filename.endswith(".xml") and not filename.endswith(".rel.xml")
                if query:
                    yield path.join(root, filename)


class CsvReader(object):
    def __init__(self, folder_name):
        self.folder = folder_name

    def convert_xml_to_csv(self):
        if path.exists(self.folder):
            print("Starting conversion of files from .xml to .csv format. Please have a coffee break while I do my job.")

            with open(path.join(self.folder, "extracted.csv"), "w", newline="") as csv_file:
                fieldnames = ['word', 'tag']
                writer = DictWriter(csv_file, fieldnames=fieldnames)
                reader = XmlReader(self.folder)
                writer.writeheader()
                for word, tag in reader.extract_words_and_tags():
                    writer.writerow({'word': word, 'tag': tag})

            print("All done. I appreciate your patience.")
        else:
            print("I am just a very simple algorithm and I have not found a Corpus directory. Provide the proper one.")

    def extract_feature(self, feature_name):
        with open(path.join(self.folder, "extracted.csv"), "r", newline="") as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                yield row[feature_name]