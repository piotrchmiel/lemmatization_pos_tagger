from src.settings import N_ONE_LETTER, N_OTHER_LETTERS


class PosFeatureExtractor(object):
    def __init__(self, suffix_unpacker):
        self.common_suffixes = {word for word, _ in suffix_unpacker.extract_n_best_k_letters(1, N_ONE_LETTER)}
        for length in range(1, suffix_unpacker.get_number_of_suffixes()):
            self.common_suffixes.update({word for word, _ in suffix_unpacker.extract_n_best_k_letters(
                length, N_OTHER_LETTERS)})

    def pos_features(self, word, n_1_tag=None, n_2_tag=None):
        features = {}
        for suffix in self.common_suffixes:
            if word.lower().endswith(suffix):
                features['endswith({})'.format(suffix)] = True
        if n_1_tag is not None:
            features['n-1 word'] = n_1_tag
        if n_2_tag is not None:
            features['n-2 word'] = n_2_tag
        return features

    @staticmethod
    def tag_mapper(word):
        parts_of_speech = {
            'subst': 'rzeczownik',
            'depr': 'rzeczownik',
            'num': 'liczebnik',
            'numcol': 'liczebnik',
            'adj': 'przymiotnik',
            'adja': 'przymiotnik.',
            'adjp': 'przymiotnik',
            'adjc': 'przymiotnik',
            'adv': 'przysłówek',
            'ppron12': 'zaimek',
            'ppron3': 'zaimek',
            'siebie': 'zaimek',
            'fin': 'czasownik',
            'bedzie': 'czasownik',
            'aglt': 'czasownik',
            'praet': 'czasownik',
            'impt': 'czasownik',
            'imps': 'czasownik',
            'inf': 'czasownik',
            'pcon': 'czasownik',
            'pant': 'czasownik',
            'ger': 'czasownik',
            'pact': 'czasownik',
            'ppas': 'czasownik',
            'winien': 'czasownik',
            'pred': 'czasownik',
            'prep': 'przyimek',
            'conj': 'spójnik',
            'comp': 'spójnik',
            'qub': 'partykuła',
            'brev': 'forma nierozpoznana',
            'burk': 'forma nierozpoznana',
            'interj': 'przyimek',
            'interp': 'forma nierozpoznana',
            'xxx': 'forma nierozpoznana',
            'ign': 'forma nierozpoznana'
        }
        return parts_of_speech[word.split(':')[0]]
