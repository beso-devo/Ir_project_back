from flask import Flask, request, jsonify
from flask import Blueprint, render_template, session, abort
import IR_Project.services.documents.cos_similarity as cos_sim
import IR_Project.API.variables.lists as lists
import IR_Project.models.document_reference as document_reference
import IR_Project.models.document_cacm as document_ca_cm

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
            lists.documents_ci[i].set_tf_idf(
                cos_sim.cosine_sim(
                    lists.documents_ci[i].words, sentence
                )
            )
        lists.documents_ci.sort(key=lambda doc: doc.tf_idf, reverse=True)
        result = []
        for doc in lists.documents_ci:
            if doc.tf_idf != 0.0:
                result.append(doc.to_json())

        return jsonify({
            "docs": result,
            "count": len(result)
        })

    if dataset_type.strip() == "2":
        if int(count.strip()) > 3204:
            return jsonify({
                "error": "Out of index!",
                "code": 415
            })
        for i in range(int(count.strip())):
            lists.documents_ca_cm[i].set_tf_idf(
                cos_sim.cosine_sim(
                    get_text_or_title(lists.documents_ca_cm[i]), sentence
                )
            )
        lists.documents_ca_cm.sort(key=lambda doc: doc.tf_idf, reverse=True)
        result = []
        for doc in lists.documents_ca_cm:
            if doc.tf_idf != 0.0:
                result.append(doc.to_json())

        return jsonify({
            "docs": result,
            "count": len(result)
        })

    return jsonify({
        "error": "No dataset with this type (" + dataset_type + ")!",
        "code": 404
    })


def get_text_or_title(doc):
    if doc.words == "":
        return doc.title
    return doc.words


@app.route('/get_document_references_ca_cm_dataset', methods=['GET'])
def get_document_references_ca_cm_dataset():
    query_parameters = request.args
    document_id = query_parameters['document_id']
    list_of_references_for_this_doc = []
    for docum in lists.documents_ca_cm:
        if int(docum.document_id) == int(document_id.strip()):
            list_of_references_for_this_doc = docum.references_list
            break

    print("----> list_of_references_for_this_doc= ", list_of_references_for_this_doc)
    references = []

    for doc in lists.documents_ca_cm:
        for r in list_of_references_for_this_doc:
            if r[0] == doc.document_id and doc not in references:
                doc.reference_rank = r[1]
                doc_reference = document_reference.DocumentReference(
                    r[1],
                    doc
                )
                if r[0] != int(document_id.strip()):
                    references.append(doc_reference)

    references.sort(key=lambda doc: doc.rank, reverse=True)

    result = []
    for doc in references:
        result.append(doc.document.to_json())

    return jsonify({
        "docs": result,
        "count": len(result)
    })


@app.route('/get_document_references', methods=['GET'])
def get_document_references_ci_si_dataset():
    query_parameters = request.args
    document_id = query_parameters['document_id']
    list_of_references_for_this_doc = []
    for docum in lists.documents_ci:
        if int(docum.document_id) == int(document_id.strip()):
            list_of_references_for_this_doc = docum.references_list
            break

    references = []

    for doc in lists.documents_ci:
        for r in list_of_references_for_this_doc:
            if r[0] == doc.document_id and doc not in references:
                doc.reference_rank = r[1]
                doc_reference = document_reference.DocumentReference(
                    r[1],
                    doc
                )
                if r[0] != int(document_id.strip()):
                    references.append(doc_reference)

    references.sort(key=lambda doc: doc.rank, reverse=True)

    result = []
    for doc in references:
        result.append(doc.document.to_json())

    return jsonify({
        "docs": result,
        "count": len(result)
    })


@app.route('/get_recall_precision_ci', methods=['GET'])
def get_recall_precision_ci():
    if not lists.results_ci:
        # lists.queries_ci = lists.ci_query.parse_ci_si_query_all()
        lists.results_ci = lists.ci_result.parse_ci_result_file()

    for query in lists.queries_ci:
        list_ids = []
        for res in lists.results_ci:
            if res[0] == query.query_id:
                list_ids.append(res[1])
        query.documents_relevant = list_ids
        # print("query_id =", query.query_id, " ", "lists_ids = ", list_ids)
        list_ids = []

    return jsonify({
        "docs": [],
        "count": 0
    })
