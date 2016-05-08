from os import path

BASE_DIR = path.dirname(path.dirname(__file__))
SUFFIX_FILE = path.join(BASE_DIR, 'Suffixes', 'suffixes.pickle')
CLASSIFIERS_DIR = path.join(BASE_DIR, 'Classifiers')
SUFFIX_DIR = path.join(BASE_DIR, 'Suffixes')
OUTPUT_CSV = path.join(BASE_DIR, 'OutputCsv')
PWR_CORPUS_DIR = path.join(BASE_DIR, 'CorpusPWr')
PWR_CORPUS_CSV = path.join(OUTPUT_CSV, 'CorpusPWr.csv')
NATIONAL_CORPUS_DIR = path.join(BASE_DIR, 'NationalCorpus')
NATIONAL_CORPUS_CSV = path.join(OUTPUT_CSV, 'NationalCorpus.csv')
OUTPUT_XML_DIR = path.join(BASE_DIR, "OutputXml")
TAGGER_FILENAMES = ('tagger_decision_tree', 'sgd', 'svm', 'logistic_regression',
                    'naive_bayes', 'kneighbors', 'neural_network', 'gpu_classifier')
SUFFIX_TAGGER = "suffix_tagger.pickle"

N_ONE_LETTER = 15
N_OTHER_LETTERS = 35

NN_UNITS = 100
NN_LEARNING_RATE = 0.02
NN_ITERATIONS = 10
