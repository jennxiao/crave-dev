import nltk, spacy, time
from yelpapi import YelpAPI
import secret

en_nlp = spacy.load('en')
nlp = spacy.load('en_core_web_sm')
yelp_api = YelpAPI(secret.yelp_key)

def run_chatbot():
    user_response = input("CRAVEBOT: Hi. I'm Cravebot. <3 What are you craving today? \n")
    food = process_food(user_response).orth_
    user_response = input("CRAVEBOT: Seems like your location settings are off. :( Would you mind giving the city you are located in? \n")
    loc = process_location(user_response).orth_
    response = yelp_api.search_query(term= food, location= loc)
    num_results = 0
    for rest in response["businesses"]:
        num_results+=1
    final_list = []
    print(str(num_results) + " responses")
    for rest in response["businesses"]:
        if not rest['is_closed']:
            loc = "{0}: {1}, {2}, {3}, {4} : {5} m away".format(rest["name"], rest["location"]["address1"], rest["location"]["city"], rest["location"]["state"], rest["location"]["zip_code"],  rest["distance"])
            print(loc)
            final_list.append(loc)
   # time.sleep(2)
    while True: 
        user_response = input("CRAVEBOT: Satisfied with the results? Let me know by saying yes or no. \n")
        if user_response == "yes":
            break
        elif user_response == "no":
            user_response = input("CRAVEBOT: What's wrong? :( \n")
            #fix this
            print("will implement features later")
            break
        else:
            print("Sorry I don't understand.")
    print("Goodbye!")

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

    
if __name__ == '__main__':
    run_chatbot()