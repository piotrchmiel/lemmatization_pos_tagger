from nltk import word_tokenize

from src.factories.tagger_factory import TaggerFactory
from src.settings import TAGGER_FILENAMES


def main():
    factory = TaggerFactory()
    taggers = {}
    feature_extractor = factory.get_feature_extractor()

    for filename in TAGGER_FILENAMES:
        taggers[filename + '_pwr'] = factory.create_tagger_from_file(filename, False)
        taggers[filename + '_nc'] = factory.create_tagger_from_file(filename, True)

    text = input("Wprowadź tekst: ")

    words = word_tokenize(text)
    print(words)
    for word in words:
        for tagger_name, tagger in taggers.items():
            print(tagger.classify(feature_extractor.pos_features(word)))


if __name__ == '__main__':
    main()
