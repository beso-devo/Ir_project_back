import math

from nltk import word_tokenize

text = "This paper consists of  of many paper many paper of this paper"
text1 = "This paper consists  survey  many paper many paper  this paper"
text2 = "now we will do another thing"
docs = [text, text1, text2]
wholedocs = ""
for doc in docs:
    wholedocs += doc + " "
idfmatrix = dict.fromkeys(word_tokenize(wholedocs))
for term in idfmatrix.keys():
    counter = 0
    for key in range(len(docs)):
        if term in docs[key]:
            counter += 1
    idfmatrix.update({term: math.log(len(docs) / counter) + 1})

print(idfmatrix)