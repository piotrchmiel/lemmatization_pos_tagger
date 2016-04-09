class PosFeatureExtractor(object):
    def __init__(self, one_letter_suffixes, two_letters_suffixes, three_letters_suffixes,
                 four_letters_suffixes):
        self.common_suffixes = {word for word, _ in one_letter_suffixes}
        self.common_suffixes.update({word for word, _ in two_letters_suffixes})
        self.common_suffixes.update({word for word, _ in three_letters_suffixes})
        self.common_suffixes.update({word for word, _ in four_letters_suffixes})

    def pos_features(self, word):
        features = {}
        for suffix in self.common_suffixes:
            if word.lower().endswith(suffix):
                features['endswith({})'.format(suffix)] = True
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
