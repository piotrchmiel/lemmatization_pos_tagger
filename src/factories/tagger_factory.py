from os import path

from src.settings import CLASSIFIERS_DIR, SUFFIX_FILE, N_ONE_LETTER, N_TWO_LETTERS, \
                        N_THREE_LETTERS, N_FOUR_LETTERS
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

    def create_tagger(self, classifier_object, national_corpus, filename):

        if national_corpus:
            filename += "_nc._pickle"
        else:
            filename += "_pwr.pickle"

        save_classifier(path.join(CLASSIFIERS_DIR, filename),
                        train_target(classifier_object, self.feature_extractor, national_corpus))

    def create_tagger_from_file(self, filename, is_trained_by_national):
        if is_trained_by_national:
            filename += "_nc.pickle"
        else:
            filename += "_pwr.pickle"

        return load_classifier(path.join(CLASSIFIERS_DIR, filename))

    def get_feature_extractor(self):
        return self.feature_extractor
