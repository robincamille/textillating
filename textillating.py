# -*- coding: utf-8 -*-

##Make a bland book exciting by upping the sentiment! 
##
##Run this on the command line like so:
##python textillating.py [filename you want to use.txt]
##Must be plain text .txt file for now
##Output will be extremely_[filename].txt

import sys
from random import randint
from nltk.corpus import wordnet as wn
from nltk import word_tokenize as tok
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk import pos_tag as pos
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordfilter import Wordfilter 

#Sometimes wordnet is inappropriate and not in a funny way
wf = Wordfilter() #https://github.com/dariusk/wordfilter
ignore = ['other','several','own','queer','fucking','first','second','third','next','same','few','such']

detok = TreebankWordDetokenizer()
sid = SentimentIntensityAnalyzer()

def main():
    """Amplifies the affect of a given text. Adverbs and adjectives are altered."""

    if len(sys.argv) == 2:
        f = sys.argv[1]
        if f[len(f)-4:] == '.txt':
            usefile = f #must be a .txt file
        else:
            usefile = 'great_expectations.txt'
            print("This script requires .txt files only. The file you\n\
            specified was not a .txt file. Instead, we'll use\n\
            Great Expectations as an example...")
    else:
        usefile = 'great_expectations.txt'
        print("You can define which .txt file to use like so: \n\
        python textillating.py [filename you want to use.txt]\n\
        You didn't specify a .txt file to use, so in the meantime,\n\
        we'll use Great Expectations as an example...")
    
    print('Processing... This may take a minute...')

    filename = open(usefile,'r')
    text = filename.readlines() #readlines in order to preserve line breaks
    filename.close()

    outfile = open('extremely_' + usefile,'w')

    raw_text = []
    new_text = []

    for line in text:   
        line = pos(tok(line)) #('excellent', 'JJ') 
        raw_text.append(line)
    
    modifiers = ['WAY','ABSOLUTELY','ACTUALLY','ACUTELY','ALMIGHTY','AMPLY',
    'ASSUREDLY','ASTONISHINGLY','AWFULLY','CATEGORICALLY','CERTAINLY',
    'CLEARLY','CONSIDERABLY','DECIDEDLY','DEEPLY','DRASTICALLY',
    'EMINENTLY','EMPHATICALLY','EXAGGERATEDLY','EXCEEDINGLY','EXCEPTIONALLY',
    'EXCESSIVELY','EXORBITANTLY','EXPLICITLY','EXTENSIVELY','EXTRAORDINARILY',
    'EXTREMELY','FOR REAL','GENUINELY','GREATLY','HIGHLY','HUGELY','IMMENSELY',
    'IMMODERATELY','INCREDIBLY','INDUBITABLY','INORDINATELY',
    'INTENSELY','LARGELY','LEGITIMATELY','LITERALLY','MARKEDLY','NOTABLY',
    'NOTICEABLY','OBVIOUSLY','OVERLY','PARTICULARLY','PLENTY','POSITIVELY',
    'POWERFULLY','PRODIGIOUSLY','PROFOUNDLY','PROHIBITIVELY',
    'QUITE','RADICALLY','REALLY','REAL','REMARKABLY','SEVERELY',
    'STRIKINGLY','SUBSTANTIALLY','SUPER','SUPERLATIVELY','SURPASSINGLY',
    'SURPRISINGLY','TERRIBLY','TERRIFICALLY','TOO','TOTALLY','TRULY','ULTRA','UNCOMMONLY',
    'UNDENIABLY','UNDOUBTEDLY','UNEQUIVOCALLY','UNMISTAKABLY','UNQUESTIONABLY',
    'UTTERLY','VASTLY','VERILY','VERY','VIOLENTLY','VITALLY','WONDERFULLY']

    for line in raw_text: #goes line by line to preserve line breaks
        for word in line:
            word_score = sid.polarity_scores(word[0])['compound']
            use_synonym = word[0] #updates later
            possible_synonyms = []
            if wf.blacklisted(word[0]):
                pass
            elif word[0].lower() in ignore:
                pass
            elif word[1] == 'JJ': #adjectives only; adverbs don't quite work well here
                for syn in wn.synsets(word[0]):
                    for lemma in syn.lemmas():
                        syn_meta = str(syn).split('.') #match part of speech
                        if syn_meta[1] == 'a' or 's': #adjectives
                            possible_synonyms.append(lemma.name())
                all_synonyms = set(possible_synonyms) #de-dupe
                for synonym in all_synonyms:
                    syn_score = sid.polarity_scores(synonym)['compound'] 
                        #scores range from -1 to 1, 1 being positive affect
                    if wf.blacklisted(synonym):
                        pass 
                    elif word_score == 0:
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
        new_text.append('\n') #preserve line breaks

    outfile.write(detok.detokenize(new_text))
    #Does not deal with quotation marks well. Adds a space before/after them

    outfile.close()

    print('All done! See extremely_' + usefile + ' for your newly exciting text.')

main()