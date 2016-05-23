from time import time
from collections import deque
from nltk import word_tokenize
from numpy import ndarray

from src.factories.tagger_factory import TaggerFactory
from src.grapher import draw_graph


def measure_time(loaded_taggers, feature_extractor, filenames):
    taggers = [(tagger_name, tagger, deque([None, None], maxlen=2))
               for tagger_name, tagger in loaded_taggers.items()]
    output = []
    for filename in filenames:
        with open(filename, "r") as f:
            text = f.read()
            words = [word for word in word_tokenize(text) if word.isalpha()]
            output.append({})
            element = output[len(output) - 1]
            for tagger_name, tagger, last_run_tag in taggers:
                start_time = time()
                for word in words:
                    tag = tagger.classify(feature_extractor.pos_features(
                        word, n_1_tag=last_run_tag[0], n_2_tag=last_run_tag[1]))
                    if isinstance(tag, ndarray):  # neural network output is nd-array
                        tag = tag[0]
                    last_run_tag.appendleft(tag)
                end_time = time()
                elapsed_time = end_time - start_time
                element[tagger_name] = elapsed_time
                print("{}, tagger: {}, time: {:.6f} secs".format(filename, tagger_name, elapsed_time))
    return output

        
def main():
    factory = TaggerFactory()
    pwr_taggers = factory.load_pwr_taggers()
    nc_taggers = factory.load_nc_taggers()
    feature_extractor = factory.get_feature_extractor()

    filenames = ["010_words.txt", "020_words.txt", "030_words.txt", "040_words.txt", "050_words.txt", "060_words.txt", "070_words.txt", "080_words.txt", "090_words.txt", "100_words.txt"]
    
    print("PWr taggers:")
    pwr_results = measure_time(pwr_taggers, feature_extractor, filenames)
    print("NC taggers:")
    nc_results = measure_time(nc_taggers, feature_extractor, filenames)
    
    draw_graph(pwr_results, "PWr tagger", 1)
    draw_graph(nc_results, "NC tagger", 2)

if __name__ == '__main__':
    main()
