import re
from collections import namedtuple

__author__ = 'Lucas Kjaero'

# Used in the process_cedict_line function. Do not change. Out here to avoid recompilation each call.
cedict_definition_pattern = re.compile("/(.*)/")
cedict_pinyin_pattern = re.compile("\[(.*)\] /")

DictionaryEntry = namedtuple("DictionaryEntry", ['traditional', 'simplified', 'pinyin', 'meaning'])


def process_cedict_line(line):
    """Process a line in cedict.
    Returns (traditional, simplified, pinyin, meaning)
    Throws an AssertionError if a line doesn't contain a definition.
    If moving, don't forget to move regular expression patterns too."""
    assert len(line) is not 0
    assert line[0] is not "#"

    split_line = line.split(" ")
    traditional_val, simplified_val = split_line[0], split_line[1]

    pinyin_val = cedict_pinyin_pattern.findall(line)[0]
    meaning_val = cedict_definition_pattern.findall(line)[0]

    entry = DictionaryEntry(traditional=traditional_val, simplified=simplified_val, pinyin=pinyin_val,
                            meaning=meaning_val)
    return traditional_val, entry


def read_dict(filename="cedict_ts.u8", line_parser=process_cedict_line):
    """Processes a dictionary file into a dictionary of entries. Assumes one line per entry.
    Default definitions come from cedict
    Uses the provided line_parser function to parse each individual dictionary.
    Ignores any lines that raise an AssertionError.
    The format is:
    {
    word: (number_of_entries, entry_1, entry_2, ...),
     ...
     }"""

    working_dictionary = dict()

    with open(filename) as chinese_dictionary:
        for line in chinese_dictionary:
            try:
                key, entry = line_parser(line)

                try:
                    old_entry = working_dictionary[key]

                    num_entries = old_entry[0]
                    working_dictionary[key] = (num_entries + 1,) + old_entry[1:] + (entry,)

                except KeyError:
                    working_dictionary[key] = (1, entry)

            except AssertionError:
                pass

    return working_dictionary
