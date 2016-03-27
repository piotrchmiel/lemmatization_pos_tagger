import filecmp
import os
from unittest import TestCase

from src.utils.csv_reader import CsvReader


class TestCsvReader(TestCase):
    def setUp(self):
        self.template_csv_path = "TestCsv/test_template.csv"
        self.path_to_test_csv = "TestCsv/test.csv"
        self.test_corpus_dir = "TestCorpus"
        self.reader = CsvReader(use_national_corpus=True)
        self.reader.csv_file_path = self.path_to_test_csv
        self.reader.corpus_dir = self.test_corpus_dir

    def tearDown(self):
        os.remove(self.path_to_test_csv)

    def test_convert_xml_to_csv(self):
        self.reader.convert_xml_to_csv()
        self.assertTrue(filecmp.cmp(self.reader.csv_file_path, self.template_csv_path))

    def test_extract_feature(self):
        self.reader.convert_xml_to_csv()
        words_with_tags = (('Powód', 'rzeczownik'), ('był', 'pseudoimiesłów'), ('prosty', 'przymiotnik'))
        extracted = [w for w in zip(self.reader.extract_feature('word'), self.reader.extract_feature('tag'))]
        self.assertSequenceEqual(words_with_tags, extracted)
