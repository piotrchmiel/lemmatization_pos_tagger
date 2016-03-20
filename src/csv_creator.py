from src.utils import CsvReader
from src.settings import CORPUS_DIR


def main():
    print("Start CSV extracting...")
    reader = CsvReader('../NationalCorpus', True)
    reader.convert_xml_to_csv()
    print("Done.")

if __name__ == '__main__':
    main()