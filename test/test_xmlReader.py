from unittest import TestCase

from src.utils.xml_reader import XmlReader


class TestXmlReader(TestCase):
    def setUp(self):
        self.test_corpus_dir = "TestCorpus"
        self.xmlReader = XmlReader(self.test_corpus_dir, use_national_corpus=True)

    def test_find_xml_files(self):
        expected_number_of_xml_files = 1
        self.assertEqual(expected_number_of_xml_files, len(list(self.xmlReader.find_xml_files())))

    def test_extract_words_and_tags(self):
        expected_number_of_extracted_pairs = 3
        expected_pairs = [('Powód', 'rzeczownik'), ('był', 'pseudoimiesłów'), ('prosty', 'przymiotnik')]
        extracted_pairs = list(self.xmlReader.extract_words_and_tags())
        self.assertEqual(expected_number_of_extracted_pairs, len(extracted_pairs))
        self.assertSequenceEqual(expected_pairs, extracted_pairs)
