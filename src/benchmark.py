from os import path

from src.settings import CLASSIFIERS_DIR, SUFFIX_FILE, N_ONE_LETTER, N_TWO_LETTERS, N_THREE_LETTERS, \
                        N_FOUR_LETTERS, CORPUS_DIR
from src.utils import load_classifier, SuffixUnpacker, PosFeatureExtractor, CsvReader


def main():

    suffix_unpacker = SuffixUnpacker(SUFFIX_FILE)

    one_letter_suffixes = suffix_unpacker.extract_n_best_one_letter(N_ONE_LETTER)
    two_letters_suffixes = suffix_unpacker.extract_n_best_two_letters(N_TWO_LETTERS)
    three_letters_suffixes = suffix_unpacker.extract_n_best_three_letters(N_THREE_LETTERS)
    four_letters_suffixes = suffix_unpacker.extract_n_best_four_letters(N_FOUR_LETTERS)

    feature_extractor = PosFeatureExtractor(one_letter_suffixes, two_letters_suffixes, three_letters_suffixes,
                                            four_letters_suffixes)

    decision_tree = load_classifier(path.join(CLASSIFIERS_DIR, 'tagger_decision_tree_pwr.pickle'))
    sgd = load_classifier(path.join(CLASSIFIERS_DIR, "sgd_pwr.pickle"))
    svc = load_classifier(path.join(CLASSIFIERS_DIR, 'svm_pwr.pickle'))
    logistic_regression = load_classifier(path.join(CLASSIFIERS_DIR, 'logistic_regression.pickle'))
    naive_bayes = load_classifier(path.join(CLASSIFIERS_DIR, 'naive_bayes_pwr.pickle'))
    k_neighbors = load_classifier(path.join(CLASSIFIERS_DIR, 'kneighbors_pwr.pickle'))
    neural_networks = load_classifier(path.join(CLASSIFIERS_DIR, 'neural_network_pwr.pickle'))

    print("Support Vector Machine PWr Tagger      :", svc.accuracy(CORPUS_DIR, CsvReader, feature_extractor))
    print("Decision Tree PWr Tagger               :", decision_tree.accuracy(CORPUS_DIR, CsvReader, feature_extractor))
    print("Stochastic Gradient Descent PWr Tagger :", sgd.accuracy(CORPUS_DIR, CsvReader, feature_extractor))
    print("Logistic Regression PWr Tagger         :", logistic_regression.accuracy(CORPUS_DIR, CsvReader, feature_extractor))
    print("Naive Bayes PWr Tagger                 :", naive_bayes.accuracy(CORPUS_DIR, CsvReader, feature_extractor))
    print("K Neighbors PWr Tagger                 :", k_neighbors.accuracy(CORPUS_DIR, CsvReader, feature_extractor))
    print("Neural Networks PWr Tagger             :", neural_networks.accuracy(CORPUS_DIR, CsvReader, feature_extractor))

if __name__ == '__main__':
    main()
