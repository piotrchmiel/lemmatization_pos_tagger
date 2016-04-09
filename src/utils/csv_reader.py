from csv import DictWriter, DictReader

from src.settings import NATIONAL_CORPUS_CSV, PWR_CORPUS_CSV, NATIONAL_CORPUS_DIR, PWR_CORPUS_DIR
from src.utils.xml_reader import XmlReader


class CsvReader(object):
    def __init__(self, use_national_corpus=False):
        self.use_national_corpus = use_national_corpus
        self.csv_file_path = NATIONAL_CORPUS_CSV if self.use_national_corpus else PWR_CORPUS_CSV
        self.corpus_dir = NATIONAL_CORPUS_DIR if self.use_national_corpus else PWR_CORPUS_DIR

    def convert_xml_to_csv(self):
        print("Starting conversion of files from .xml to .csv format. "
              "Please have a coffee break while I do my job.")

        with open(self.csv_file_path, "w", newline="", encoding="utf8") as csv_file:
            reader = XmlReader(self.corpus_dir, use_national_corpus=self.use_national_corpus)
            fieldnames = ['word', 'tag']
            writer = DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for word, tag in reader.extract_words_and_tags():
                writer.writerow({'word': word, 'tag': tag})

            print("All done. I appreciate your patience.")

    def extract_feature(self, feature_name):
        with open(self.csv_file_path, "r", newline="", encoding="utf8") as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                yield row[feature_name]
