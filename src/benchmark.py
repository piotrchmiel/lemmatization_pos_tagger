from collections import OrderedDict

from src.factories.tagger_factory import TaggerFactory
from src.settings import TAGGER_FILENAMES


def main():
    factory = TaggerFactory()
    feature_extractor = factory.get_feature_extractor()

    taggers = OrderedDict()

    for filename in TAGGER_FILENAMES:
        taggers[filename + '_pwr'] = factory.create_tagger_from_file(filename, False)
        taggers[filename + '_nc'] = factory.create_tagger_from_file(filename, True)

    for name, tagger in taggers.items():
        if "pwr" in name:
            print(tagger + "\t:", tagger.accuracy(True, 100, feature_extractor))
        else:
            print(tagger + "\t:", tagger.accuracy(False, 100, feature_extractor))

if __name__ == '__main__':
    main()
