# Textillating

This is my little project for NaNoGenMo (National Novel Generation Month) 2018.

## About 

Ever wished the novel you were reading was way more exciting? Try Textillating it! 

The user inputs a .txt file (like a novel), and the script outputs a modified version of the file wherein most adjectives have been replaced by their most extreme synonyms. In other words, the affect has been amped up. 

For example, here's a paragraph from *Great Expectations*, as it is originally written:

>"Yes; but my dear Handel," Herbert went on, as if we had been talking, instead of silent, "its having been so strongly rooted in the breast of a boy whom nature and circumstances made so romantic, renders it very serious. Think of her bringing-up, and think of Miss Havisham. Think of what she is herself (now I am repulsive and you abominate me). This may lead to miserable things."  "I know it, Herbert," said I, with my head still turned away, "but I can't help it."  "You can't detach yourself?"  "No. Impossible!"  "You can't try, Handel?"  "No. Impossible!"

And here's the same paragraph after being run through textillating.py:

> "Yes; but my LOVE Handel," Herbert went on, as if we had been talking, instead of silent, "its having been so strongly rooted in the breast of a boy whom nature and circumstances made so ROMANTICIST, renders it very DANGEROUS! Think of her bringing-up, and think of Miss Havisham! Think of what she is herself (now I am EMINENTLY REPULSIVE and you abominate me)! This may lead to PATHETIC things!" "I know it, Herbert," said I, with my head still turned away, "but I can't help it!" "You can't detach yourself??!!" "No! SEVERELY IMPOSSIBLE!!!!!!!!!!!!!" "You can't try, Handel??!!" "No! ASTONISHINGLY IMPOSSIBLE!!!!!!!!!!!!!"

This project uses the [VADER sentiment analysis](http://www.nltk.org/howto/sentiment.html) tools and [WordNet](http://www.nltk.org/howto/wordnet.html) from NLTK (Natural Language Tool Kit). The SentimentIntensityAnalyzer quantifies how affective a word (or sentence) is, and WordNet finds a replacement. Here's what those scores look like:

Word | Sentiment polarity score 
--- | ---
awesome | 0.6249
good | 0.4404
fine | 0.2023
terrible | -0.4767
abhorrent | -0.6249

When Textillating encounters an adjective, it finds its sentiment polarity score, then checks for any synonyms from WordNet that have more extreme scores. So *fine* might be replaced by *awesome*, and *terrible* might be replaced by *abhorrent*. 

If there the sentiment polarity score is 0, or if there are no viable synonyms, the adjective is modified by an additional adverb, for instance: *necessary* might be replaced by *intensely necessary.* 

All replaced words are output in all caps. Some simple punctuation changes are also implemented.

## How to use

To use Textillating, run in on the command line like so:

`python textillating.py [filename you want to use.txt]`

You'll need to `pip install nltk` and `pip install wordfilter` if you don't already have those.

Textillating needs a plain text .txt file. You can find lots of boring classic novels on [Project Gutenberg](http://www.gutenberg.org).

I have included an example of a novel that I found so boring I did not finish it. (Sorry, 10th grade English teacher!) If there's a filename issue, it will use *Great Expectations* instead. 

## Issues 

The de-tokenizer currently has no idea what to do with quotation marks, so the output looks quite wonky.

## See also 

I became interested in this in the course of working on my [Nondescript project](https://github.com/robincamille/nondescript), which guides a user in changing their writing "style" is it is computed by stylometric analyses. The 2010 paper "[Automatic Synonym and Phrase Replacement Show Promise for Style Transformation](https://ieeexplore.ieee.org/document/5708976)" (Khosmood and Levinson) used WordNet and ranked possible synonyms by statistical popularity. It got me thinking about other ways to rank synonyms, like by affect! 

