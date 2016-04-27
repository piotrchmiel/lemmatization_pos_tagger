from csv import DictWriter, DictReader
from os.path import splitext

from src.settings import NATIONAL_CORPUS_CSV, PWR_CORPUS_CSV, NATIONAL_CORPUS_DIR, PWR_CORPUS_DIR
from src.utils.xml_reader import XmlReader


class CsvReader(object):
    def __init__(self, use_national_corpus=False, extract_base_words=False):
        self.use_national_corpus = use_national_corpus
        self.extract_base_words = extract_base_words
        self.csv_file_path = NATIONAL_CORPUS_CSV if self.use_national_corpus else PWR_CORPUS_CSV
        self.corpus_dir = NATIONAL_CORPUS_DIR if self.use_national_corpus else PWR_CORPUS_DIR

        if self.extract_base_words:
            filename, extension = splitext(self.csv_file_path)
            self.csv_file_path = filename + '_base' + extension

    def convert_xml_to_csv(self):
        print("Starting conversion of files from .xml to .csv format. "
              "Please have a coffee break while I do my job.")

        with open(self.csv_file_path, "w", newline="", encoding="utf8") as csv_file:
            reader = XmlReader(self.corpus_dir, use_national_corpus=self.use_national_corpus)
            fieldnames = ['word', 'tag' if not self.extract_base_words else 'base']
            writer = DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for word, tag, base in reader.extract_words_and_tags():
                if not self.extract_base_words:
                    writer.writerow({'word': word, 'tag': tag})
                else:
                    if word.lower() != base.lower():
                        writer.writerow({'word': word, 'base': base})

            print("All done. I appreciate your patience.")

    def extract_feature(self, feature_name):
        with open(self.csv_file_path, "r", newline="", encoding="utf8") as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                yield row[feature_name]
