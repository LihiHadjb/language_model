###############################################################################
# Language Modeling on Penn Tree Bank
#
# This file generates new sentences sampled from the language model
#
###############################################################################
import argparse
import os
import torch
from model.model import data
import pandas as pd

parser = argparse.ArgumentParser(description='PyTorch PTB Language Model')

# Model parameters.
parser.add_argument('--data', type=str, default='./data/reflexives',
                    help='location of the data corpus')
parser.add_argument('--checkpoint', type=str, default='norm_ref_not_manual_new2.pt',
                    help='model checkpoint to use')
# parser.add_argument('--outf', type=str, default='generated.txt',
#                     help='output file for generated text')
# parser.add_argument('--words', type=int, default='1000',
#                     help='number of words to generate')
parser.add_argument('--seed', type=int, default=1111,
                    help='random seed')
parser.add_argument('--cuda', type=bool, default=True,
                    help='use CUDA')
# parser.add_argument('--temperature', type=float, default=1.0,
#                     help='temperature - higher will increase diversity')
parser.add_argument('--log-interval', type=int, default=100,
                    help='reporting interval')
parser.add_argument('--manual_LSTM', type=bool, default=False, help='False for pytorch nn.LSTM')
args = parser.parse_args()

# Set the random seed manually for reproducibility.
torch.manual_seed(args.seed)
if torch.cuda.is_available():
    if not args.cuda:
        print("WARNING: You have a CUDA device, so you should probably run with --cuda")
    else:
        torch.cuda.manual_seed(args.seed)
device = torch.device("cuda" if args.cuda else "cpu")

with open(args.checkpoint, 'rb') as f:
    # model = torch.load(f)[0]
    model = torch.load(f, map_location=lambda storage, loc: storage)[0]
model.eval()

if args.cuda:
    model.cuda()
else:
    model.cpu()

# corpus = data.Corpus("data/reflexives")

corpus = data.Corpus(args.data)
ntokens = len(corpus.dictionary)



# this is not working for some reason
# Retruns a tensor of shape(1, vocab_size)) with the next word probabilily of the entire sentence and saves it to a csv
def next_word_probs_to_csv(probs):

    df = pd.DataFrame(probs.cpu().numpy()).rename(columns={'index': 'idx', 0: 'probability'})
    df['word'] = corpus.dictionary.idx2word

    if not os.path.exists("raw"):
        os.mkdir("raw")
    if not os.path.exists("sorted"):
        os.mkdir("sorted")

    file_name ="my_sent"
    df.to_csv(os.path.join("raw", file_name + ".csv"))
    # df.to_csv(file_name + ".csv")

    sorted_df = df.sort_values(by=['probability'], ascending=False)
    sorted_df.to_csv(os.path.join("sorted", file_name + "_sorted" + ".csv"))
    # sorted_df.to_csv(file_name + "_sorted" + ".csv")

    return probs




def generate_text(num_words, temperature):
    assert (temperature >= 1e-3)
    hidden = model.init_hidden(1)
    outdir = "generated"
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    outf_name = os.path.join(outdir,
                             "generated_from_" + os.path.splitext(args.checkpoint)[0] + "_" + str(num_words) + "_t" + str(
                                 temperature) + "s" + str(args.seed) + ".txt")

    with torch.no_grad():
        input = torch.rand(1, 1).mul(ntokens).long()

        if args.cuda:
            input.data = input.data.cuda()

        with open(outf_name, 'w') as outf:
            for i in range(num_words):
                if args.manual_LSTM:
                    output, hidden, gates = model(input, hidden)
                else:
                    output, hidden = model(input, hidden)
                word_weights = torch.log_softmax(model.decoder(output).squeeze().data.div(temperature), dim=-1).exp()
                # word_weights = model.decoder(output).squeeze().data.div(temperature).exp().cpu()

                word_idx = torch.multinomial(word_weights, 1)[0]
                while word_idx == corpus.dictionary.word2idx['<unk>']:
                    word_idx = torch.multinomial(word_weights, 1)[0]

                input.data.fill_(word_idx)
                word = corpus.dictionary.idx2word[word_idx]
                if i == 18483:
                    print(word)
                    next_word_probs_to_csv(word_weights)

                outf.write(word + ('\n' if i % 20 == 19 else ' '))

                if i % args.log_interval == 0:
                    print('| Generated {}/{} words'.format(i, num_words))
    return outf_name


def run_generate_texts():
    #temps = [i for i in np.arange(0.9, 1.05, 0.05)]
    temps = [1]
    for temp in temps:
        generate_text(500000, temp)



run_generate_texts()
