import pandas as pd
from analyze.words_by_categories import REFLEXIVES, PRONOMINALS, GENITIVES, NOMINAMLS
from analyze import sentences


def produce_describe(sentence):
    sorted_df = pd.read_csv("next_word_probs_reflexives/sorted/" + sentence.replace(" ", "_") + "_sorted.csv")
    # top_100 = sorted_df.head(100)
    # print(top_100)
    # reflexives = top_100[top_100['word'].isin(REFLEXIVES + PRONOUNS)]
    interesting_words = sorted_df[sorted_df['word'].isin(REFLEXIVES + PRONOMINALS + NOMINAMLS + GENITIVES)]
    print(sentence)
    interesting_words.to_csv("inter/ " + sentence)
    print(interesting_words)


#for sent in sentences.physcicist_like_him:

    #produce_describe("the man said to the woman that physicists like")
   # produce_describe("the man said about the woman that physicists like")

#produce_describe("the woman said to the man that physicists like")
#produce_describe("the woman said about the man that physicists like")
for sent in sentences.smarter_new:
    produce_describe(sent)