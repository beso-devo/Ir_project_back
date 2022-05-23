# import nltk
# nltk.download()
from shlex import join

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

sentence = """How to install python on windows OS.
stuff dear.
"""

##############################

sentence_tokens = nltk.sent_tokenize(sentence)
print("Sentence-Tokens: ")
print(sentence_tokens)
print("")

##############################

tokens = nltk.word_tokenize(sentence)
print("Tokens: ")
print(tokens)
print("")

##############################

lowercase_tokens = list(map(lambda x: x.lower(), tokens))
print("LowerCase-Tokens: ")
print(lowercase_tokens)
print("")

##############################

porter = PorterStemmer()
lancaster = LancasterStemmer()

for word in lowercase_tokens:
    print("{0:20}{1:20}{2:20}".format(word, porter.stem(word), lancaster.stem(word)))

print("")


# porter_stem = porter.stem(join(word for word in lowercase_tokens))
# lancaster_stem = porter.stem(join(word for word in lowercase_tokens))
# print("Porter-Stemming: ")
# print(porter_stem)
# print("Lancaster-Stemming: ")
# print(lancaster_stem)


def stemSentence(sentence):
    stem_sentence = []
    for word in tokens:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


porter_stem = stemSentence(sentence)
print("Porter-Stemming: ")
print(porter_stem)
print("")

##############################

stop_words = set(stopwords.words('english'))
list_of_list = []
for i in sentence_tokens:
    wordsList = nltk.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words]
    tagged = nltk.pos_tag(wordsList)
    list_of_list.append(tagged)
    print(tagged)

print("\nAll parts of speech: ")
print(list_of_list)
print("")

##############################

p_stemmer = PorterStemmer()
tokens = word_tokenize(sentence)

# Stemming
nltk_stemedList = []
for word in tokens:
    nltk_stemedList.append(p_stemmer.stem(word))

# Lemmatization
word_lemmatizer = WordNetLemmatizer()
lemmaList = []
for word in nltk_stemedList:
    lemmaList.append(word_lemmatizer.lemmatize(word))

print("Stemming + Lemmatization")
print(lemmaList)
# Filter stopword
filtered_sentence = []
nltk_stop_words = set(stopwords.words("english"))
for w in lemmaList:
    if w not in nltk_stop_words:
        filtered_sentence.append(w)
# Removing Punctuation
punctuations = "?:!.,;"
for word in filtered_sentence:
    if word in punctuations:
        filtered_sentence.remove(word)
print(" ")
print("Remove stopword & Punctuation")
print(filtered_sentence)
