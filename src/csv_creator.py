from src.settings import CORPUS_DIR
from src.utils import CsvReader


def main():
    print("Start CSV extracting...")
    reader = CsvReader(CORPUS_DIR)
    reader.convert_xml_to_csv()

    print("Done.")

if __name__ == '__main__':
    main()