import unittest

from Dictionary import read_dict, process_cedict_line
from InputParsing import drop_punctuation_and_numbers, split_into_sentences, words_in_text
from KnownWords import scan_new_words

__author__ = 'Lucas Kjaero'


class DictionaryTest(unittest.TestCase):
    def test_process_cedict_line(self):
        bad_line = "# CC-CEDICT"
        with self.assertRaises(AssertionError):
            process_cedict_line(bad_line)

        blank_line = ""
        with self.assertRaises(AssertionError):
            process_cedict_line(blank_line)

        good_line = "一切 一切 [yi1 qie4] /everything/every/all/"
        key, good_result = process_cedict_line(good_line)
        self.assertEqual(key, "一切")
        self.assertEqual(good_result.traditional, "一切")
        self.assertEqual(good_result.simplified, "一切")
        self.assertEqual(good_result.pinyin, "yi1 qie4")
        self.assertEqual(good_result.meaning, "everything/every/all")

    def test_read_dict(self):
        test_dict = read_dict()

        # Make sure every line has been processed (assumes CEDICT)
        lines_processed = sum([test_dict[x][0] for x in test_dict])
        self.assertEqual(lines_processed, 104198)

        # Make sure entries have the right shape
        for key in test_dict:
            entry = test_dict[key]
            length = entry[0]
            self.assertEqual(len(entry), length + 1)


class InputParsingTest(unittest.TestCase):
    """Tests functions in InputParsing
    Note that segment_sentence is not tested because it calls external code, rather than doing things by itself."""
    def test_drop_punctuation_and_numbers(self):
        test_punctuation = "。"
        test_number = "42.2453"
        test_words = ["乘法", "九月"]

        with self.assertRaises(StopIteration):
            next(drop_punctuation_and_numbers(test_punctuation))

        with self.assertRaises(StopIteration):
            next(drop_punctuation_and_numbers(test_number))

        good_list = list(drop_punctuation_and_numbers(test_words))
        self.assertEqual(good_list[0], "乘法")
        self.assertEqual(good_list[1], "九月")
        self.assertEqual(len(good_list), 2)

    def test_split_into_sentences(self):
        empty_input = ""
        sample_input = """你叫什麼名字？我叫路卡斯。我高興認識你！"""

        empty_lines = split_into_sentences(empty_input)
        self.assertEqual(len(empty_lines), 0)

        test_sentences = split_into_sentences(sample_input)
        self.assertEqual(len(test_sentences), 3)
        self.assertEqual(test_sentences[0], "你叫什麼名字？")
        self.assertEqual(test_sentences[1], "我叫路卡斯。")
        self.assertEqual(test_sentences[2], "我高興認識你！")

    def test_words_in_text(self):
        sample_input = """你叫什麼名字？我叫鄧小平。我高興認識你！"""
        words = words_in_text(sample_input)

        # Use in because order is not guaranteed
        self.assertEqual(len(words), 8)
        self.assertTrue('你' in words)
        self.assertTrue('叫' in words)
        self.assertTrue('什麼' in words)
        self.assertTrue('名字' in words)
        self.assertTrue('我' in words)
        self.assertTrue('鄧小平' in words)
        self.assertTrue('高興' in words)
        self.assertTrue('認識' in words)


class KnownWordsTest(unittest.TestCase):
    def test_scan_new_words(self):
        sample_input = """你叫什麼名字？我叫鄧小平。我高興認識你！"""
        known_words = {'你', '我'}
        new_words = scan_new_words(sample_input, known_words=known_words)

        self.assertEqual(len(new_words), 6)
        self.assertTrue('叫' in new_words)
        self.assertTrue('什麼' in new_words)
        self.assertTrue('名字' in new_words)
        self.assertTrue('鄧小平' in new_words)
        self.assertTrue('高興' in new_words)
        self.assertTrue('認識' in new_words)
