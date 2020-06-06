import os
import pandas as pd
from model.model import data
import matplotlib.pyplot as plt
import random
from analyze.words_by_categories import REFLEXIVES, PRONOMINALS

corpus = data.Corpus("data/reflexives")
def word2_is_high_when_word1_is_high(word1, word2, threshold):
    df = pd.read_csv(os.path.join("0.1", word1+"_probs.csv")).drop('word', axis=1)
    word2_idx = corpus.dictionary.word2idx[word2]
    word2_row = df.loc[word2_idx]
    num_high = len(word2_row[word2_row > threshold])

    labels = [word2+' high', word2+' low']
    sizes = [num_high, len(df.columns) - num_high]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title(word2 + " in " + word1)
    #plt.title("Fraction of times " + word2 + "'s probabilty is high when " + word1 + "'s probability is high")
    plt.show()


for word1 in PRONOMINALS:
    for word2 in REFLEXIVES:
        try:
            word2_is_high_when_word1_is_high(word1, word2, 0.1)
        except FileNotFoundError:
            continue

rand_indices = [random.randint(0, len(corpus.dictionary.idx2word)) for i in range(10)]
for word1 in PRONOMINALS:
    for word2_idx in rand_indices:
        word2 = corpus.dictionary.idx2word[word2_idx]
        word2_is_high_when_word1_is_high(word1, word2, 0.1)