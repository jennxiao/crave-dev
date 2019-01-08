import nltk 
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#download module for ntlk 
#nltk.download('punkt') # use first-time only 

#read text file
f=open('food.txt','r',errors = 'ignore')
raw=f.read()

raw=raw.lower()# converts text to lowercase

sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

#define helper functions for lemmization
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

# Check for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generating response using TF-IDF approach (finds similarity between user response and words in text file)
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    index = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response = "I'm sorry! I don't understand."
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[index]
        return robo_response


flag=True
print("CRAVEBOT: My name is Cravebot. Would what you like to eat? If you want to leave, type 'bye'!")

while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if user_response != 'bye' and user_response != "bye!":
        if user_response=='thanks' or user_response=='thank you':
            flag=False
            print("CRAVEBOT: You're welcome!")
        else:
            if greeting(user_response) != None:
                print("CRAVEBOT: " + greeting(user_response))
            else:
                print("CRAVEBOT: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("CRAVEBOT: Goodbye!") 