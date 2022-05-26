from flask import Flask, request, jsonify
import nltk
from nltk import ngrams
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import stuff.tf_idf as tf_idf_stuff

app = Flask(__name__)


def clean_up_query(sentence):
    # query_parameters = request.args
    # sentence = query_parameters['q']
    tokens = nltk.word_tokenize(sentence)
    lowercase_tokens = list(map(lambda x: x.lower(), tokens))
    stemmer = PorterStemmer()
    stemming_list = []
    p_stemmer = PorterStemmer()
    for word in tokens:
        stemming_list.append(stemmer.stem(word))
    nltk_stemedList = []
    for word in tokens:
        nltk_stemedList.append(p_stemmer.stem(word))

    # Lemmatization
    word_lemmatizer = WordNetLemmatizer()
    lemmaList = []
    for word in nltk_stemedList:
        lemmaList.append(word_lemmatizer.lemmatize(word, 'v'))

    print("lemmaList: ", lemmaList)
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
    print("Filtered list: ", filtered_sentence)


clean_up_query("How to made a youtube video in youtube")
