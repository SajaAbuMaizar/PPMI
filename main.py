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
corpus.close()

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
sortedTokenCounts = sorted(tokenCounts)

simlexFile = open('EN-SIMLEX-999.txt', 'r+', encoding="utf8")
simlexContent = simlexFile.read()  # reading all the data in the simlexFile file
simlexSplits = simlexContent.split(" ")  # dividing the data into the creators
simlexFile.close()

simlexWords = re.findall(r"[a-zA-Z]+", simlexContent)

rows = len(simlexWords) + 1
cols = 2 + 1  # change to 20,000

frequencyCountsWindow2Mat = [[0 for _ in range(cols)] for _ in range(rows)]

for col in range(3 - 1):  # -1 because of leaving the first cell empty
    frequencyCountsWindow2Mat[0][col + 1] = sortedTokenCounts[col]

for row in range(rows - 1):
    frequencyCountsWindow2Mat[row + 1][0] = simlexWords[row]

# frequency count window +/-2
for i, simWord in enumerate(simlexSplits):
    for j, sentence in enumerate(sentences):
        if simWord in sentence:
            sentence.index(simWord)
#    for j,frequentWord in enumerate(sortedTokenCounts[:2]): #change to 20000
#        for sentence in sentences:

#        if
            #frequencyCountsWindow2Mat[i][j]+=1

m = np.zeros([length,length]) # n is the count of all words
def cal_occ(sentence,m,window):
    for i,word in enumerate(sentence):
        for j in range(max(i-window,0),min(i+window,len(sentence))):
             m[word,sentence[j]]+=1
for sentence in X:
    cal_occ(sentence, m)


for row in frequencyCountsWindow2Mat:
    print(row)

# for word in simlexSplits:
#    if
#    simlexWords.append(re.match(r"^[0-9]+",word))

# bigram_measures = BigramAssocMeasures()
# finder = BigramCollocationFinder.from_words(word_tokenize(text))
# for i in finder.score_ngrams(bigram_measures.pmi):
#    print(i)
