from unittest import TestCase

from src.utils.extractor import PosFeatureExtractor


class TestPosFeatureExtractor(TestCase):
    def setUp(self):
        mock_one_letters_suf = [('a', 1), ('b', 2)]
        mock_two_letters_suf = [('aa', 1), ('bb', 2)]
        mock_three_letters_suf = [('aaa', 1), ('bbb', 2)]
        mock_four_letters_suf = [('aaaa', 1), ('bbbb', 2)]

        self.extractor = PosFeatureExtractor(mock_one_letters_suf,
                                             mock_two_letters_suf,
                                             mock_three_letters_suf,
                                             mock_four_letters_suf)

    def test_init(self):
        mock_common_suffixes = {'a', 'b', 'aa', 'bb', 'aaa', 'bbb', 'aaaa', 'bbbb'}
        self.assertSetEqual(self.extractor.common_suffixes, mock_common_suffixes)

    def test_pos_features(self):
        self.assertTrue(self.extractor.pos_features("worda")["endswith(a)"])
        self.assertTrue(self.extractor.pos_features("wordaa")["endswith(a)"])
        self.assertTrue(self.extractor.pos_features("wordaa")["endswith(aa)"])
        self.assertTrue(self.extractor.pos_features("wordbbb")["endswith(bbb)"])

        with self.assertRaises(KeyError):
            self.extractor.pos_features("worda")["endswith(aa)"]

        with self.assertRaises(KeyError):
            self.extractor.pos_features("wordaa")["endswith(bb)"]

        with self.assertRaises(KeyError):
            self.extractor.pos_features("wordbbb")["endswith(bbbb)"]
