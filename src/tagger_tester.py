from src.factories.tagger_factory import TaggerFactory


def main():
    factory = TaggerFactory()
    feature_extractor = factory.get_feature_extractor()

    decision_tree_pwr = factory.create_tagger_from_file('tagger_decision_tree', False)
    sgd_pwr = factory.create_tagger_from_file('sgd', False)
    svc_pwr = factory.create_tagger_from_file('svm', False)
    logistic_regression_pwr = factory.create_tagger_from_file('logistic_regression', False)
    naive_bayes_pwr = factory.create_tagger_from_file('naive_bayes', False)
    k_neighbors_pwr = factory.create_tagger_from_file('kneighbors', False)
    neural_networks_pwr = factory.create_tagger_from_file('neural_network', False)
    decision_tree_nc = factory.create_tagger_from_file('tagger_decision_tree', True)
    sgd_nc = factory.create_tagger_from_file('sgd', True)
    svc_nc = factory.create_tagger_from_file('svm', True)
    logistic_regression_nc = factory.create_tagger_from_file('logistic_regression', True)
    naive_bayes_nc = factory.create_tagger_from_file('naive_bayes', True)
    k_neighbors_nc = factory.create_tagger_from_file('kneighbors', True)
    neural_networks_nc = factory.create_tagger_from_file('neural_network', True)

    word = input("Podaj słowo: ")

    print("Decision Tree PWr Tagger               :", decision_tree_pwr.classify(feature_extractor.pos_features(word)))
    print("Stochastic Gradient Descent PWr Tagger :", sgd_pwr.classify(feature_extractor.pos_features(word)))
    print("Support Vector Machine PWr Tagger      :", svc_pwr.classify(feature_extractor.pos_features(word)))
    print("Logistic Regression PWr Tagger         :", logistic_regression_pwr.classify(feature_extractor.pos_features(word)))
    print("Naive Bayes PWr Tagger                 :", naive_bayes_pwr.classify(feature_extractor.pos_features(word)))
    print("K Neighbors PWr Tagger                 :", k_neighbors_pwr.classify(feature_extractor.pos_features(word)))
    print("Neural Networks PWr Tagger             :", neural_networks_pwr.classify(feature_extractor.pos_features(word))[0])
    print("Decision Tree NC Tagger               :", decision_tree_nc.classify(feature_extractor.pos_features(word)))
    print("Stochastic Gradient Descent NC Tagger :", sgd_nc.classify(feature_extractor.pos_features(word)))
    print("Support Vector Machine NC Tagger      :", svc_nc.classify(feature_extractor.pos_features(word)))
    print("Logistic Regression NC Tagger         :", logistic_regression_nc.classify(feature_extractor.pos_features(word)))
    print("Naive Bayes NC Tagger                 :", naive_bayes_nc.classify(feature_extractor.pos_features(word)))
    print("K Neighbors NC Tagger                 :", k_neighbors_nc.classify(feature_extractor.pos_features(word)))
    print("Neural Networks NC Tagger             :", neural_networks_nc.classify(feature_extractor.pos_features(word))[0])

if __name__ == '__main__':
    main()
