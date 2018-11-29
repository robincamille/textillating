# -*- coding: utf-8 -*-

##Make a bland book exciting by upping the sentiment
##
##POS tag text 
##Find words in the text that have wordnet synonyms with same sense
##Find the synonym with the least MOST sentiment (using word lists) 
##Replace 
##Tack on word ending 

from nltk.corpus import wordnet as wn
from nltk import word_tokenize as tok
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk import pos_tag as pos
from nltk.sentiment.vader import SentimentIntensityAnalyzer

detok = TreebankWordDetokenizer()
sid = SentimentIntensityAnalyzer()

# from afinn import Afinn
# afinn = Afinn()

text = "Mr. Pocket being justly celebrated. He gave most excellent practical advice, and for having a clear and sound perception of things and a highly judicious mind, I had some notion in my heart-ache of begging him to accept my confidence. But happening to look up at Mrs. Pocket as she sat reading her book of dignities after prescribing Bed as a sovereign remedy for baby, I thought—Well—No, I wouldn't. "
#text = "I am good, excellent, holy, although I feel bad, terrible, evil."

text = pos(tok(text)) #('excellent', 'JJ') 

#print(text)
new_text = []

for word in text:
    word_score = sid.polarity_scores(word[0])['compound']
    use_synonym = word[0] #updates later
    possible_synonyms = []
    if word[1] == 'JJ':
        for syn in wn.synsets(word[0]):
            for lemma in syn.lemmas():
                #possible_synonyms.append(lemma.name())
                syn_meta = str(syn).split('.') # match part of speech
                if syn_meta[1] == 'a' or 's':
                    possible_synonyms.append(lemma.name())
    # all_synonyms = [item for sublist in possible_synonyms for item in sublist]
        all_synonyms = set(possible_synonyms)
        for synonym in all_synonyms:
            syn_score = sid.polarity_scores(synonym)['compound']
            if word_score == 0:
                pass
            elif word_score > 0:
                if syn_score > sid.polarity_scores(use_synonym)['compound']:
                    #print('use ',synonym, syn_score, ' instead of ',word[0], word_score)
                    use_synonym = synonym.upper()
            elif word_score < 0:
                if syn_score < sid.polarity_scores(use_synonym)['compound']:
                    #print('use ',synonym, syn_score, ' instead of ',word[0], word_score)
                    use_synonym = synonym.upper()
        #new_text.append(use_synonym)
        #print('use ',use_synonym, sid.polarity_scores(use_synonym)['compound'], ' instead of ',word[0], word_score)
    elif word[0] == '.':
        use_synonym = '!'
    else:
        use_synonym = word[0]
    new_text.append(use_synonym)

print(detok.detokenize(new_text))
#uses afinn:

# for word in text:
#     word_score = int(afinn.score(word[0]))
#     possible_synonyms = []
#     if word[1] == 'JJ':
#         for syn in wn.synsets(word[0]):
#             for lemma in syn.lemmas():
#                 possible_synonyms.append(lemma.name())
#                 # syn_meta = str(syn).split('.') # match part of speech
#                 # if syn_meta[1] == 'a':
#                 #     possible_synonyms.append(syn.lemma_names())
#     # all_synonyms = [item for sublist in possible_synonyms for item in sublist]
#     all_synonyms = set(possible_synonyms)
#     for synonym in all_synonyms:
#         syn_score = int(afinn.score(synonym))
#         if word_score > 0:
#             if syn_score >= word_score:
#                 print('use ',synonym, syn_score, ' instead of ',word[0], word_score)
#         elif word_score < 0:
#             if syn_score <= word_score:
#                 print('use ',synonym, syn_score, ' instead of ',word[0], word_score)
                
    #print(word, all_synonyms)
                #print(word[0], afinn.score(word[0]), syn)





