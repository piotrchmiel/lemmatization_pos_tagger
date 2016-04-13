from nltk import word_tokenize
from numpy import ndarray

from src.factories.tagger_factory import TaggerFactory
from src.settings import TAGGER_FILENAMES
from src.utils.xml_creator import XmlCreator


def main():
    factory = TaggerFactory()
    taggers = {}
    feature_extractor = factory.get_feature_extractor()

    for tagger_filename in TAGGER_FILENAMES:
        taggers[tagger_filename + '_pwr'] = factory.load_pwr_tagger(tagger_filename)
        taggers[tagger_filename + '_nc'] = factory.load_national_tagger(tagger_filename)

    text = input("Provide a text input: ")
    words = word_tokenize(text)
    xml_creator = XmlCreator()

    for word in words:
        xml_creator.create_new_root("token")
        xml_creator.add_word(word)
        for tagger_name, tagger in taggers.items():
            tag = tagger.classify(feature_extractor.pos_features(word))
            if isinstance(tag, ndarray): # neural network output is nd-array
                tag = tag[0]
            print("Word:", word, "Tag:", tag, "Tagger name:", tagger_name)
            xml_creator.add_tagger(tagger_name, tag)
        xml_creator.save_xml(word)


if __name__ == '__main__':
    main()
