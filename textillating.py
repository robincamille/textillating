# -*- coding: utf-8 -*-

##Make a bland book exciting by upping the sentiment
##
##POS tag text 
##Find words in the text that have wordnet synonyms with same sense
##Find the synonym with the least MOST sentiment (using word lists) 
##Replace 
##Tack on word ending 

from random import randint
from nltk.corpus import wordnet as wn
from nltk import word_tokenize as tok
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk import pos_tag as pos
from nltk.sentiment.vader import SentimentIntensityAnalyzer

detok = TreebankWordDetokenizer()
sid = SentimentIntensityAnalyzer()

#text = "Mr. Pocket being justly celebrated. He gave most excellent practical advice, and for having a clear and sound perception of things and a highly judicious mind, I had some notion in my heart-ache of begging him to accept my confidence. But happening to look up at Mrs. Pocket as she sat reading her book of dignities after prescribing Bed as a sovereign remedy for baby, I thought—Well—No, I wouldn't. "
#text = "I am good, excellent, holy, although I feel bad, terrible, evil."

filename = open('house_of_the_seven_gables.txt','r')
text = filename.read()
filename.close()

outfile = open('house_of_the_seven_gables_xtreme.txt','w')



text = pos(tok(text)) #('excellent', 'JJ') 

#print(text)
new_text = []

negatives = ['not','never','no']
modifiers = ['ABSOLUTELY','ACTUALLY','ACUTELY','ADMITTEDLY','AMPLY',\
'as a MATTER of FACT','ASSUREDLY','ASTONISHINGLY','AUTHENTICALLY',\
'AWFULLY','BEYOND DOUBT','CATEGORICALLY','CERTAINLY','CONSIDERABLY',\
'DE FACTO','DEARLY','DECIDEDLY','DEEPLY','EASILY','EMINENTLY','EMPHATICALLY',\
'EXAGGERATEDLY','EXCEEDINGLY','EXCESSIVELY','EXTENSIVELY','EXTRAORDINARILY',\
'EXTREMELY','FOR REAL','GENUINELY','GREATLY','HIGHLY','HONESTLY','in ACTUALITY',\
'in EFFECT','in FACT','in POINT of FACT','in REALITY','INCREDIBLY','INDEED',\
'INDISPENSABLY','INDUBITABLY','LARGELY','LEGITIMATELY','LITERALLY','NOTABLY',\
'NOTHING ELSE but','NOTICEABLY','PARTICULARLY','POSITIVELY','POWERFULLY',\
'PRECISELY','PRESSINGLY','PRODIGIOUSLY','PROFOUNDLY','REMARKABLY',\
'SUBSTANTIALLY','SUPER','ACUTELY','EXCEPTIONALLY','HUGELY','IMMENSELY',\
'INORDINATELY','INTENSELY','OVERLY','QUITE','SEVERELY','STRIKINGLY','TERRIBLY',\
'TERRIFICALLY','TOO','TOTALLY','UNCOMMONLY','UNDULY','UNUSUALLY','UTTERLY',\
'VERY','ALMIGHTY','DRASTICALLY','EXORBITANTLY','IMMODERATELY','MARKEDLY',\
'PLENTY','POWERFUL','PROHIBITIVELY','RADICALLY','RARELY','SURPASSINGLY',\
'WAY','ULTRA','VIOLENTLY','VITALLY','SUPERLATIVELY','SURELY','SURPRISINGLY',\
'TRULY','UNDOUBTEDLY','UNMISTAKABLY','UNQUESTIONABLY','VASTLY','VERILY',\
'WELL','WONDERFULLY']

for word in text:
    word_score = sid.polarity_scores(word[0])['compound']
    use_synonym = word[0] #updates later
    possible_synonyms = []
    if word[0] in negatives:
        use_synonym = word[0].upper()
    elif word[1] == 'JJ':
        for syn in wn.synsets(word[0]):
            for lemma in syn.lemmas():
                syn_meta = str(syn).split('.') #match part of speech
                if syn_meta[1] == 'a' or 's': #adjectives
                    possible_synonyms.append(lemma.name())
        all_synonyms = set(possible_synonyms) #de-dupe
        for synonym in all_synonyms:
            syn_score = sid.polarity_scores(synonym)['compound']
            if word_score == 0:
                use_synonym = modifiers[randint(0,len(modifiers)-1)] + ' ' + word[0].upper() #VERY neutral
            elif word_score > 0:
                if syn_score > sid.polarity_scores(use_synonym)['compound']:
                    use_synonym = synonym.upper() #choose most xtreme synonym (positive)
            elif word_score < 0:
                if syn_score < sid.polarity_scores(use_synonym)['compound']:
                    use_synonym = synonym.upper() #choose most xtreme synonym (negative)
    elif word[0] == '.':
        use_synonym = '!'
    elif word[0] == '!':
        use_synonym = '!!!!!!!!!!!!!'
    elif word[0] == '?':
        use_synonym = '??!!'
    else:
        use_synonym = word[0]
    new_text.append(use_synonym)

#print(detok.detokenize(new_text))


outfile.write(detok.detokenize(new_text))

outfile.close()

print('All done')