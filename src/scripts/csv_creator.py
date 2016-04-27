import argparse

from src.utils.csv_reader import CsvReader


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--use_pwr', action='store_true', help="Use pwr corpus")
    group.add_argument('--use_national', action='store_true', help="Use national corpus")
    parser.add_argument('--extract_base_words', action='store_true', help="Save words with their base form")
    args = parser.parse_args()

    print("Start CSV extracting...")
    reader = CsvReader(use_national_corpus=args.use_national, extract_base_words=args.extract_base_words)
    try:
        reader.convert_xml_to_csv()
    except FileNotFoundError as E:
        print(E)
    else:
        print("Done.")


if __name__ == '__main__':
    main()
