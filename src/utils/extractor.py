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
            'depr': 'rzeczownik deprecjatywny',
            'num': 'liczebnik główny',
            'numcol': 'liczebnik zbiorowy',
            'adj': 'przymiotnik',
            'adja': 'przymiotnik przyprzym.',
            'adjp': 'przymiotnik poprzyimkowy',
            'adjc': 'przymiotnik predykatywny',
            'adv': 'przysłówek',
            'ppron12': 'zaimek nietrzecioosobowy',
            'ppron3': 'zaimek trzecioosobowy',
            'siebie': 'zaimek siebie ',
            'fin': 'forma nieprzeszła',
            'bedzie': 'forma przyszła być ',
            'aglt': 'aglutynant być ',
            'praet': 'pseudoimiesłów',
            'impt': 'rozkaźnik',
            'imps': 'bezosobnik',
            'inf': 'bezokolicznik',
            'pcon': 'im. przys. współczesny',
            'pant': 'im. przys. uprzedni',
            'ger': 'odsłownik',
            'pact': 'im. przym. czynny',
            'ppas': 'im. przym. bierny',
            'winien': 'winien',
            'pred': 'predykatyw',
            'prep': 'przyimek',
            'conj': 'spójnik współrzędny',
            'comp': 'spójnik podrzędny',
            'qub': 'kublik',
            'brev': 'skrót',
            'burk': 'burkinostka',
            'interj': 'wykrzyknik',
            'interp': 'interpunkcja',
            'xxx': 'ciało obce',
            'ign': 'forma nierozpoznana'
        }
        return parts_of_speech[word.split(':')[0]]
