from os import walk, path

from bs4 import BeautifulSoup

from src.utils.extractor import PosFeatureExtractor


class XmlReader(object):
    def __init__(self, corpus_dir, use_national_corpus=False):
        self.corpus_dir = corpus_dir
        self.use_national_corpus = use_national_corpus

    def extract_words_and_tags(self):
        for filename in self.find_xml_files():
            for word, ctag, base in self.get_words(filename):
                yield word, ctag, base

    def get_words(self, filename):
        with open(filename, encoding='utf8') as file_handler:
            tokens_str = 'seg' if self.use_national_corpus else 'tok'
            tokens = BeautifulSoup(file_handler.read(), 'xml').find_all(tokens_str)
            if self.use_national_corpus:
                return self.get_words_national(tokens)
            else:
                return self.get_words_pwr(tokens)

    @staticmethod
    def get_words_pwr(tokens):
        for token in tokens:
            try:
                word = token.orth.string
                ctag = PosFeatureExtractor.tag_mapper(token.find('lex').ctag.string)
                base = token.find('lex', {'disamb': '1'}).base.string
            except Exception:
                pass
            else:
                if ctag is not None and word is not None and len(word) != 1 and base is not None:
                    yield word, ctag, base

    @staticmethod
    def get_words_national(tokens):
        for token in tokens:
            try:
                word = token.find('f', attrs={'name': 'orth'}).find('string').string
                ctag = PosFeatureExtractor.tag_mapper(':'.join(
                    token.find('f', attrs={'name': 'disamb'}).find(
                        'f', attrs={'name': 'interpretation'}).find(
                        'string').string.split(':')[1:]))
                base = token.find('f', attrs={'name': 'disamb'}).find('f', attrs={'name': 'interpretation'}).\
                             find('string').string.split(':')[0]
            except Exception:
                pass
            else:
                if ctag is not None and word is not None and len(word) != 1 and base is not None:
                    yield word, ctag, base

    def find_xml_files(self):
        for root, _, files in walk(self.corpus_dir):
            for filename in files:
                if self.use_national_corpus:
                    query = filename == "ann_morphosyntax.xml"
                else:
                    query = filename.endswith(".xml") and not filename.endswith(".rel.xml")
                if query:
                    yield path.join(root, filename)
