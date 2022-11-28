import fileinput
import string
import sys
import re
from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')


def countTokens(par):
    counts = dict()
    list_of_words = par.split()

    for token in list_of_words:
        if token in counts:
            counts[token] += 1
        else:
            counts[token] = 1

    return counts


corpus = open('nlp.txt', 'r+', encoding="utf8")
content = corpus.read()  # reading all the data in the sql file
sentences = content.split("\n")  # dividing the data into the creators
# print(sentences)

for i, word in enumerate(sentences):
    word = re.sub(pattern=r"[^\w\s]", repl="", string=word)
    word = word.lower()
    word = re.sub(pattern=r"[^a-zA-Z0-9\s]+", repl="<UNK>", string=word)
    word = re.sub(pattern=r"[0-9]+", repl=" <!DIGIT!>", string=word)
    word = re.sub(pattern=r"\t", repl=" ", string=word)
    sentences[i] = '<S>' + word + ' </S>'

text = ""
for sentence in sentences:
    text += " " + sentence

tokenCounts = countTokens(text)
print(tokenCounts)



# bigram_measures = BigramAssocMeasures()
# finder = BigramCollocationFinder.from_words(word_tokenize(text))
# for i in finder.score_ngrams(bigram_measures.pmi):
#    print(i)
