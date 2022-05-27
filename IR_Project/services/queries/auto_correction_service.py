import pandas as pandas
from nltk import jaccard_distance, ngrams
from nltk.corpus import words
import nltk
from textblob import TextBlob


def correct_sentence_spelling(sentence):
    sentence = TextBlob(sentence)

    result = sentence.correct()

    print(result)


def auto_correcting_query():
    incorrect_words = nltk.word_tokenize("how to extract irreguslar verbs with nltk pythoon")
    # incorrect_words = ['happpy', 'azmaing', 'intelliengt']
    correct_words = words.words()
    outcomes = []
    for word in incorrect_words:
        temp = [(jaccard_distance(set(ngrams(word, 2)),
                                  set(ngrams(w, 2))), w)
                for w in correct_words if w[0] == word[0]]
        outcomes.append(sorted(temp, key=lambda val: val[0])[0][1])

    result = ""
    for i in outcomes:
        result = result + i + " "
    print("outcomes: ", outcomes)
    print("result: ", result)


auto_correcting_query()
