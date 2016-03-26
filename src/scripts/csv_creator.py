import argparse

from src.utils.csv_reader import CsvReader


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--use_pwr', action='store_true', help="Use pwr corpus")
    group.add_argument('--use_national', action='store_true', help="Use national corpus")
    args = parser.parse_args()

    print("Start CSV extracting...")
    reader = CsvReader(use_national_corpus=args.use_national)
    try:
        reader.convert_xml_to_csv()
    except FileNotFoundError as E:
        print(E)

    print("Done.")


if __name__ == '__main__':
    main()
