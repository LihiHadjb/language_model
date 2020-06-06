import os

import argparse

ROOT_DIR = r'/specific/netapp5/joberant/nlp_fall_2020/lihi_dori/nlp_project/awd-lstm-lm/data'
REFLEXIVES = ['myself', 'yourself', 'yourselves', 'himself', 'herself', 'oneself', 'itself', 'ourselves', 'ourself', 'themselves']

# parser = argparse.ArgumentParser(description='Word Statistics')
# parser.add_argument('--file', type=str, default=ROOT_DIR, help='file to get statistics for')
# parser.add_argument('--outf', type=str, default='stats.txt', help='output file for statistics')
# args = parser.parse_args()

def print_counts(file_name):
    file = open(os.path.join(ROOT_DIR, file_name), "r")
    content = file.read()
    total = 0
    for word in REFLEXIVES:
        word_cnt = content.count(word)
        total += word_cnt
        print(word, ":", word_cnt)
    print("Count of all REFLEXIVES:", total)

def print_reflexive_info(train_file, test_file, validation_file):
    print("---Training set---")
    print_counts(train_file)

    print("---Test set---")
    print_counts(test_file)

    print("---Validation set---")
    print_counts(validation_file)

print("--------Files with reflexives--------")
print_reflexive_info('reflexives/train.txt', 'reflexives/test.txt', 'reflexives/valid.txt')

print("--------Files without reflexives--------")
print_reflexive_info('non_reflexives/train.txt', 'non_reflexives/test.txt', 'non_reflexives/valid.txt')