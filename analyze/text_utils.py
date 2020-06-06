
import os
from collections import Counter
import pandas as pd
from analyze.words_by_categories import REFLEXIVES



# Return a Counter object with the number of occurences of each word from vocab in file
# note: to make life easier for me, the vocabulary is based on the words
# in vocab and *not* on the generated file (so words that did not appear in the generated file will get a 0 count)
# parmas: file_to_process - file path to get counts for, vocab- list of words to get counts for
def get_counts_from_file(file_name, vocab):
    file = open(file_name, "r")
    counts = Counter(file.read().split())
    for word in vocab:
        if word not in counts.keys():
            counts[word] = 0
    file.close()
    return counts


# Return a pandas dataFrame with word counts for each word, sorted by the indices of the corpus, and save it to an excel file
def word_counts(file_to_process, idx2word, word2idx, output_name=None):
    # if not word2idx:
    #     word2idx = {word: i for i, word in enumerate(idx2word)}

    if not output_name or output_name == "":
        outdir = "word_counts"
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        output_name = os.path.join(outdir, os.path.splitext(file_to_process.split('/')[-1].split('\\')[-1])[
            0] + "_word_counts" + ".xlsx")

    counts = get_counts_from_file(file_to_process, idx2word)
    counts_df = pd.DataFrame.from_dict(counts, orient='index').reset_index()
    counts_df = counts_df.rename(columns={'index': 'word', 0: 'count'})
    counts_df['word2idx'] = counts_df['word'].map(word2idx)
    counts_df.sort_values(['word2idx'], inplace=True)
    counts_df.to_excel(output_name)
    return counts_df


# Return a pandas dataFrame with word counts for each word in idx2word in the train, valid, test and the generated files,
# and save it to an excel file
def word_counts_in_all_files(data_path, idx2word, word2idx, output_name=None, generated_dir=None):
    if not output_name or output_name == "":
        outdir = "word_counts"
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        output_name = os.path.join(outdir, "all_counts" + ".xlsx")

    if not generated_dir or generated_dir == "":
        generated_dir = "generated"
        if not os.path.exists(generated_dir):
            os.mkdir(generated_dir)

    files = [os.path.join(data_path, file) for file in ["train.txt", "valid.txt", "test.txt"]]
    files += [os.path.join(generated_dir, generated) for generated in os.listdir(generated_dir)]
    dfs = [word_counts(file, idx2word, word2idx) for file in files]

    # copy to a new data frame the count colomn of each file
    result = pd.DataFrame()
    result['word'] = dfs[0]['word']
    result['word2idx'] = dfs[0]['word2idx']
    for i, file in enumerate(files):
        result[file] = dfs[i]['count'].to_numpy()
    result.to_excel(output_name)

    return result


# Return a df with counts only for the tokens in words, and save it to an excel file
# params: all_words_count - df with counts for every word. words - list of strings
def specific_words_count(all_words_count, words, output_name=None):
    if not output_name or output_name == "":
        outdir = "word_counts"
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        output_name = os.path.join(outdir, "specific_counts" + ".xlsx")

    filtered = all_words_count[all_words_count.word.isin(words)]
    filtered.to_excel(output_name)
    return filtered


# Produces a txt file contatinig every senetence in the file that contains one of the words in the parameter words
# file-string with path to the file to proccess, words- list of strings, outf_name-string with the desired output path
def sentences_with_specific_words(file, words, outf_name):
    with open(outf_name, 'w') as outf:
        content = open(file, 'r')
        sentences = content.read().split('.')
        for sent in sentences:
            for word in words:
                if word in sent:
                    outf.write(sent + "\n\n")
                    break


def get_words_ratios(words, file):
    counts = get_counts_from_file(file, words)
    total = sum(counts.values())
    return {word: (100 * counts[word] / total) for word in words}


def get_reflexives_indices(path):
    file = open(path, "r")
    words = file.read().split()
    result = []
    for i, word in enumerate(words):
        #if word in REFLEXIVES:
        if word == "himself":
            result.append(i)
    return result


def add_word_ratios(all_counts_path):
    all_counts = pd.read_excel(all_counts_path)
    num_tokens = all_counts.ix[2].sum()
    all_counts.loc[:, 'ratio'] = 100 * all_counts.ix[2] / num_tokens
    print(all_counts.loc[:, ['ratio']])
    all_counts.to_excel("bla.xlsx")


sentences_with_specific_words("nounk2.txt", REFLEXIVES, "REFLEXIVES.txt")
    #sentences_with_specific_words(os.path.join("generated", file), REFLEXIVES, file + "PRONOMINALS.txt")
