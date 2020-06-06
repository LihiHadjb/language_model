import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def repackage_hidden(h):
    """Wraps hidden states in new Tensors,
    to detach them from their history."""
    if isinstance(h, torch.Tensor):
        return h.detach()
    else:
        return tuple(repackage_hidden(v) for v in h)


def batchify(data, bsz, args):
    # Work out how cleanly we can divide the dataset into bsz parts.
    nbatch = data.size(0) // bsz
    # Trim off any extra elements that wouldn't cleanly fit (remainders).
    data = data.narrow(0, 0, nbatch * bsz)
    # Evenly divide the data across the bsz batches.
    data = data.view(bsz, -1).t().contiguous()
    if args.cuda:
        data = data.cuda()
    return data


def get_batch(source, i, args, seq_len=None, evaluation=False):
    seq_len = min(seq_len if seq_len else args.bptt, len(source) - 1 - i)
    data = source[i:i+seq_len]
    target = source[i+1:i+1+seq_len].view(-1)
    return data, target


def get_probs_to_keep_indices(probs, thresh, keep_word, corpus):
    if thresh is None or keep_word is None:
        return False
    # keep_word_prob = prob[corpus.dictionary.word2idx[keep_word]]
    # return keep_word_prob >= thresh
    keep_word_idx = corpus.dictionary.word2idx[keep_word]
    keep_word_probs = probs[:, keep_word_idx]
    result = np.nonzero(keep_word_probs >= thresh)
    result = result.view(result.shape[0])
    return result



def save_keep_probs(keep_probs, keep_positions, keep_word, corpus):
    print("saving probabilities!")
    if keep_word is None:
        return

    if len(keep_probs) > 0:
        col_names = {'index': 'idx'}
        for i in range(len(keep_probs)):
            col_names[i] = keep_positions[i]

        keep_probs = pd.DataFrame(torch.cat(keep_probs, dim=0).transpose(0, 1).cpu().numpy()).rename(columns=col_names)
        #keep_probs = pd.DataFrame(torch.stack(keep_probs).transpose(0, 1).cpu().numpy()).rename(columns={'index': 'idx', 0: 'probability'})
        #keep_probs['position'] = keep_positions
        keep_probs['word'] = corpus.dictionary.idx2word
    else:
        keep_probs = pd.DataFrame(columns=["Nothing to keep"])

    keep_probs.to_csv(keep_word + '_probs.csv')


def hist(x, word):
    plt.hist(x)
    plt.title(word)
    plt.savefig(word + ".png")


def plot_pairs(prob_pairs, word1, word2):
    title = word1 + ", " + word2
    x, y = zip(*prob_pairs)
    # hist(x, word1)
    # hist(y, word2)
    plt.scatter(x, y)
    plt.title(title + "\n" + str(len(prob_pairs)) + " random time steps")
    plt.xlabel(word1)
    plt.ylabel(word2)
    #line = mlines.Line2D([1, 1], [2, 2], color='red')
    plt.savefig(title + ".png")


def save_means(means, corpus):
    col_names = {'index': 'idx', 0:'mean', 1: 'word'}
    df = pd.DataFrame(means.cpu.numpy()).rename(columns=col_names)
    df['word'] = corpus.dictionary.idx2word
    df.to_csv('probability_means.csv')

