import time, datetime, logging
from joblib import load, dump

from src.sklearn_wrapper import SklearnWrapper


def train_target(class_object, feature_extractor, csv_reader):

    logging.basicConfig(filename='train_target.log',level=logging.INFO)

    clf = SklearnWrapper(class_object)
    train_features = (feature_extractor.pos_features(word) for word in csv_reader.extract_feature('word'))
    train_labels = [tag for tag in csv_reader.extract_feature('tag')]

    print("Training model", class_object, "...")
    start_time = time.time()
    clf.train(train_features, train_labels)
    end_time = time.time()
    elapsed_time = str(datetime.timedelta(seconds=end_time-start_time))
    print("Done in", elapsed_time)
    logging.info('Trained model' + str(class_object) + '\nTraining time:' + elapsed_time)

    return clf


def save_classifier(file_location, classifier):
    dump(classifier, file_location, 9)

def load_classifier(file_location):
    return load(file_location)
