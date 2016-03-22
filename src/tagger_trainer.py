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

    factory.create_tagger(DecisionTreeClassifier(), False, "tagger_decision_tree")
    factory.create_tagger(SGDClassifier(), False, "sdg")
    factory.create_tagger(LogisticRegression(), False, "logistic_regression")
    factory.create_tagger(BernoulliNB(), False, "naive_bayes")
    factory.create_tagger(SVC(), False, "svm")
    factory.create_tagger(KNeighborsClassifier(), False, "kneighbors")
    factory.create_tagger(Classifier(layers=[Layer("Rectifier", units=100), Layer("Softmax")],
                                     learning_rate=0.02, n_iter=10), False, "neural_network")
    factory.create_tagger(DecisionTreeClassifier(), True, "tagger_decision_tree")
    factory.create_tagger(SGDClassifier(), True, "sdg")
    factory.create_tagger(LogisticRegression(), True, "logistic_regression")
    factory.create_tagger(BernoulliNB(), True, "naive_bayes")
    factory.create_tagger(SVC(), True, "svm")
    factory.create_tagger(KNeighborsClassifier(), True, "kneighbors")
    factory.create_tagger(Classifier(layers=[Layer("Rectifier", units=100), Layer("Softmax")],
                                     learning_rate=0.02, n_iter=10), True, "neural_network")

if __name__ == '__main__':
    main()
