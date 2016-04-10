from itertools import islice

from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder

from src.utils.csv_reader import CsvReader


class SklearnWrapper(object):

    def __init__(self, classifier, dtype=int, sparse=True, sort=False):

        self._classifier = classifier
        self._encoder = LabelEncoder()
        self._vectorizer = DictVectorizer(dtype=dtype, sparse=sparse, sort=sort)

    def __repr__(self):
        return "<SklearnWrapper(%r)>" % self._classifier

    def train(self, X, y):

        X = self._vectorizer.fit_transform(X)
        y = self._encoder.fit_transform(y)
        self._classifier.fit(X, y)

    def classify(self, feature_set):
        feature_set = self._vectorizer.transform(feature_set)
        return self._encoder.classes_[self._classifier.predict(feature_set)][0]

    def accuracy(self, is_test_corpus_national, number_of_testing_features, feature_extractor):
        reader = CsvReader(use_national_corpus=is_test_corpus_national)
        total = 0
        good = 0
        for word, tag in islice(zip(reader.extract_feature('word'),
                                    reader.extract_feature('tag')), 0, number_of_testing_features):
            if self.classify(feature_extractor.pos_features(word)) == tag:
                good += 1
            total += 1

        return (good/total) * 100
