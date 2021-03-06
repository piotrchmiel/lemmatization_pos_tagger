from collections import deque
from datetime import timedelta
from os import path
from time import time

from joblib import load, dump

from src.classifiers.gpu_classifier import GPUClassifier
from src.sklearn_wrapper import SklearnWrapper


def feature_generator(feature_extractor, csv_reader):
    last_tag_cache = deque([None, None], maxlen=2)

    for word, tag in zip(csv_reader.extract_feature('word'), csv_reader.extract_feature('tag')):
        yield feature_extractor.pos_features(word, n_1_tag=last_tag_cache[0], n_2_tag=last_tag_cache[1])

        last_tag_cache.appendleft(tag)


def train_target(class_object, feature_extractor, csv_reader):
    clf = SklearnWrapper(class_object)
    train_features = feature_generator(feature_extractor, csv_reader)
    train_labels = [tag for tag in csv_reader.extract_feature('tag')]

    print("Training model", class_object, "...")
    start_time = time()
    clf.train(train_features, train_labels)
    end_time = time()
    elapsed_time = str(timedelta(seconds=end_time - start_time))
    print("Model trained in: ", elapsed_time)

    return clf, elapsed_time


def save_classifier(file_location, classifier):
    if 'gpu' in path.basename(file_location) or 'gpu' in str(classifier):
        classifier._classifier.save_classifier(file_location)
        classifier._classifier = None
        dump(classifier, file_location + '_skl', 9)
    else:
        dump(classifier, file_location, 9)


def load_classifier(file_location):
    if 'gpu' in path.basename(file_location):
        gpu_classifier = GPUClassifier()
        gpu_classifier.load_classifier(file_location)
        skl = load(file_location + '_skl')
        skl._classifier = gpu_classifier
        return skl
    else:
        return load(file_location)
