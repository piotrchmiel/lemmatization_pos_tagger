from os import path

BASE_DIR = path.dirname(path.dirname(__file__))
SUFFIX_FILE = path.join(BASE_DIR, 'Suffixes', 'suffixes.pickle')
CLASSIFIERS_DIR = path.join(BASE_DIR, 'Classifiers')
SUFFIX_DIR = path.join(BASE_DIR, 'Suffixes')
CORPUS_DIR = path.join(BASE_DIR, 'CorpusPWr')
CORPUS_CSV = path.join(CORPUS_DIR, 'extracted.csv')
NATIONAL_CORPUS_DIR = path.join(BASE_DIR, 'NationalCorpus')
NATIONAL_CORPUS_CSV = path.join(NATIONAL_CORPUS_DIR, 'extracted.csv')

SUFFIX_TAGGER = "suffix_tagger.pickle"
N_ONE_LETTER = 15
N_TWO_LETTERS = 35
N_THREE_LETTERS = 35
N_FOUR_LETTERS = 35
