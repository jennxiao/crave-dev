import nltk, spacy, time
from yelpapi import YelpAPI

en_nlp = spacy.load('en')
nlp = spacy.load('en_core_web_sm')
yelp_api = YelpAPI("Hp8pY32pxeXSNL8oAaQIRHT2cKs4A711Jn-5cJof-rSE1SicUkneft1NKY_gdHk8mJoCMVY7iZARi13lqYCgpz65MXqYwN6vBqYpAnBovBbxN45Vf-u0MNdjgMAvXHYx")

def run_chatbot():
    user_response = input("CRAVEBOT: Hi. I'm Cravebot. <3 What are you craving today? \n")
    food = process_food(user_response).orth_
    user_response = input("CRAVEBOT: Seems like your location settings are off. :( Would you mind giving the city you are located in? \n")
    loc = process_location(user_response).orth_
    response = yelp_api.search_query(term= food, location= loc)
    num_results = 0
    for rest in response["businesses"]:
        num_results+=1
    #print("Processing request")
    #time.sleep(2)
    print(str(num_results) + " responses")
    for rest in response["businesses"]:
        if not rest['is_closed']:
            print("{0}: {1}, {2}, {3}, {4} : {5} m away".format(rest["name"], rest["location"]["address1"], rest["location"]["city"], rest["location"]["state"], rest["location"]["zip_code"],  rest["distance"]))
    time.sleep(2)
 


"""
def process_food(user_response):
    for res in user_response:
        doc = nlp(res)
        relations = extract_object_relations(doc)
        for r1, r2 in relations:
            print('{:<10}\t{}\t{}'.format(r1.text, r2.ent_type_, r2.text))
"""
def process_food(user_response):
    doc = en_nlp(user_response)
    sentence = next(doc.sents)
    for word in sentence:
        if word.dep_ == 'dobj':
           return word

def process_location(user_response):
    doc = en_nlp(user_response)
    sentence = next(doc.sents)
    for word in sentence:
        return word

"""
def process_location(user_response):
     for res in user_response:
        doc = nlp(res)
        relations = extract_location_relations(doc)
        print("finished relations")
        print(relations)
        for r1, r2 in relations:
            print('{:<10}\t{}\t{}'.format(r1.text, r2.ent_type_, r2.text))

"""
"""
def extract_object_relations(doc):
    spans = list(doc.ents) + list(doc.noun_chunks)
    for span in spans:
        span.merge()

    relations = []
    for product in filter(lambda w: w.ent_type_ == 'PRODUCT', doc):
        if prduct.dep_ in ('attr', 'dobj'):
            subject = [w for w in product.head.lefts if w.dep_ == 'nsubj']
            if subject:
                subject = subject[0]
                relations.append((subject, product))
        elif product.dep_ == 'pobj' and product.head.dep_ == 'prep':
            relations.append((product.head.head, product))
    return relations
"""

def extract_location_relations(doc):
    spans = list(doc.ents) + list(doc.noun_chunks)
    for span in spans:
        span.merge()

    relations = []
    for product in filter(lambda w: w.ent_type_ == 'GPE', doc):
        if prduct.dep_ in ('attr', 'dobj'):
            subject = [w for w in product.head.lefts if w.dep_ == 'nsubj']
            if subject:
                subject = subject[0]
                relations.append((subject, product))
        elif product.dep_ == 'pobj' and product.head.dep_ == 'prep':
            relations.append((product.head.head, product))
    return relations


    
if __name__ == '__main__':
    run_chatbot()