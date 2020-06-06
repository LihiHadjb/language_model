import os
import random
import unicodedata

REFLEXIVES = ['myself', 'yourself', 'yourselves', 'himself', 'herself', 'oneself', 'itself', 'ourselves', 'ourself', 'themselves']

#ROOT_DIR = r'C:\Users\10User\Desktop\University\Natural Language Processing\project\datasets\OANC_GrAF\OANC-GrAF'
ROOT_DIR = r'C:\Users\lihin\Documents\uni\NLP\project\datasets\OANC-GrAF'

def find_relexives():
    relfexive_pronoun_files = []
    non_reflexive_pronoun_files = []
    
    for subdir, dirs, files in os.walk(ROOT_DIR):
        for file in [f for f in files if f.endswith('.txt')]:
            p = os.path.join(subdir, file)
            with open(p, 'r') as f:
                try:
                    content = f.read()
                    if any(reflexive in content for reflexive in REFLEXIVES):
                        relfexive_pronoun_files.append(p)
                    else:
                        non_reflexive_pronoun_files.append(p)
                except Exception as e:
                    continue
    
    return relfexive_pronoun_files, non_reflexive_pronoun_files
    

def split_to_train_test_validation(files, train_perc=0.8, test_perc=0.1, valid_perc=0.1):
    assert (train_perc + test_perc + valid_perc == 1)
    files_dup = list(files)
    random.shuffle(files_dup)
    
    num_train = int(len(files_dup) * train_perc)
    num_test = int(len(files_dup) * test_perc)
    return files_dup[:num_train], files_dup[num_train:num_train+num_test], files_dup[num_train+num_test:]
    

def combine_data_into_one_file(files, file_name):
    def strip_accents(text):
        return "".join(char for char in unicodedata.normalize('NFKD', text) if unicodedata.category(char) != 'Mn')
    
    with open(os.path.join(ROOT_DIR, file_name), 'w', encoding='utf8') as f:
        f.writelines([strip_accents(open(file, 'r').read()) for file in files])





relfexive_pronoun_files, non_reflexive_pronoun_files = find_relexives()
relfexive_pronoun_train_files, relfexive_pronoun_test_files, relfexive_pronoun_valid_files = split_to_train_test_validation(relfexive_pronoun_files)
non_reflexive_pronoun_train_files, non_reflexive_pronoun_test_files, non_reflexive_pronoun_valid_files = split_to_train_test_validation(non_reflexive_pronoun_files)

open(os.path.join(ROOT_DIR, 'reflexives.files.train.txt'), 'w').write('\n'.join(relfexive_pronoun_train_files))
open(os.path.join(ROOT_DIR, 'reflexives.files.test.txt'), 'w').write('\n'.join(relfexive_pronoun_test_files))
open(os.path.join(ROOT_DIR, 'reflexives.files.valid.txt'), 'w').write('\n'.join(relfexive_pronoun_valid_files))

open(os.path.join(ROOT_DIR, 'non_reflexives.files.train.txt'), 'w').write('\n'.join(non_reflexive_pronoun_train_files))
open(os.path.join(ROOT_DIR, 'non_reflexives.files.test.txt'), 'w').write('\n'.join(non_reflexive_pronoun_test_files))
open(os.path.join(ROOT_DIR, 'non_reflexives.files.valid.txt'), 'w').write('\n'.join(non_reflexive_pronoun_valid_files))

combine_data_into_one_file(relfexive_pronoun_train_files, 'reflexive.train.txt')
combine_data_into_one_file(relfexive_pronoun_test_files, 'reflexive.test.txt')
combine_data_into_one_file(relfexive_pronoun_valid_files, 'reflexive.valid.txt')

combine_data_into_one_file(non_reflexive_pronoun_train_files, 'non_reflexive.train.txt')
combine_data_into_one_file(non_reflexive_pronoun_test_files, 'non_reflexive.test.txt')
combine_data_into_one_file(non_reflexive_pronoun_valid_files, 'non_reflexive.valid.txt')



# import unidecode
# from nltk.tokenize import word_tokenize
# from nltk.probability import FreqDist
# def normalise_file(file_name):
#     text = open(file_name, 'r').read().decode('utf8')
#     text = unidecode.unidecode(text)
#     fdist = FreqDist(word.lower() for word in word_tokenize(text))
#     common = [i for i, v in fdist.items() if v > 1]
#     mapping = nltk.defaultdict(lambda: '<unk>')
#     for v in common:
#         mapping[v] = v
#     normalised_words = [mapping[word] for word in word_tokenize(text)]
#     normalised_text = ' '.join(normalised_words)
#     open(file_name.replace('.txt', '.normalised.txt') , 'w').write(normalised_text)
# normalise_file('reflexive.train.txt')
# normalise_file('reflexive.test.txt')
# normalise_file('reflexive.valid.txt')
# normalise_file('non_reflexive.train.txt')
# normalise_file('non_reflexive.test.txt')
# normalise_file('non_reflexive.valid.txt')
