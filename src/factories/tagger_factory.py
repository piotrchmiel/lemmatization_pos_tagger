from os import path

from src.settings import CLASSIFIERS_DIR, SUFFIX_FILE, N_ONE_LETTER, N_TWO_LETTERS, \
                        N_THREE_LETTERS, N_FOUR_LETTERS
from src.utils.csv_reader import CsvReader
from src.utils.extractor import PosFeatureExtractor
from src.utils.suffix import SuffixUnpacker
from src.utils.tools import train_target, save_classifier, load_classifier


class TaggerFactory(object):

    def __init__(self):
        suffix_unpacker = SuffixUnpacker(SUFFIX_FILE)

        one_letter_suffixes = suffix_unpacker.extract_n_best_one_letter(N_ONE_LETTER)
        two_letters_suffixes = suffix_unpacker.extract_n_best_two_letters(N_TWO_LETTERS)
        three_letters_suffixes = suffix_unpacker.extract_n_best_three_letters(N_THREE_LETTERS)
        four_letters_suffixes = suffix_unpacker.extract_n_best_four_letters(N_FOUR_LETTERS)

        self.feature_extractor = PosFeatureExtractor(one_letter_suffixes, two_letters_suffixes,
                                                     three_letters_suffixes, four_letters_suffixes)

    def dump_national_tagger(self, classifier_object, filename):
        filename += "_nc.pickle"
        file_location = path.join(CLASSIFIERS_DIR, filename)
        csv_reader = CsvReader(use_national_corpus=True)
        save_classifier(file_location, train_target(classifier_object, self.feature_extractor, csv_reader))

    def dump_pwr_tagger(self, classifier_object, filename):
        filename += "_pwr.pickle"
        file_location = path.join(CLASSIFIERS_DIR, filename)
        csv_reader = CsvReader(use_national_corpus=False)
        save_classifier(file_location, train_target(classifier_object, self.feature_extractor, csv_reader))

    def load_national_tagger(self, filename):
        filename += "_nc.pickle"
        return load_classifier(path.join(CLASSIFIERS_DIR, filename))

    def load_pwr_tagger(self, filename):
        filename += "_pwr.pickle"
        return load_classifier(path.join(CLASSIFIERS_DIR, filename))

    def get_feature_extractor(self):
        return self.feature_extractor
