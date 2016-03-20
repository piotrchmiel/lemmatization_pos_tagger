from src.settings import SUFFIX_FILE
from src.utils import SuffixUnpacker
from unittest import TestCase


class TestSuffixUnpacker(TestCase):
    def setUp(self):
        self.unpacker = SuffixUnpacker(SUFFIX_FILE)
        self.num_of_extracted_suffixes = 10

    def test_extract_n_best_one_letter(self):
        extracted_one_letter_suffixes = self.unpacker.extract_n_best_one_letter(self.num_of_extracted_suffixes)
        for suffix_with_count in extracted_one_letter_suffixes:
            suffix = suffix_with_count[0]
            self.assertEqual(len(suffix), 1)

    def test_extract_n_best_two_letters(self):
        extracted_two_letter_suffixes = self.unpacker.extract_n_best_two_letters(self.num_of_extracted_suffixes)
        for suffix_with_count in extracted_two_letter_suffixes:
            suffix = suffix_with_count[0]
            self.assertEqual(len(suffix), 2)

    def test_extract_n_best_three_letters(self):
        extracted_three_letter_suffixes = self.unpacker.extract_n_best_three_letters(self.num_of_extracted_suffixes)
        for suffix_with_count in extracted_three_letter_suffixes:
            suffix = suffix_with_count[0]
            self.assertEqual(len(suffix), 3)

    def test_extract_n_best_four_letter(self):
        extracted_four_letter_suffixes = self.unpacker.extract_n_best_four_letters(self.num_of_extracted_suffixes)
        for suffix_with_count in extracted_four_letter_suffixes:
            suffix = suffix_with_count[0]
            self.assertEqual(len(suffix), 4)
