from collections import Counter

import en_core_web_sm
nlp = en_core_web_sm.load()

import nltk

from pprint import pprint

doc = nlp("I'm looking for ice cream. Classy restaurant. In Berkeley, CA.")

pprint([(X.text, X.label_) for X in doc.ents])


pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])