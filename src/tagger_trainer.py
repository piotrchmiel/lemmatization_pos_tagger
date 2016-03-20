from os import path, mkdir
from itertools import islice
from sklearn.svm import SVC
from src.sklearn_wrapper import SklearnWrapper
from src.utils import SuffixUnpacker, PosFeatureExtractor, CsvReader, save_classifier
from src.settings import SUFFIX_FILE, CORPUS_DIR, CLASSIFIERS_DIR, SUFFIX_TAGGER, N_ONE_LETTER, N_TWO_LETTERS, \
                         N_THREE_LETTERS, N_FOUR_LETTERS


def main():
    clf = SklearnWrapper(SVC())
    print("Tagger Trainer Start")
    print("Extracting features...")
    suffix_unpacker = SuffixUnpacker(SUFFIX_FILE)

    one_letter_suffixes = suffix_unpacker.extract_n_best_one_letter(N_ONE_LETTER)
    two_letters_suffixes = suffix_unpacker.extract_n_best_two_letters(N_TWO_LETTERS)
    three_letters_suffixes = suffix_unpacker.extract_n_best_three_letters(N_THREE_LETTERS)
    four_letters_suffixes = suffix_unpacker.extract_n_best_four_letters(N_FOUR_LETTERS)

    feature_extractor = PosFeatureExtractor(one_letter_suffixes, two_letters_suffixes, three_letters_suffixes,
                                            four_letters_suffixes)

    reader = CsvReader(CORPUS_DIR)

    if not path.isfile(path.join(CORPUS_DIR, "extracted.csv")):
        print("No CSV File")
    else:
        print("Csv file found. Gonna use it.")

        X = (feature_extractor.pos_features(word) for word in reader.extract_feature('word'))
        y = [tag for tag in reader.extract_feature('tag')]

        print("Training...")
        clf.train(X, y)
        print("Done.")

        if not path.exists(CLASSIFIERS_DIR):
            mkdir(CLASSIFIERS_DIR)

        print("Saving Model.")
        save_classifier(path.join(CLASSIFIERS_DIR, SUFFIX_TAGGER), clf)
        print("Done.")

if __name__ == '__main__':
    main()
