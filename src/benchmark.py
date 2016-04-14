from itertools import chain

from joblib import Parallel, delayed

from src.factories.tagger_factory import TaggerFactory
from src.settings import TAGGER_FILENAMES


def benchmark_result(factory, feature_extractor, filename, is_test_corpus_national, number_of_test_records):
    tagger = factory.load_pwr_tagger(filename) if is_test_corpus_national else factory.load_national_tagger(filename)
    name = filename + '_pwr' if is_test_corpus_national else filename + '_nc'
    return "{0:25} : {1:.3f}".format(name, tagger.accuracy(is_test_corpus_national,
                                                           number_of_test_records, feature_extractor))


def main():
    factory = TaggerFactory()
    feature_extractor = factory.get_feature_extractor()

    print("*** Benchmark Start ***")

    result = Parallel(n_jobs=-1)(chain((delayed(benchmark_result)(factory, feature_extractor, filename, True, 100)
                                        for filename in TAGGER_FILENAMES),
                                       (delayed(benchmark_result)(factory, feature_extractor, filename, False, 100)
                                        for filename in TAGGER_FILENAMES)))

    print("\n".join(sorted(result)))


if __name__ == '__main__':
    main()
