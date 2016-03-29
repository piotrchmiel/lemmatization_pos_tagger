from collections import OrderedDict

from src.factories.tagger_factory import TaggerFactory
from src.settings import TAGGER_FILENAMES


def main():
    factory = TaggerFactory()
    feature_extractor = factory.get_feature_extractor()

    taggers = OrderedDict()

    for filename in TAGGER_FILENAMES:
        taggers[filename + '_pwr'] = factory.load_pwr_tagger(filename)
        taggers[filename + '_nc'] = factory.load_national_tagger(filename)

    for name, tagger in taggers.items():
        if "pwr" in name:
            print("{0:25} : {1:.3f}".format(name, tagger.accuracy(True, 100, feature_extractor)))
        else:
            print("{0:25} : {1:.3f}".format(name, tagger.accuracy(False, 100, feature_extractor)))

if __name__ == '__main__':
    main()
