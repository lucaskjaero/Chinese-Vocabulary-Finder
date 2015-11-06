import re

# Chinese word segmentation
import jieba

__author__ = 'Lucas Kjaero'

# Optimize Chinese segmenter for running in parallel.
try:
    from multiprocessing import cpu_count
    jieba.enable_parallel(cpu_count())
except NotImplementedError:
    pass

number_pattern = re.compile("[0-9]+(.)*[0-9]*")


def drop_punctuation_and_numbers(iterable_text):
    """A generator that returns tokens in a text if they are not punctuation or numbers. Input must be iterable"""
    for token in iterable_text:
        if token not in ",.?;'[]()`~!@#$%^&*/+_-=<>{}:，。？！·；：‘“、\"" and number_pattern.match(token) is None:
            yield token


def segment_sentence(input_text, split_compounds=False):
    """Segment a Chinese sentence, returns a generator containing the words.
    If you select split_compounds, it will return all possible words in the sentence, including overlaps."""
    return drop_punctuation_and_numbers(jieba.cut(input_text, cut_all=split_compounds))


def split_into_sentences(input_text):
    """Split a text into sentences, returns a list of strings."""
    new_lined_text = input_text.replace(".", ".\n").replace("?", "?\n").replace("!", "!\n")\
        .replace("。", "。\n").replace("？", "？\n").replace("！", "！\n")
    return new_lined_text.splitlines()


def words_in_text(input_text):
    """Returns a set of words in a given string."""
    word_list = []
    for sentence in split_into_sentences(input_text):
        word_list.extend(segment_sentence(sentence))
    return set(word_list)
