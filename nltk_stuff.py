from __future__ import division
import nltk
from nltk.corpus import stopwords
from nltk.corpus import toolbox
from nltk.corpus import wordnet as wn

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)


def generate_model(cfdist,word, num=15):
	for i in range(num):
		print word,
		word =cfdist[word].max()

def lexical_diversity(my_text_data):
	word_count = len(my_text_data)
	vocab_size = len(set(my_text_data))
	diversity_score = word_count / vocab_size

#what if we take out unusual words from analysis
def unusual_words(text):
	text_vocab = set(w.lower() for w in text if w.isalpha())
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab.difference(english_vocab)
	return sorted(unusual)

def content_fraction(text):
	stopwords = nltk.corpus.stopwords.words('english')
	content = [w for w in text if w.lower() not in stopwords]
	return len(content)/len(text)



generate_model(cfd,"and")
print 'END'
generate_model(cfd,"thou")
print 'END'
generate_model(cfd,"God")




#Synset stuff from wordnet
wn.synsets('motorcar') #this outputs to synset name, in this case 'car.n.01'
wn.synset('car.n.01').lemma_names 	#I can use this to find lemmatizations and groups of words, and then see which word performed better
wn.synset('car.n.01').definition
wn.synset('car.n.01').examples

for synset in wn.synsets('car')

motorcar = wn.synset('car.n.01')

types_of_motorcar = motorcar.hyponyms()

#this is to get each hyponym in for car
sorted([lemma.name for synset in types_of_motorcar for lemma in synset.lemmas])

motorcar.hypernyms()

paths = motorcar.hypernym_paths()

motorcar.root_hypernyms()

wn.synset('tree.n.01').part_meronyms #components of an item
wn.synset('tree.n.01').substance_meronyms()
wn.synset('tree.n.01').member_holonyms() #things the components are contained in

for synset in wn.synsets('mint',wn.NOUN):
	print synset.name + ':', synset.definition

wn.synset('walk.v.01').entailments()

#dir lets you see all lexical relationships
dir(wn.synset('harmony.n.02'))


#grouping words (from the book): If two synsets share a very specific hypernym = one that is low down in the hyperntm hierarchy- they must be closely related
right = wn.synset('right_whale.n.01')