import spacy
from nltk import Tree
from spacy import displacy


en_nlp = spacy.load('en')

struct_1 = en_nlp("Spaghetti and meatballs please.")
struct_2 = en_nlp("I would like spaghetti and meatballs.")


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


[to_nltk_tree(sent.root).pretty_print() for sent in struct_1.sents]
print()
[to_nltk_tree(sent.root).pretty_print() for sent in struct_2.sents]