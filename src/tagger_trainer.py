from sklearn import tree
from os import path, mkdir
from src.sklearn_wrapper import SklearnWrapper
from src.utils import SuffixUnpacker, PosFeatureExtractor, XmlReader, save_classifier
from src.settings import SUFFIX_FILE, CORPUS_DIR, CLASSIFIERS_DIR, SUFFIX_TAGGER, N_ONE_LETTER, N_TWO_LETTERS, \
                         N_THREE_LETTERS, N_FOUR_LETTERS
from itertools import islice

def main():
    clf = SklearnWrapper(tree.DecisionTreeClassifier())
    print("Tagger Trainer Start")
    print("Extracting features...")
    suffix_unpacker = SuffixUnpacker(SUFFIX_FILE)

    one_letter_suffixes = suffix_unpacker.extract_n_best_one_letter(N_ONE_LETTER)
    two_letters_suffixes = suffix_unpacker.extract_n_best_two_letters(N_TWO_LETTERS)
    three_letters_suffixes = suffix_unpacker.extract_n_best_three_letters(N_THREE_LETTERS)
    four_letters_suffixes = suffix_unpacker.extract_n_best_four_letter(N_FOUR_LETTERS)

    feature_extractor = PosFeatureExtractor(one_letter_suffixes, two_letters_suffixes, three_letters_suffixes,
                                            four_letters_suffixes)

    reader = XmlReader(CORPUS_DIR)
    X = []
    y = []
    for word, tag in islice(reader.extract_words_and_tags(), 0, 30):
        X.append(feature_extractor.pos_features(word))
        y.append(tag)

    clf.train(X,y)

    if not path.exists(CLASSIFIERS_DIR):
        mkdir(CLASSIFIERS_DIR)

    save_classifier(path.join(CLASSIFIERS_DIR, SUFFIX_TAGGER), clf)

if __name__ == '__main__':
    main()