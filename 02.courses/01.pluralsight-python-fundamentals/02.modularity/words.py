#!/user/bin/env python3

"""Retrieve and print words from a url

    Usage:

        python3 words.py <URL>

    Comments:

        Code from Pluralsight Python Fundamentals course
"""

from urllib.request import urlopen
import sys


def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        url: The URL of a UTF-8 document

    Returns:
        A list of string containing the words from the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            # urlopen returns bytes (b'string') and not unicode string
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print a list of items

    Args:
        items: the list of items
    """
    for word in items:
        print(word)


def main(url):
    """main function when running the script

    Args:
        url: The URL of a UTF-8 document

    """
    print_items(fetch_words(url))


# When executing the script:
if __name__ == "__main__":
    if len(sys.argv) == 1:
        main("https://github.com/wmalgoire/learning.python")
    else:
        main(sys.argv[1])
