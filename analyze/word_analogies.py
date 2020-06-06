
import math


def vector_len(v):
    return math.sqrt(sum([x*x for x in v]))


def dot_product(v1, v2):
    assert v1.shape[0] == v2.shape[0]
    return sum([x*y for (x,y) in zip(v1, v2)])


def cosine_similarity(v1, v2):
    """
    Returns the cosine of the angle between the two vectors.
    Results range from -1 (very different) to 1 (very similar).
    """
    return dot_product(v1, v2) / (vector_len(v1) * vector_len(v2))


def sorted_by_similarity(all_embeddings, base_vector):
    """Returns words sorted by cosine distance to a given vector, most similar first"""
    words_with_distance = [(cosine_similarity(base_vector, vec), ind) for ind, vec in enumerate(all_embeddings)]
    # We want cosine similarity to be as large as possible (close to 1)
    return sorted(words_with_distance, key=lambda t: t[0], reverse=True)


def analogy(word1, word2, word3, all_embeddings, corpus):
    idx1 = corpus.dictionary.word2idx[word1]
    idx2 = corpus.dictionary.word2idx[word2]
    idx3 = corpus.dictionary.word2idx[word3]

    base_vector = all_embeddings[idx2] - all_embeddings[idx1] + all_embeddings[idx3]
    sorted_by_cosine = sorted_by_similarity(all_embeddings, base_vector)
    return [corpus.dictionary.idx2word[sorted_by_cosine[0][1]], corpus.dictionary.idx2word[sorted_by_cosine[1][1]]]

