from collections import deque
from argparse import ArgumentParser, FileType

from nltk import word_tokenize
from numpy import ndarray

from src.factories.tagger_factory import TaggerFactory
from src.utils.xml_creator import XmlCreator


def main():
    parser = ArgumentParser("Text tagger")
    parser.add_argument("-f", type=FileType("r"), required=False, help="Optional input text file.")
    args = parser.parse_args()

    factory = TaggerFactory()
    taggers = [(tagger_name, tagger, deque([None, None], maxlen=2))
               for tagger_name, tagger in factory.load_all_taggers().items()]
    feature_extractor = factory.get_feature_extractor()

    if args.f is None:
        text = input("Provide a text input: ")
    else:
        text = args.f.read()

    words = [word for word in word_tokenize(text) if word.isalpha()]
    xml_creator = XmlCreator()

    for word in words:
        xml_creator.create_new_root("token")
        xml_creator.add_word(word)
        for tagger_name, tagger, last_run_tag in taggers:
            tag = tagger.classify(feature_extractor.pos_features(
                word, n_1_tag=last_run_tag[0], n_2_tag=last_run_tag[1]))
            if isinstance(tag, ndarray):  # neural network output is nd-array
                tag = tag[0]
            last_run_tag.appendleft(tag)
            print("Word:", word, " ---> Tag:", tag, "Tagger name:", tagger_name)
            xml_creator.add_tagger(tagger_name, tag)
        xml_creator.save_xml(word)


if __name__ == '__main__':
    main()
