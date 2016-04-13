from os import path, makedirs
from lxml.etree import Element, SubElement, ElementTree

from src.settings import OUTPUT_XML_DIR


class XmlCreator(object):
    def __init__(self):
        self.root = None

    def create_new_root(self, root):
        self.root = Element(root)

    def add_word(self, word_text):
        SubElement(self.root, "word").text = word_text

    def add_tagger(self, classifier_name, tag_text):
        tagger = SubElement(self.root, "tagger")
        SubElement(tagger, "classifier").text = classifier_name
        SubElement(tagger, "tag").text = tag_text

    def save_xml(self, filename):
        if not path.exists(OUTPUT_XML_DIR):
            makedirs(OUTPUT_XML_DIR)
        full_path = path.join(OUTPUT_XML_DIR, filename + ".xml")
        tree = ElementTree(self.root)
        tree.write(full_path, method="xml")
