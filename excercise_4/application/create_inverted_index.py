#encoding=utf-8

from excercise_4.data import data_manager
from excercise_4.domain.inverted_index import InvertedIndex

def start(default=True, **recipes_dic):
    print "*** Start creating an inverted index ***"

    if default:
        index = InvertedIndex()

    print "1) Creating inverted index :: add recipes to the inverted index"
    for link, recipe in recipes_dic.iteritems():
        res = index.add_recipe(recipe)
        if res == -1:
            print "error occurred"
            return -1

    print "2) Creating inverted index :: store the inverted index on disk"
    data_manager.save_inverted_index(index)