import argparse
import os

from src.settings import CORPUS_DIR
from src.utils import CsvReader


def detect_national_corpus(path):
    _, subdirectories, _ = next(os.walk(path))
    return 'ann_morphosyntax.xml' in os.listdir(os.path.join(path, subdirectories[0]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--corpus", dest="corpus", help="path to corpus directory", default="../CorpusPWr")
    args = parser.parse_args()
    if os.path.exists(args.corpus):
        print("Start CSV extracting...")
        reader = CsvReader(args.corpus, national_corpus=detect_national_corpus(args.corpus))
        reader.convert_xml_to_csv()

        print("Done.")
    else:
        print("Please provide valid directory!")

if __name__ == '__main__':
    main()

