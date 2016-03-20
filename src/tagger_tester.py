from os import path
from src.utils import load_classifier, SuffixUnpacker, PosFeatureExtractor
from src.settings import CLASSIFIERS_DIR, SUFFIX_TAGGER, SUFFIX_FILE, N_ONE_LETTER, N_TWO_LETTERS, N_THREE_LETTERS, \
                        N_FOUR_LETTERS


def main():

    suffix_unpacker = SuffixUnpacker(SUFFIX_FILE)

    one_letter_suffixes = suffix_unpacker.extract_n_best_one_letter(N_ONE_LETTER)
    two_letters_suffixes = suffix_unpacker.extract_n_best_two_letters(N_TWO_LETTERS)
    three_letters_suffixes = suffix_unpacker.extract_n_best_three_letters(N_THREE_LETTERS)
    four_letters_suffixes = suffix_unpacker.extract_n_best_four_letters(N_FOUR_LETTERS)

    feature_extractor = PosFeatureExtractor(one_letter_suffixes, two_letters_suffixes, three_letters_suffixes,
                                            four_letters_suffixes)

    clf = load_classifier(path.join(CLASSIFIERS_DIR, SUFFIX_TAGGER))

    word = "siedzieć"

    print(clf.classify(feature_extractor.pos_features(word)))

if __name__ == '__main__':
    main()
