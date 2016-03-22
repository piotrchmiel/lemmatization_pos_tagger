from pickle import load


class SuffixUnpacker(object):
    def __init__(self, name_of_pickle_file):
        with open(name_of_pickle_file, "rb") as file_handler:
            self.suffixes = load(file_handler)

    def extract_n_best_one_letter(self, n):
        return self.suffixes[0].most_common(n)

    def extract_n_best_two_letters(self, n):
        return self.suffixes[1].most_common(n)

    def extract_n_best_three_letters(self, n):
        return self.suffixes[2].most_common(n)

    def extract_n_best_four_letters(self, n):
        return self.suffixes[3].most_common(n)
