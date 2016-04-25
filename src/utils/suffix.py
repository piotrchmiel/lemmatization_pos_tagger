from pickle import load


class SuffixUnpacker(object):
    def __init__(self, name_of_pickle_file):
        with open(name_of_pickle_file, "rb") as file_handler:
            self.suffixes = load(file_handler)

    def get_number_of_suffixes(self):
        return len(self.suffixes)

    def extract_n_best_k_letters(self, k, n):
        if k - 1 > len(self.suffixes):
            return {}
        return self.suffixes[k - 1].most_common(n)
