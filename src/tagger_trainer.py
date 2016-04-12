import sys, getopt
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


def main(argv):

    help = 'tagger_trainer.py --n-jobs int (default: 1; all cores: -1)'
    n_jobs = 1
    try:
        opts, args = getopt.getopt(argv,'hn:', ['help', 'n-jobs='])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit()
        elif opt in ("-n", "--n-jobs"):
            if not arg.isdigit():
                print("--n-jobs argument takes an integer. Given: ", arg)
                sys.exit(2)
            n_jobs = int(arg)


    factory = TaggerFactory()

    algorithms = {'tagger_decision_tree': DecisionTreeClassifier(), 'sdg': SGDClassifier(), 'svm': SVC(),
                  'logistic_regression': LogisticRegression(), 'naive_bayes': BernoulliNB(),
                  'kneighbors': KNeighborsClassifier(),
                  'neural_network': Classifier(layers=[Layer("Rectifier",
                                                             units=100),
                                                       Layer("Softmax")],
                                               learning_rate=0.02, n_iter=10)}

    Parallel(n_jobs=n_jobs)(chain((delayed(factory.dump_tagger)(deepcopy(algorithm), filename, True)
                        for filename, algorithm in algorithms.items()),
                        (delayed(factory.dump_tagger)(deepcopy(algorithm), filename, False)
                        for filename, algorithm in algorithms.items())))

if __name__ == '__main__':
    main(sys.argv[1:])
