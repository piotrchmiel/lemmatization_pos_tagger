from copy import deepcopy

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sknn.mlp import Classifier, Layer

from src.factories.tagger_factory import TaggerFactory


def main():
    factory = TaggerFactory()

    algorithms = {'tagger_decision_tree': DecisionTreeClassifier(), 'sdg': SGDClassifier(), 'svm': SVC(),
                  'logistic_regression': LogisticRegression(), 'naive_bayes': BernoulliNB(),
                  'kneighbors': KNeighborsClassifier(),
                  'neural_network': Classifier(layers=[Layer("Rectifier",
                                                             units=100),
                                                       Layer("Softmax")],
                                               learning_rate=0.02, n_iter=10)}

    for filename, algorithm in algorithms.items():
        factory.create_tagger_for_pwr_corpus(deepcopy(algorithm), filename)
        factory.create_tagger_for_national_corpus(deepcopy(algorithm), filename)


if __name__ == '__main__':
    main()
