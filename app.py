import math

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


@app.route('/')
def index():
    return "Welcome to our first API"


@app.route('/get_sentence_tokens', methods=['GET'])
def get_sentence_tokens():
    print(request.args)
    query_parameters = request.args
    sentence = query_parameters['q']
    tokens = []
    json_obj = {}
    data = []
    sentence_tokens = nltk.sent_tokenize(sentence)
    for sent in sentence_tokens:
        tokens = []
        tokens = nltk.word_tokenize(sent)
        json_obj[sent] = tokens
        data.append({'sentence': sent, 'tokens': json_obj[sent]})
    return jsonify({
        "sentence_tokens": data
    })


@app.route('/get_tokens', methods=['GET'])
def get_tokens():
    print(request.args)
    query_parameters = request.args
    sentence = query_parameters['q']
    tokens = nltk.word_tokenize(sentence)
    return jsonify({
        "tokens": tokens
    })


@app.route('/get_lowercase_tokens', methods=['GET'])
def get_lowercase_tokens():
    print(request.args)
    query_parameters = request.args
    sentence = query_parameters['q']
    tokens = nltk.word_tokenize(sentence)
    lowercase_tokens = list(map(lambda x: x.lower(), tokens))
    return jsonify({
        "lowercase_tokens": lowercase_tokens
    })


@app.route('/get_stemming_tokens', methods=['GET'])
def get_stemming_tokens():
    print(request.args)
    query_parameters = request.args
    sentence = query_parameters['q']
    stemmer = PorterStemmer()
    tokens = word_tokenize(sentence)
    stemming_list = []
    for word in tokens:
        stemming_list.append(stemmer.stem(word))

    return jsonify({
        "stemming_tokens": stemming_list
    })


@app.route('/get_lemmatization_tokens', methods=['GET'])
def get_lemmatization_tokens():
    query_parameters = request.args
    sentence = query_parameters['q']
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

    return jsonify({
        "lemmatization_tokens": {
            "sentence": sentence,
            "lemmas": filtered_sentence
        }
    })


@app.route('/get_part_of_speech_tokens', methods=['GET'])
def get_part_of_speech_tokens():
    query_parameters = request.args
    sentence = query_parameters['q']
    stop_words = set(stopwords.words('english'))
    sentence_tokens = nltk.sent_tokenize(sentence)
    list_of_list = []
    json_obj = {}
    for i in sentence_tokens:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
        list_of_list.append({'sentence': i, 'pos': tagged})
        print(tagged)

    return jsonify({
        "part_of_speech_tokens": list_of_list
    })


@app.route('/get_data_parsing_tokens', methods=['GET'])
def get_data_parsing_tokens():
    query_parameters = request.args
    sentence = query_parameters['q']
    n = query_parameters['ngram']
    print(n)
    print(sentence)
    list = []
    n_grams = ngrams(sentence.split(), int(n))
    for grams in n_grams:
        list.append(grams)
    return jsonify({
        "data_parsing_tokens": list
    })


@app.route('/get_tf_matrix', methods=['GET'])
def get_tf_matrix():
    query_parameters = request.args
    sentence = query_parameters['q']
    sentences = sent_tokenize(sentence)
    freq_matrix = tf_idf_stuff.create_frequency_matrix(sentences)
    tf_matrix = tf_idf_stuff.create_tf_matrix(freq_matrix)

    return jsonify({
        "tf_matrix": tf_matrix
    })


@app.route('/get_idf_matrix', methods=['GET'])
def get_idf_matrix():
    query_parameters = request.args
    sentence = query_parameters['q']
    sentences = sent_tokenize(sentence)
    total_documents = len(sentences)
    freq_matrix = tf_idf_stuff.create_frequency_matrix(sentences)
    count_doc_per_words = tf_idf_stuff.create_documents_per_words(freq_matrix)
    idf_matrix = tf_idf_stuff.create_idf_matrix(freq_matrix, count_doc_per_words, total_documents)



    return jsonify({
        "idf_matrix": idf_matrix
    })


@app.route('/get_tf_idf_matrix', methods=['GET'])
def get_tf_idf_matrix():
    query_parameters = request.args
    sentence = query_parameters['q']
    sentences = sent_tokenize(sentence)
    total_documents = len(sentences)
    freq_matrix = tf_idf_stuff.create_frequency_matrix(sentences)
    tf_matrix = tf_idf_stuff.create_tf_matrix(freq_matrix)
    count_doc_per_words = tf_idf_stuff.create_documents_per_words(freq_matrix)
    idf_matrix = tf_idf_stuff.create_idf_matrix(freq_matrix, count_doc_per_words, total_documents)
    tf_idf_matrix = tf_idf_stuff.create_tf_idf_matrix(tf_matrix, idf_matrix)

    return jsonify({
        "tf_idf_matrix": tf_idf_matrix
    })


if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.17')
