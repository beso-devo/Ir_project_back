from nltk import ngrams
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from flask import Flask, request, jsonify
from flask import Blueprint, render_template, session, abort
import IR_Project.services.documents.cos_similarity as cos_sim
import IR_Project.models.document as document

# import IR_Project.app as main_app_stuff
import IR_Project.API.variables.lists as lists

app = Blueprint('core', __name__)


@app.route('/test', methods=['GET'])
def test():
    return 'it works!'


@app.route('/search', methods=['GET'])
def search():
    query_parameters = request.args
    sentence = query_parameters['q']
    dataset_type = query_parameters['type']
    count = query_parameters['count']

    if dataset_type.strip() == "1":
        if int(count.strip()) > 1459:
            return jsonify({
                "error": "Out of index!",
                "code": 415
            })
        for i in range(int(count.strip())):
            cos_value = 0.0
            text = ""
            text = lists.documents_ci[i].words
            cos_value = cos_sim.cosine_sim(
                text, sentence
            )
            lists.documents_ci[i].set_tf_idf(
                cos_value
            )
            print(i, ": tf_idf = ", lists.documents_ci[i].tf_idf)
        lists.documents_ci.sort(key=lambda doc: doc.tf_idf, reverse=True)
        result = []
        for doc in lists.documents_ci:
            print("-------> tf_idf = ", doc.tf_idf)
            if doc.tf_idf != 0.0:
                result.append(doc.to_json())
        return jsonify({
            "docs": result
        })

    if dataset_type.strip() == "2":
        print("CACM")
    # print(len(lists.documents_ca_cm))
    return jsonify({
        "length": len(lists.documents_ca_cm)
    })
