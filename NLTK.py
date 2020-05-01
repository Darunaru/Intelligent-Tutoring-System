"""
#from nltk import *
import nltk
from textblob.classifiers import NaiveBayesClassifier

train_set = ["If we want to accelerate an object, then we must apply a force. Applying a force requires us to do work. After work has been done, energy has been transferred to the object, and the object will be moving with a new constant speed. The energy transferred is known as kinetic energy, and it depends on the mass and speed achieved.",
             "energy above that needed to ionize the molecule is carried away as kinetic energy of the electron ejected",
             "the kinetic energy of an object is the energy that it possesses due to its motion. It is defined as the work needed to accelerate a body of a given mass from rest to its stated velocity"]
#train_set = ['If', 'we', 'want', 'to', 'accelerate', 'an', 'object,', 'then', 'we', 'must', 'apply', 'a', 'force.', 'Applying', 'a', 'force', 'requires', 'us', 'to', 'do', 'work.', 'After', 'work', 'has', 'been', 'done,', 'energy', 'has', 'been', 'transferred', 'to', 'the', 'object,', 'and', 'the', 'object', 'will', 'be', 'moving', 'with', 'a', 'new', 'constant', 'speed.', 'The', 'energy', 'transferred', 'is', 'known', 'as', 'kinetic', 'energy,', 'and', 'it', 'depends', 'on', 'the', 'mass', 'and', 'speed', 'achieved']
devtest_set = ["kinetic is equal to half of product of mass and velocity square"]
#devtest_set = ['kinetic', 'is', 'equal', 'to', 'half', 'of', 'product', 'of', 'mass', 'and', 'velocity', 'square']
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)

"""

from sklearn.feature_extraction.text import TfidfVectorizer
import nltk, string
# import the existing word and sentence tokenizing  
# libraries 
from nltk.tokenize import sent_tokenize, word_tokenize 
  
text = "Natural language processing (NLP) is a field " + \ 
       "of computer science, artificial intelligence " + \ 
       "and computational linguistics concerned with " + \ 
       "the interactions between computers and human " + \ 
       "(natural) languages, and, in particular, " + \ 
       "concerned with programming computers to " + \ 
       "fruitfully process large natural language " + \ 
       "corpora. Challenges in natural language " + \ 
       "processing frequently involve natural " + \ 
       "language understanding, natural language" + \ 
       "generation frequently from formal, machine" + \ 
       "-readable logical forms), connecting language " + \ 
       "and machine perception, managing human-" + \ 
       "computer dialog systems, or some combination " + \ 
       "thereof."
  
print(sent_tokenize(text)) 
print(word_tokenize(text))` #nltk.download('punkt') # if necessary...


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

train_set = ["If we want to accelerate an object, then we must apply a force. Applying a force requires us to do work. After work has been done, energy has been transferred to the object, and the object will be moving with a new constant speed. The energy transferred is known as kinetic energy, and it depends on the mass and speed achieved.",
             "energy above that needed to ionize the molecule is carried away as kinetic energy of the electron ejected",
             "the kinetic energy of an object is the energy that it possesses due to its motion. It is defined as the work needed to accelerate a body of a given mass from rest to its stated velocity"]
#train_set = ['If', 'we', 'want', 'to', 'accelerate', 'an', 'object,', 'then', 'we', 'must', 'apply', 'a', 'force.', 'Applying', 'a', 'force', 'requires', 'us', 'to', 'do', 'work.', 'After', 'work', 'has', 'been', 'done,', 'energy', 'has', 'been', 'transferred', 'to', 'the', 'object,', 'and', 'the', 'object', 'will', 'be', 'moving', 'with', 'a', 'new', 'constant', 'speed.', 'The', 'energy', 'transferred', 'is', 'known', 'as', 'kinetic', 'energy,', 'and', 'it', 'depends', 'on', 'the', 'mass', 'and', 'speed', 'achieved']
devtest_set = ["i am a good boy"]
#devtest_set = ["Kinetic energy is the energy an object possesses due to its motion. An object of mass m moving at velocity v has a kinetic energy equal to mv"]
#print cosine_sim('energy above that needed to ionize the molecule is carried away as kinetic energy of the electron ejected', 'kinetic is equal to half of product of mass and velocity square')
print cosine_sim("If we want to accelerate an object then we must apply a force. Applying a force requires us to do work. After work has been done energy has been transferred to the object and the object will be moving with a new constant speed. The energy transferred is known as kinetic energy and it depends on the mass and speed achievedenergy above that needed to ionize the molecule is carried away as kinetic energy of the electron ejected the kinetic energy of an object is the energy that it possesses due to its motion. It is defined as the work needed to accelerate a body of a given mass from rest to its stated velocity"
,"kinetic enery is a type of energy it comes under physics")
