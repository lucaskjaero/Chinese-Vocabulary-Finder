from InputParsing import words_in_text

__author__ = 'Lucas Kjaero'


def get_known_words():
    """Returns a set of known words."""
    known_words = []
    try:
        words = open("known_words.txt", 'r')
        for line in words:
            known_words.append(line.strip("\n"))
    finally:
        return set(known_words)


def save_new_words(new_words):
    """Saves the list of known words to file."""
    words = open("known_words.txt", 'a')
    try:
        for word in new_words:
            words.write(word + "\n")
    finally:
        words.close()


def scan_new_words(input_text, known_words=get_known_words()):
    """Scans an input text and returns a set of new words.
    Defaults to reading from known_words.txt, but can take a set"""
    return set(word for word in words_in_text(input_text) if word not in known_words)
