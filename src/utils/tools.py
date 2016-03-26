from pickle import load, dump

from src.sklearn_wrapper import SklearnWrapper
from src.utils.csv_reader import CsvReader


def train_target(class_object, feature_extractor, is_train_corpus_national):

    clf = SklearnWrapper(class_object)
    reader = CsvReader(use_national_corpus=is_train_corpus_national)

    train_features = (feature_extractor.pos_features(word) for word in reader.extract_feature('word'))
    train_labels = [tag for tag in reader.extract_feature('tag')]

    print("Training model", class_object, "...")
    clf.train(train_features, train_labels)
    print("Done.")

    return clf


def save_classifier(file_location, classifier):
    with open(file_location, 'wb') as file_handler:
        dump(classifier, file_handler)


def load_classifier(file_location):
    with open(file_location, 'rb') as file_handler:
        classifier = load(file_handler)
    return classifier
