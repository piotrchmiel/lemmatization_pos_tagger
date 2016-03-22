from nltk import word_tokenize

from src.factories.tagger_factory import TaggerFactory


def main():
    factory = TaggerFactory()
    taggers = {}
    feature_extractor = factory.get_feature_extractor()

    taggers['decision_tree_pwr'] = factory.create_tagger_from_file('tagger_decision_tree', False)
    taggers['sgd_pwr'] = factory.create_tagger_from_file('sgd', False)
    taggers['svc_pwr'] = factory.create_tagger_from_file('svm', False)
    taggers['logistic_regression_pwr'] = factory.create_tagger_from_file('logistic_regression', False)
    taggers['naive_bayes_pwr'] = factory.create_tagger_from_file('naive_bayes', False)
    taggers['k_neighbors_pwr'] = factory.create_tagger_from_file('kneighbors', False)
    taggers['neural_networks_pwr'] = factory.create_tagger_from_file('neural_network', False)
    taggers['decision_tree_nc'] = factory.create_tagger_from_file('tagger_decision_tree', True)
    taggers['sgd_nc'] = factory.create_tagger_from_file('sgd', True)
    taggers['svc_nc'] = factory.create_tagger_from_file('svm', True)
    taggers['logistic_regression_nc'] = factory.create_tagger_from_file('logistic_regression', True)
    taggers['naive_bayes_nc'] = factory.create_tagger_from_file('naive_bayes', True)
    taggers['k_neighbors_nc'] = factory.create_tagger_from_file('kneighbors', True)
    taggers['neural_networks_nc'] = factory.create_tagger_from_file('neural_network', True)

    text = input("Wprowadź tekst: ")

    words = word_tokenize(text)
    print(words)
    for word in words:
        for tagger_name, tagger in taggers.items():
            print(tagger.classify(feature_extractor.pos_features(word)))


if __name__ == '__main__':
    main()
