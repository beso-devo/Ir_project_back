from flask import Flask, request, jsonify
from nltk import ngrams
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from flask import Blueprint, render_template, session, abort

app = Blueprint('features', __name__)


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
