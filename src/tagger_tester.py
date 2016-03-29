from collections import OrderedDict

from src.factories.tagger_factory import TaggerFactory
from src.settings import TAGGER_FILENAMES


def main():
    factory = TaggerFactory()
    feature_extractor = factory.get_feature_extractor()
    taggers = OrderedDict()

    for filename in TAGGER_FILENAMES:
        taggers[filename + '_pwr'] = factory.create_pwr_tagger_from_file(filename)
        taggers[filename + '_nc'] = factory.create_national_tagger_from_file(filename)

    word = input("Podaj słowo: ")

    for name, tagger in taggers.items():
        print("{0:25} : {1}".format(name, tagger.classify(feature_extractor.pos_features(word))))


if __name__ == '__main__':
    main()
