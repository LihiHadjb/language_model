import matplotlib.pyplot as plt
import numpy as np


def plot_mean_probs_of_correct_next_word(ref_pron_avg_probs_pairs):
    barWidth = 0.25
    bars1 = [ref_prob for ref_prob, pron_prob in ref_pron_avg_probs_pairs]
    bars2 = [pron_prob for ref_prob, pron_prob in ref_pron_avg_probs_pairs]

    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    plt.bar(r1, bars1, color='#557f2d', width=barWidth, edgecolor='white', label='himself')
    plt.bar(r2, bars2, color='orange', width=barWidth, edgecolor='white', label='him')


    # plt.xlabel('mean probability assigned', fontweight='bold')
    # plt.xlabel('group', fontweight='bold')
    labels = ['himself him', ' herself her', ' myself me', 'yourself  you', 'themselves  them', 'itself', 'it', 'ourselves', 'us']
    plt.xticks(
        [r + barWidth/4 for r in range(len(bars1))],
        labels)
    plt.title("Mean probability assigned to the \ncorrect pronoun and respective reflexive")
    plt.savefig("prons_indices_acc_complete")


def next_is_ref():
    # next is himself
    himself = 0.0363
    him = 0.0318

    # next is herself
    herself = 0.0111
    her = 0.0687

    # next is myself
    myself = 0.0173
    me = 0.0180

    # next is yourself
    yourself = 0.0314
    you = 0.0658

    # next is themselves
    themselves = 0.0188
    them = 0.0321

    # next is itself
    itself = 0.0191
    it = 0.0161

    # next is ourselves
    ourselves = 0.0039
    us = 0.0074

    pairs = [(himself, him), (herself, her), (myself, me), (yourself, you), (themselves, them), (itself, it), (ourselves, us)]
    plot_mean_probs_of_correct_next_word(pairs)


def next_is_pron():
    # next is him
    himself = 0.0059
    him = 0.0535

    # next is her
    herself = 0.0026
    her = 0.0659

    # next is me
    myself = 0.0024
    me = 0.1356

    # next is you
    yourself = 0.0008
    you = 0.1380

    # next is them
    themselves = 0.0028
    them = 0.0626

    # next is it
    itself = 0.0004
    it = 0.0771

    # next us us
    ourselves = 0.0006
    us = 0.0962

    pairs = [(himself, him), (herself, her), (myself, me), (yourself, you), (themselves, them), (itself, it), (ourselves, us)]
    plot_mean_probs_of_correct_next_word(pairs)

def useless_pie_chart():
    total_himself_as_object = 70
    num_times_himself_greater_than_him_when_himself_is_used_as_object = 19
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    langs = ['himself', 'him']
    data = [num_times_himself_greater_than_him_when_himself_is_used_as_object,
            total_himself_as_object - num_times_himself_greater_than_him_when_himself_is_used_as_object]

    ax.pie(data, labels=langs, autopct='%1.2f%%')
    ax.set_title(
        "Cases in which him/himself is assigned greater probability when true next token is 'himself used as the "
        "object of a verb")
    plt.show()
    plt.savefig("himself_over_him")


next_is_pron()
