from collections import OrderedDict
from os import path
import logging

from src.settings import CLASSIFIERS_DIR, SUFFIX_FILE, N_ONE_LETTER, N_TWO_LETTERS, \
    N_THREE_LETTERS, N_FOUR_LETTERS, TAGGER_FILENAMES
from src.utils.csv_reader import CsvReader
from src.utils.extractor import PosFeatureExtractor
from src.utils.suffix import SuffixUnpacker
from src.utils.tools import train_target, save_classifier, load_classifier


class TaggerFactory(object):
    def __init__(self):
        logging.basicConfig(filename='tagger_factory.log', level=logging.INFO)
        suffix_unpacker = SuffixUnpacker(SUFFIX_FILE)

        one_letter_suffixes = suffix_unpacker.extract_n_best_one_letter(N_ONE_LETTER)
        two_letters_suffixes = suffix_unpacker.extract_n_best_two_letters(N_TWO_LETTERS)
        three_letters_suffixes = suffix_unpacker.extract_n_best_three_letters(N_THREE_LETTERS)
        four_letters_suffixes = suffix_unpacker.extract_n_best_four_letters(N_FOUR_LETTERS)

        self.feature_extractor = PosFeatureExtractor(one_letter_suffixes, two_letters_suffixes,
                                                     three_letters_suffixes, four_letters_suffixes)

    def dump_tagger(self, classifier_object, filename, use_national_corpus):
        filename = filename + "_nc.pickle" if use_national_corpus else filename + "_pwr.pickle"
        file_location = path.join(CLASSIFIERS_DIR, filename)
        csv_reader = CsvReader(use_national_corpus=use_national_corpus)
        classifier, elapsed_time = train_target(classifier_object, self.feature_extractor, csv_reader)
        save_classifier(file_location, classifier)
        logging.info('--> Trained model' + str(classifier_object) +
                  '\n---> Training time: ' + elapsed_time +
                  '\n---> Saved in: ' + file_location)

    @staticmethod
    def load_national_tagger(filename):
        filename += "_nc.pickle"
        return load_classifier(path.join(CLASSIFIERS_DIR, filename))

    @staticmethod
    def load_pwr_tagger(filename):
        filename += "_pwr.pickle"
        return load_classifier(path.join(CLASSIFIERS_DIR, filename))

    def load_all_taggers(self):
        taggers = OrderedDict()
        for tagger_filename in TAGGER_FILENAMES:
            taggers[tagger_filename + '_pwr'] = self.load_pwr_tagger(tagger_filename)
            taggers[tagger_filename + '_nc'] = self.load_national_tagger(tagger_filename)
        return taggers

    def get_feature_extractor(self):
        return self.feature_extractor
