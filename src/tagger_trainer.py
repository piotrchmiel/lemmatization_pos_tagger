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

    parallel_option = ''
    try:
        opts, args = getopt.getopt(argv,'hp:', ['help', 'parallel='])
    except getopt.GetoptError:
        print('tagger_trainer.py --parallel <y/n>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('tagger_trainer.py --parallel <y/n>')
            sys.exit()
        elif opt in ("-p", "--parallel"):
            if arg not in ('y', 'n'):
                print("--parallel argument takes 'y' or 'n' input. Given: ", arg)
                sys.exit(2)
            parallel_option = arg


    factory = TaggerFactory()

    algorithms = {'tagger_decision_tree': DecisionTreeClassifier(), 'sdg': SGDClassifier(), 'svm': SVC(),
                  'logistic_regression': LogisticRegression(), 'naive_bayes': BernoulliNB(),
                  'kneighbors': KNeighborsClassifier(),
                  'neural_network': Classifier(layers=[Layer("Rectifier",
                                                             units=100),
                                                       Layer("Softmax")],
                                               learning_rate=0.02, n_iter=10)}

    if (parallel_option == 'n'):
        print("Parallelization is disabled")
        for filename, algorithm in algorithms.items():
            factory.dump_tagger(deepcopy(algorithm), filename, True)
            factory.dump_tagger(deepcopy(algorithm), filename, False)

    else:
        print("Parallelization is enabled")
        Parallel(n_jobs=-1)(chain((delayed(factory.dump_tagger)(deepcopy(algorithm), filename, True)
                            for filename, algorithm in algorithms.items()),
                            (delayed(factory.dump_tagger)(deepcopy(algorithm), filename, False)
                            for filename, algorithm in algorithms.items())))

if __name__ == '__main__':
    main(sys.argv[1:])
