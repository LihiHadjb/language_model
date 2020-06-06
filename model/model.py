import torch
import torch.nn as nn
from model.model import LSTM
from model.model import embedded_dropout
from model.model import LockedDropout
from model.weight_drop import WeightDrop


class LSTMModel(nn.Module):
    """Container module with an encoder, a recurrent module, and a decoder."""

    def __init__(self, rnn_type, ntoken, ninp, nhid, nlayers, dropout=0.5, dropouth=0.5, dropouti=0.5, dropoute=0.1, wdrop=0, tie_weights=False, manual_LSTM=False):
        super(LSTMModel, self).__init__()
        self.lockdrop = LockedDropout()
        self.idrop = nn.Dropout(dropouti)
        self.hdrop = nn.Dropout(dropouth)
        self.drop = nn.Dropout(dropout)
        self.encoder = nn.Embedding(ntoken, ninp)
        self.manual = manual_LSTM

        if not self.manual:
            self.lstm = [torch.nn.LSTM(ninp if l == 0 else nhid, nhid if l != nlayers - 1 else (ninp if tie_weights else nhid), 1, dropout=0) for l in range(nlayers)]

        else:
            # now there is no dropout!
            self.lstm = []
            for l in range(nlayers):
                input_size = ninp if l == 0 else nhid
                hidden_size = nhid if l != nlayers - 1 else (ninp if tie_weights else nhid)
                num_layers = 1
                batch_first = False
                self.lstm.append(LSTM(input_size, hidden_size, num_layers, batch_first))

        if wdrop and not self.manual:
            self.lstm = [WeightDrop(rnn, ['weight_hh_l0'], dropout=wdrop) for rnn in self.lstm]

        self.lstm = torch.nn.ModuleList(self.lstm)
        self.decoder = nn.Linear(nhid, ntoken)

        # Optionally tie weights as in:
        # "Using the Output Embedding to Improve Language Models" (Press & Wolf 2016)
        # https://arxiv.org/abs/1608.05859
        # and
        # "Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling" (Inan et al. 2016)
        # https://arxiv.org/abs/1611.01462
        if tie_weights:
            self.decoder.weight = self.encoder.weight

        self.init_weights()

        self.rnn_type = rnn_type
        self.ninp = ninp
        self.nhid = nhid
        self.nlayers = nlayers
        self.dropout = dropout
        self.dropouti = dropouti
        self.dropouth = dropouth
        self.dropoute = dropoute
        self.tie_weights = tie_weights

    def reset(self):
        return True

    def init_weights(self):
        initrange = 0.1
        self.encoder.weight.data.uniform_(-initrange, initrange)
        self.decoder.bias.data.fill_(0)
        self.decoder.weight.data.uniform_(-initrange, initrange)

    def forward(self, input, hidden, return_h=False):
        emb = embedded_dropout(self.encoder, input, dropout=self.dropoute if self.training else 0)

        emb = self.lockdrop(emb, self.dropouti)

        raw_output = emb
        new_hidden = []
        raw_outputs = []
        outputs = []
        gates = []
        for l, rnn in enumerate(self.lstm):
            current_input = raw_output
            if self.manual:
                raw_output, new_h, new_gates = rnn(raw_output, hidden[l])
            else:
                raw_output, new_h = rnn(raw_output, hidden[l])
            new_hidden.append(new_h)
            raw_outputs.append(raw_output)
            if self.manual:
                gates.append(new_gates)
            if l != self.nlayers - 1:
                raw_output = self.lockdrop(raw_output, self.dropouth)
                outputs.append(raw_output)
        hidden = new_hidden
        output = self.lockdrop(raw_output, self.dropout)
        outputs.append(output)

        result = output.view(output.size(0)*output.size(1), output.size(2))

        ret = (result, hidden,)
        if return_h:
            ret = ret + (raw_outputs, outputs,)
        if self.manual:
            ret = ret + (gates,)
        return ret

    def init_hidden(self, bsz):
        weight = next(self.parameters()).data

        return [(weight.new(1, bsz, self.nhid if l != self.nlayers - 1 else (self.ninp if self.tie_weights else self.nhid)).zero_(),
                weight.new(1, bsz, self.nhid if l != self.nlayers - 1 else (self.ninp if self.tie_weights else self.nhid)).zero_())
                for l in range(self.nlayers)]

