import unittest

from Dictionary import read_dict, process_cedict_line

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