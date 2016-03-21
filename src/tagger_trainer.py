from os import path

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sknn.mlp import Classifier

from src.settings import SUFFIX_FILE, CORPUS_DIR, N_ONE_LETTER, N_TWO_LETTERS, \
                         N_THREE_LETTERS, N_FOUR_LETTERS
from src.utils import SuffixUnpacker, PosFeatureExtractor, train_target


def main():
    print("Tagger Trainer Start")
    print("Extracting features...")
    suffix_unpacker = SuffixUnpacker(SUFFIX_FILE)

    one_letter_suffixes = suffix_unpacker.extract_n_best_one_letter(N_ONE_LETTER)
    two_letters_suffixes = suffix_unpacker.extract_n_best_two_letters(N_TWO_LETTERS)
    three_letters_suffixes = suffix_unpacker.extract_n_best_three_letters(N_THREE_LETTERS)
    four_letters_suffixes = suffix_unpacker.extract_n_best_four_letters(N_FOUR_LETTERS)

    feature_extractor = PosFeatureExtractor(one_letter_suffixes, two_letters_suffixes,
                                            three_letters_suffixes, four_letters_suffixes)

    if not path.isfile(path.join(CORPUS_DIR, "extracted.csv")):
        print("No CSV File")
    else:
        print("Csv file found. Gonna use it.")

        train_target(DecisionTreeClassifier, feature_extractor, CORPUS_DIR, "tagger_decision_tree_pwr.pickle")
        train_target(SGDClassifier, feature_extractor, CORPUS_DIR, "sgd_pwr.pickle")
        train_target(LogisticRegression, feature_extractor, CORPUS_DIR, "logistic_regression.pickle")
        train_target(BernoulliNB, feature_extractor, CORPUS_DIR, "naive_bayes_pwr.pickle")
        train_target(SVC, feature_extractor, CORPUS_DIR, "svm_pwr.pickle")
        train_target(KNeighborsClassifier, feature_extractor, CORPUS_DIR, "kneighbors_pwr.pickle")
        train_target(Classifier, feature_extractor, CORPUS_DIR, "neural_network_pwr.pickle")


if __name__ == '__main__':
    main()
