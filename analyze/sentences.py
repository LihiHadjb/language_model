sentences = ["she hugged",
             "can you talk with",
             "can you talk to",
             "he assigned",
             "he assigned him to",
             "she assigned",
             "she assigned him to",
             "he assigned himself to",
             "the student put the computers near",
             "the students put the computers near",
             "it is illegal for",
             "it is illegal that",
             "he wanted to kill",
             "he wanted to congratulate",
             "he convinced",
             "he convinced him to kill",
             "she convinced",
             "she convinced him to kill",
             "he convinced him to congratulate",
             "she convinced him to kill",
             "she convinced him to congratulate",
             "his professor convinced",
             "his professor convinced him to kill",
             "her professor convinced",
             "her professor convinced him to kill",
             "their professor convinced",
             "his professors convinced her to congratulate",
             "she is likely to congratulate",
             "she is likely to kill",
             "he is likely to congratulate",
             "he is likely to kill",
             "that she told",
             "that she told him the story made",
             "he proved",
             "he believes",
             "his parents want",
             "his parents believe",
             "he heard",
             "his mother spoils",
             "he likes jokes about",
             "she likes jokes about",
             "they like jokes about"]

sentences2 = ["john would be eager for",
              "for himself to dance would be surprising",
              "their professors convinced her to congratulate",
              "rumor says that for",
              "he tried to kill",
              "i heard that he is suicidal and he tried to kill",
              # "rumor says he is suicidal and that he tried to kill",
              "rumor says he is suicidal and tried to kill"]

phase2 = ["she hugs",
          "he hugs",
          "he hugged",
          "i think that for",
          "rumor has it that for",
          "the rumor is that for",
          # "rumour has it that for",
          # "the rumour is that for",
          "their professors convinced her to congratulate"]

hiddens = ["he hugged him", "she hugged her"]

# for_tsne_non_reflexives = ["the rumor he has heard made",
#                            "the new rules make", "rumor has it that for", "it is illegal for", "it is illegal that",
#                            "john would be eager for"]
#
# for_tsne_reflexives = ["the boy made",
#                        "the boy spoiled",
#                        "the boy"]


tsne_no_ref = ["the rumor about her surprised",
               "the rumor about him surprised"]

tsne_yes_ref = ["the rumor that she surprised",
                "the rumor that he surprised",
                "his rumor about",
                "her rumor about"]

tsne_neutral = ["it is surprising for"]

tsne_no_ref_full = ["the rumor about her surprised him",
                    # "the rumor about her surprised her",
                    "the rumor about her surprised himself", "the rumor about her surprised herself",
                    "the rumor about him surprised him",
                    # "the rumor about him surprised her",
                    "the rumor about him surprised himself", "the rumor about him surprised herself"]

cl1 = ["the rumor that he heard made", "the man that he met angered", "the man that he met angered",
       "the rumor that he heard made"]
cl1_labels = [0, 0, 1, 1]

tsne_yes_ref_full = ["the rumor that she surprised him",
                     # "the rumor that she surprised her",
                     "the rumor that she surprised himself", "the rumor that she surprised herself",
                     "the rumor that he surprised him",
                     # "the rumor that he surprised her",
                     "the rumor that he surprised himself", "the rumor that he surprised herself",
                     "his rumor about him",
                     # "his rumor about her",
                     "his rumor about himself", "his rumor about herself",
                     "her rumor about him",
                     # "her rumor about her",
                     "her rumor about himself", "her rumor about herself"]

tsne_neutral_full = ["it is surprising for him",
                     # "it is surprising for her",
                     "it is surprising for herself",
                     "it is surprising for himself", ]

tsne_labels = [0 for i in tsne_neutral_full + tsne_no_ref_full + tsne_yes_ref_full]

refs_impossible = ["it seems that",
                   "it appears that",
                   "it would be nice to know that",
                   "it would be nice if",
                   "it will be illegal for",
                   "it it illegal for",
                   "it is convenient for",
                   "it is inconvenient for",
                   "it is easy for",
                   "it is tough for",
                   "it is surprising for",
                   "it would be illegal for",
                   "it would be convenient for",
                   "it would be inconvenient for",
                   "it is easy for",
                   "it is tough for",
                   "it is surprising for",
                   "the rumor that",
                   "the rumor he has heard made",
                   "the rumor she has heard made",
                   "the rumor they have heard made",
                   "the rumor you have heard made",
                   "the report about",
                   "the reports about",
                   "the report about his death surprised",
                   "the report about her death surprised",
                   "the report about their death surprised",
                   "the report about his death made",
                   "the report about her death made",
                   "the report about their death made",
                   "the story about the boy alarmed",
                   "the story about the girl alarmed",
                   "the story about the kids alarmed",
                   "the rumor about the president made",
                   "the rumors about the president made",
                   "the rumor about the presidents made",
                   "the rumors about the presidents made",
                   "the rumor spread",
                   "the story spread"]

refs_possible_for_hadgasha = ["john",
                              "the guys",
                              "the girls",
                              "the the boys",
                              "he",
                              "she",
                              "you",
                              "john told me that george"
                              "the nurse told me that the girl",
                              "the doctor told me that the nurse"]

mary_criticized_john_commas = [  # "john thought that the teacher criticized",
    # "john thought that the teacher did not criticize",

    "john said that the teacher criticized everybody but",
    "according to john , the teacher criticized everybody but",
    "john thought that the teacher criticized everybody but",
    "john heard that the teacher criticized everybody but",
    "john thought that while he was away , the teacher criticized everybody but",
    "john said that while he was away , the teacher criticized everybody but",

    "according to what happened , the teacher criticized everybody but",
    "speaking of john , the teacher criticized everybody but",
    "while john was away , the teacher criticized everybody but",
]

mary_criticized_john_no_commas = [  # "while john was away the teacher criticized everybody but",
    # "while john was away the teacher did not criticize everybody but",
    # "while john was away the teacher did not criticize",

    # "john said that the teacher criticized everybody but",
    "according to him the teacher criticized everybody but",
    "he says that the teacher criticized everybody but",
    # "he said that the teacher criticized everybody but",
    "he claimed that the teacher criticized everybody but",
    "he told me that the teacher criticized everybody but",
    # "i heard of him that the teacher criticized everybody but",

    # "facts are that while john was away the teacher criticized everybody but",
    "speaking of him the teacher criticized everybody but",
    "as for him the teacher criticized everybody but",
    "rumor has it that the teacher criticized everybody but",
    "the report about him says that the teacher criticized everybody but",
    "according to the report about him the teacher criticized everybody but"

]

the_girl_is_taller = [  # "this man said that the girl is a little smarter than", #0
    # "according to this man the girl is a little smarter than", #1
    # "this man claims that the girl is a little smaller than", #2

    # "as for this man the girl is a little smarter than", #2
    # "speaking of this man the girl is a little smarter than", #3

    # "this girl said that the man is a little smarter than", #4
    # "according to this girl the man is a little smarter than", #5
    # "this girl claims that the man is a little smaller than", #7

    # "as for this girl the man is a little smarter than", #6
    # "speaking of this girl the man is a little smarter than", #7

    "he said that she is smarter than",  # 8
    "according to him she is smarter than",  # 9
    "as for him she is smarter than",  # 10
    "speaking of him she is smarter than",  # 11

    "she said that he is smarter than",  # 12
    "according to her he is smarter than",  # 13
    "as for her he is smarter than",  # 14
    "speaking of her he is smarter than"  # 15
]

the_girl_is_taller_labels = [0, 0, 1, 1, 0, 0, 1, 1]

she_is_smarter = ["he said that she is smarter than",  # 0
                  "she is smarter than",  # 1
                  "they said that he said she is smarter than",  # 2
                  "i said that he said she is smarter than",  # 3
                  "you said that he said she is smarter than",  # 4
                  "it said that he said she is smarter than",  # 5
                  "he said that he said she is smarter than",  # 6

                  "she said that he is smarter than",  # 7
                  "he is smarter than",  # 8
                  "they said that she said he is smarter than",  # 9
                  "i said that she said he is smarter than",  # 10
                  "you said that she said he is smarter than",  # 11
                  "it said that she said he is smarter than",  # 12
                  "she said that he is smarter than",  # 13

                  "she said that they are smarter than",  # 14
                  "he said that they are smarter than",  # 15
                  "it said that they are smarter than",  # 16
                  "she said that she said they are smarter than",  # 17
                  "she said that he said they are smarter than",  # 18
                  "he said that he said they are smarter than",  # 19
                  "he said the she said they are smarter than",
                  "they said the they are smarter than",
                  "he said that they said they are smarter than",
                  "they said that he said they are smarter than"  # 20
                  "she said that they said they are smarter than",
                  "they said that she said they are smarter than"  # 20
                  "they are smarter than"]  # 21

mary_labels = [0, 0, 0, 0, 1, 1, 1, 1, 1]

new_idea = ["it is waiting but it is illegal for",
            "it is illegal but it is waiting for",
            "it is searching but it is impossible for",
            "it is impossible but it is searching for",
            "it is sorry but it is interesting for",
            "it is interesting but it is sorry for",

            "it is paying but it is surprising for",
            "it is surprising but it is paying for",
            "it is praying but it is challenging for",
            "it is challenging but it is praying for",
            "it is asking but it is crucial for",
            "it is crucial but it is asking for",
            "it is longing but it is inefficient for",
            "it is inefficient but it is longing for",
            "it is preparing but it is hard for",
            "it is hard but it is preparing for",
            "it is voting but it is scary for",
            "it is scary but it is voting for",
            "it is wishing but it is nice for",
            "it is nice but it is wishing for"]

new_idea_he = ["he is waiting but it is illegal for",
               "it is illegal but he is waiting for",
               "he is searching but it is impossible for",
               "it is impossible but he is searching for",
               "he is sorry but it is interesting for",
               "it is interesting but he is sorry for",

               "he is paying but it is surprising for",
               "it is surprising but he is paying for",
               "he is praying but it is challenging for",
               "it is challenging but he is praying for",
               "he is asking but it is crucial for",
               "it is crucial but he is asking for",
               "he is longing but it is inefficient for",
               "it is inefficient but he is longing for",
               "he is preparing but it is hard for",
               "it is hard but he is preparing for",
               "he is voting but it is scary for",
               "it is scary but he is voting for",
               "he is wishing but it is nice for",
               "it is nice but he is wishing for"]

new_idea_labels = [0 if i % 2 == 0 else 1 for i in range(len(new_idea))]

physcicist_like_him = ["the woman said to the man that doctors like",
                       "the woman said about the man that doctors like",
                       # "the woman heard from the man that physicists like",
                       # "the woman heard about the man that physicists like",

                       # "the girl said to the boy that physicists like",
                       # "the girl said about the boy that physicists like",
                       # "the girl heard from the boy that physicists like",
                       # "the girl heard about the boy that physicists like",
                       # "the girl said to the man that physicists like",
                       # "the girl said about the man that physicists like",
                       # "the girl heard from the man that physicists like",
                       # "the girl heard about the man that physicists like",
                       # "the woman said to the boy that physicists like",
                       # "the woman said about the boy that physicists like",
                       # "the woman heard from the boy that physicists like",
                       # "the woman heard about the boy that physicists like",

                       "the man said to the woman that doctors like",
                       "the man said about the woman that doctors like",
                       # "the man heard from the woman that physicists like",
                       # "the man heard about the woman that physicists like",

                       "the teacher said to the doctor that doctors like",
                       "the teacher said about the doctor that doctors like",

                       "the doctor said to the teacher that women like",
                       "the teacher said about the doctor that doctors like",

                       "the woman said to the man that teachers like",
                       "the woman said about the man that teachers like",

                       "the man said to the woman that teachers like",
                       "the man said about the woman that teachers like",

                       "the teacher said to the driver that men like",
                       "the teacher said about the driver that men like",

                       "the driver said to the teacher that women like",
                       "the driver said about the teacher that women like",

                       "the driver said to the teacher that men like",
                       "the driver said about the teacher that men like",

                       "the driver said to the man that men like",
                       "the driver said about the man that men like",

                       "the dancer said to the driver that women like",
                       "the dancer said about the driver that women like",

                       "the driver said to the dancer that women like",
                       "the driver said about the dancer that women like",

                       "the driver said to the dancer that men like",
                       "the driver said about the dancer that men like"

                       ]

phys_labels = [0 if i % 2 == 0 else 1 for i in range(len(physcicist_like_him))]

promise = ["he promised her to give",
           "he promised her to give a present to",
           "he promised her kids to write a diary for",
           "he promised their mother to write a diary for"]

promise2 = ["he promised her kids to give a present to",
            "he promised the kids to give a present to",
            "he promised her kids to write a diary for",
            "he promised her parents to give a present for",
            "he promised her parents to write a diary for"]

hugged = ["he hugged",
          "she hugged",
          "they hugged",
          "i hugged",
          # "you hugged",

          "he said that he hugged",
          "he said that she hugged",
          "he said that they hugged",
          "he said that i hugged",
          # "he said that you hugged",

          "she said that he hugged",
          "she said that she hugged",
          "she said that they hugged",
          "she said that i hugged",
          # "she said that you hugged",

          "they said that he hugged",
          "they said that she hugged",
          "they said that they hugged",
          "they said that i hugged",
          # "they said that you hugged",

          "i said that he hugged",
          "i said that she hugged",
          "i said that they hugged",
          "i said that i hugged",
          # "i said that you hugged",

          "you said that he hugged",
          "you said that she hugged",
          "you said that they hugged",
          "you said that i hugged",
          # "you said that you hugged"
          ]

loved = ["he loved",
         "she loved",
         "they loved",
         "i loved",
         # "you loved",

         "he said that he loved",
         "he said that she loved",
         "he said that they loved",
         "he said that i loved",
         # "he said that you loved",

         "she said that he loved",
         "she said that she loved",
         "she said that they loved",
         "she said that i loved",
         # "she said that you loved",

         "they said that he loved",
         "they said that she loved",
         "they said that they loved",
         "they said that i loved",
         # "they said that you loved",

         "i said that he loved",
         "i said that she loved",
         "i said that they loved",
         "i said that i loved",
         # "i said that you loved",

         "you said that he loved",
         "you said that she loved",
         "you said that they loved",
         "you said that i loved",
         # "you said that you loved"
         ]

defended = ["he defended",
            "she defended",
            "they defended",
            "i defended",
            "you defended",

            "he said that he defended",
            "he said that she defended",
            "he said that they defended",
            "he said that i defended",
            "he said that you defended",

            "she said that he defended",
            "she said that she defended",
            "she said that they defended",
            "she said that i defended",
            "she said that you defended",

            "they said that he defended",
            "they said that she defended",
            "they said that they defended",
            "they said that i defended",
            "they said that you defended",

            "i said that he defended",
            "i said that she defended",
            "i said that they defended",
            "i said that i defended",
            "i said that you defended",

            "you said that he defended",
            "you said that she defended",
            "you said that they defended",
            "you said that i defended",
            "you said that you defended",

            "he heard that he defended",
            "he heard that she defended",
            "he heard that they defended",
            "he heard that i defended",
            "he heard that you defended",

            "she heard that he defended",
            "she heard that she defended",
            "she heard that they defended",
            "she heard that i defended",
            "she heard that you defended",

            "they heard that he defended",
            "they heard that she defended",
            "they heard that they defended",
            "they heard that i defended",
            "they heard that you defended",

            "i heard that he defended",
            "i heard that she defended",
            "i heard that they defended",
            "i heard that i defended",
            "i heard that you defended",

            "you heard that he defended",
            "you heard that she defended",
            "you heard that they defended",
            "you heard that i defended",
            "you heard that you defended"
            ]

convinced = ["he convinced",
             "she convinced",
             "they convinced",
             "i convinced",
             "you convinced",

             "he said that he convinced",
             "he said that she convinced",
             "he said that they convinced",
             "he said that i convinced",
             "he said that you convinced",

             "she said that he convinced",
             "she said that she convinced",
             "she said that they convinced",
             "she said that i convinced",
             "she said that you convinced",

             "they said that he convinced",
             "they said that she convinced",
             "they said that they convinced",
             "they said that i convinced",
             "they said that you convinced",

             "i said that he convinced",
             "i said that she convinced",
             "i said that they convinced",
             "i said that i convinced",
             "i said that you convinced",

             "you said that he convinced",
             "you said that she convinced",
             "you said that they convinced",
             "you said that i convinced",
             "you said that you convinced",

             "he heard that he convinced",
             "he heard that she convinced",
             "he heard that they convinced",
             "he heard that i convinced",
             "he heard that you convinced",

             "she heard that he convinced",
             "she heard that she convinced",
             "she heard that they convinced",
             "she heard that i convinced",
             "she heard that you convinced",

             "they heard that he convinced",
             "they heard that she convinced",
             "they heard that they convinced",
             "they heard that i convinced",
             "they heard that you convinced",

             "i heard that he convinced",
             "i heard that she convinced",
             "i heard that they convinced",
             "i heard that i convinced",
             "i heard that you convinced",

             "you heard that he convinced",
             "you heard that she convinced",
             "you heard that they convinced",
             "you heard that i convinced",
             "you heard that you convinced"
             ]

hugged_labels = [i % 4 for i in range(len(hugged))]

professor = ["the professor that she likes convinced",
             "the professors that she likes convinced",
             "their professor that she likes convinced",
             "their professors that she likes convinced"]

smarter_new = ["according to him she is smarter than",
               "he says that she is smarter than",
               "as for him she is smarter than",
               "speaking of him she is smarter than"]