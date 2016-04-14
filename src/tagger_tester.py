from src.factories.tagger_factory import TaggerFactory


def main():
    factory = TaggerFactory()
    feature_extractor = factory.get_feature_extractor()
    taggers = factory.load_all_taggers()

    word = input("Please provide a word to tag: ")

    for name, tagger in taggers.items():
        print("{0:25} : {1}".format(name, tagger.classify(feature_extractor.pos_features(word))))


if __name__ == '__main__':
    main()
