""" Utility functions used by the application. Involves a lot of loading of
json data.

September 2, 2016
"""

import json

def load_json(filename):
    """ Loads in a json file """
    with open(filename, 'r') as f:
        results = json.load(f)
    return results

def create_error(message):
    """ Returns a dict containing an error message. """
    return {"error" : message}

def load_dictionary(sids):
    dictionary = TrieDict()
    for sid in sids:
        dictionary.add(sid)
    return dictionary


class TrieDict(object):

    def __init__(self, char, word):
        self.children = {}
        self.char = char
        self.word = word

    def add(word):
        """ Adds WORD to the trie. """
        def add_helper(word, index):
            if index != len(word) - 1:
                curr = TrieDict(word[index], None)
                curr.children[word[index + 1]] = add_helper(word, index + 1)
                return curr
            return TrieDict(word[index], word)
        return add_helper(word, 0)

    def complete(phrase):
        """ Finds WORD in the trie and returns a list of completed phrases. """
        pass
