from os import walk, path

from bs4 import BeautifulSoup

from src.utils.extractor import PosFeatureExtractor


class XmlReader(object):
    def __init__(self, folder_name, national_corpus=False):
        self.folder = folder_name
        self.national_corpus = national_corpus

    def extract_words_and_tags(self):
        for filename in self.find_xml_files():
            for word, ctag in self.get_words(filename):
                yield word, ctag

    def get_words(self, filename):
        with open(filename) as file_handler:
            tokens_str = 'tok' if not self.national_corpus else 'seg'
            tokens = BeautifulSoup(file_handler.read(), 'xml').find_all(tokens_str)
            if self.national_corpus:
                return self.get_words_national(tokens)
            else:
                return self.get_words_pwr(tokens)

    def get_words_pwr(self, tokens):
        for token in tokens:
            try:
                word = ctag = None
                word = token.orth.string
                ctag = PosFeatureExtractor.tag_mapper(token.find('lex').ctag.string)
            except Exception:
                pass
            else:
                if ctag is not None and word is not None and len(word) != 1:
                    yield word, ctag

    def get_words_national(self, tokens):
        for token in tokens:
            try:
                word = token.find('f', attrs={'name': 'orth'}).find('string').string
                ctag = PosFeatureExtractor.tag_mapper(':'.join(
                    token.find('f', attrs={'name': 'disamb'}).find(
                        'f', attrs={'name': 'interpretation'}).find(
                            'string').string.split(':')[1:]))
            except Exception:
                pass
            else:
                if ctag is not None and word is not None and len(word) != 1:
                    yield word, ctag

    def find_xml_files(self):
        for root, _, files in walk(self.folder):
            for filename in files:
                query = False
                if self.national_corpus:
                    query = filename == "ann_morphosyntax.xml"
                else:
                    query = filename.endswith(".xml") and not filename.endswith(".rel.xml")
                if query:
                    yield path.join(root, filename)
