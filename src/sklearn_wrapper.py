from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder

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

    def accuracy(self, corpus_dir, reader, feature_extractor):
        reader = reader(corpus_dir)
        total = 0
        good = 0
        for word, tag in zip(reader.extract_feature('word'), reader.extract_feature('tag')):
            if self.classify(feature_extractor.pos_features(word)) == tag:
                good+=1
            total += 1

        return good/total

