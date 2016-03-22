from csv import DictWriter, DictReader
from os import path

from src.settings import NATIONAL_CORPUS_CSV, CORPUS_CSV
from src.utils.xml import XmlReader


class CsvReader(object):
    def __init__(self, national_corpus=False):
        self.national_corpus = national_corpus
        self.csv_file_path = NATIONAL_CORPUS_CSV if self.national_corpus else CORPUS_CSV

    def convert_xml_to_csv(self, dir_name):
        if path.exists(dir_name):
            print("Starting conversion of files from .xml to .csv format. "
                  "Please have a coffee break while I do my job.")

            with open(self.csv_file_path, "w", newline="") as csv_file:
                fieldnames = ['word', 'tag']
                writer = DictWriter(csv_file, fieldnames=fieldnames)
                reader = XmlReader(dir_name, national_corpus=self.national_corpus)
                writer.writeheader()
                for word, tag in reader.extract_words_and_tags():
                    writer.writerow({'word': word, 'tag': tag})

            print("All done. I appreciate your patience.")
        else:
            print("I am just a very simple algorithm and I have not found a Corpus directory. "
                  "Provide the proper one.")

    def extract_feature(self, feature_name):
        with open(self.csv_file_path, "r", newline="") as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                yield row[feature_name]
