import nltk
import os
import unidecode
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

REFLEXIVES = ['myself', 'yourself', 'yourselves', 'himself', 'herself', 'oneself', 'itself', 'ourselves', 'ourself', 'themselves']

def normalise_file(file_name):
    text = open(file_name, 'r').read()
    text = unidecode.unidecode(text)
    fdist = FreqDist(word.lower() for word in word_tokenize(text))
    common = [i for i, v in fdist.items() if v > 1]
    mapping = nltk.defaultdict(lambda: '<unk>')
    for v in common:
        mapping[v] = v
    normalised_words = [mapping[word] for word in word_tokenize(text)]
    normalised_text = ' '.join(normalised_words)
    open(file_name.replace('.txt', '.normalised.txt') , 'w').write(normalised_text)
normalise_file('reflexive.train.txt')
normalise_file('reflexive.test.txt')
normalise_file('reflexive.valid.txt')
normalise_file('non_reflexive.train.txt')
normalise_file('non_reflexive.test.txt')
normalise_file('non_reflexive.valid.txt')

