from argparse import ArgumentParser
from copy import deepcopy
from itertools import chain

from joblib import Parallel, delayed
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sknn.mlp import Classifier, Layer

from src.factories.tagger_factory import TaggerFactory
from src.settings import NN_UNITS, NN_LEARNING_RATE, NN_ITERATIONS


def main():
    parser = ArgumentParser("Tagger trainer")
    parser.add_argument('--n-jobs', '-n', default=-1, type=int, help="Number of used CPU cores. Default: all cores")
    args = parser.parse_args()

    factory = TaggerFactory()

    algorithms = {'tagger_decision_tree': DecisionTreeClassifier(), 'sdg': SGDClassifier(), 'svm': SVC(),
                  'logistic_regression': LogisticRegression(), 'naive_bayes': BernoulliNB(),
                  'kneighbors': KNeighborsClassifier(),
                  'neural_network': Classifier(layers=[Layer("Rectifier", units=NN_UNITS), Layer("Softmax")],
                                               learning_rate=NN_LEARNING_RATE,
                                               n_iter=NN_ITERATIONS)}

    Parallel(n_jobs=args.n_jobs)(chain((delayed(factory.dump_tagger)(deepcopy(algorithm), filename, True)
                                        for filename, algorithm in algorithms.items()),
                                       (delayed(factory.dump_tagger)(deepcopy(algorithm), filename, False)
                                        for filename, algorithm in algorithms.items())))


if __name__ == '__main__':
    main()
