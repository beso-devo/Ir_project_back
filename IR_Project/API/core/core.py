from flask import Flask, request, jsonify
from flask import Blueprint, render_template, session, abort
import IR_Project.services.documents.cos_similarity as cos_sim
import IR_Project.API.variables.lists as lists
import IR_Project.models.document_reference as document_reference
import IR_Project.utils.recall_precision as func_stuff
import IR_Project.models.query_cacm as query_ca_cm

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


@app.route('/get_document_references_ci_si_dataset', methods=['GET'])
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
    # if not lists.results_ci:
    #     # lists.queries_ci = lists.ci_query.parse_ci_si_query_all()
    #     lists.results_ci = lists.ci_result.parse_ci_result_file()
    #
    # for query in lists.queries_ci:
    #     list_ids = []
    #     for res in lists.results_ci:
    #         if res[0] == query.query_id:
    #             list_ids.append(res[1])
    #     query.documents_relevant = list_ids
    #     # print("query_id =", query.query_id, " ", "lists_ids = ", list_ids)

    for i in range(55):
        print("--------> i = ", i)
        results = get_first_ten_ci_docs(lists.queries_ci[i])
        retrieved_docs = count_relevant_documents(results, lists.queries_ci[i])
        lists.queries_ci[i].query_precision = func_stuff.precision(retrieved_docs, 500)
        if retrieved_docs == 0 or len(lists.queries_ci[i].documents_relevant) == 0:
            lists.queries_ci[i].query_re_call = 0.0
        else:
            lists.queries_ci[i].query_re_call = func_stuff.recall(retrieved_docs,
                                                                  len(lists.queries_ci[i].documents_relevant))

    result = []
    for query in lists.queries_ci:
        result.append(query.to_json())

    return jsonify({
        "queries": result,
        "count": len(result),
        "MAP": get_mean_average_precision_ci(result),
        "MRR": get_mean_reciprocal_rank_ci(result),
    })


def get_first_ten_ci_docs(query):
    docs = []
    # query.display()
    for i in range(1459):
        cos_sim_value = 0.0
        # cos_sim_value = cos_sim.enhanced_cosine_sim(
        #     lists.documents_ci[i].tf_idf_for_whole_document, query.tf_idf_for_whole_query
        # )

        cos_sim_value = cos_sim.cosine_sim(
            lists.documents_ci[i].words, query.query_text
        )
        if cos_sim_value != 0.0:
            lists.documents_ci[i].set_tf_idf(
                cos_sim_value
            )
            docs.append(lists.documents_ci[i])

    if len(docs) > 500:
        return docs[0:500]
    return docs


@app.route('/get_recall_precision_ca_cm', methods=['GET'])
def get_recall_precision_ca_cm():
    for i in range(63):
        results = get_first_ten_ca_cm_docs(lists.queries_ca_cm[i])
        retrieved_docs = count_relevant_documents(results, lists.queries_ca_cm[i])
        lists.queries_ca_cm[i].query_precision = func_stuff.precision(retrieved_docs, 500)
        if retrieved_docs == 0 or len(lists.queries_ca_cm[i].documents_relevant) == 0:
            lists.queries_ca_cm[i].query_re_call = 0.0
        else:
            lists.queries_ca_cm[i].query_re_call = func_stuff.recall(retrieved_docs,
                                                                     len(lists.queries_ca_cm[i].documents_relevant))
        print("result = ", len(results), "retrieved_docs = ", retrieved_docs, "lists.queries_ca_cm[i] = ",
              query_ca_cm.QueryCaCm.display(lists.queries_ca_cm[i]),
              "results_ids = ", get_ids(results))
        print("____________________________________________________")

    result = []
    for query in lists.queries_ca_cm:
        result.append(query.to_json())

    return jsonify({
        "queries": result,
        "count": len(result),
        "MAP": get_mean_average_precision_ca_cm(result),
        "MRR": get_mean_reciprocal_rank_ca_cm(result),
    })


def get_first_ten_ca_cm_docs(query):
    docs = []
    # query.display()
    for i in range(3203):
        cos_sim_value = 0.0
        if lists.documents_ca_cm[i].words != "" and query.query_text != "":
            cos_sim_value = cos_sim.cosine_sim(
                lists.documents_ca_cm[i].words, query.query_text
            )
        if cos_sim_value != 0.0:
            lists.documents_ca_cm[i].set_tf_idf(
                cos_sim_value
            )
            docs.append(lists.documents_ca_cm[i])

    if len(docs) > 500:
        return docs[0:500]
    return docs


def count_relevant_documents(results, query):
    counter = 0.0
    for document_relevant_id in query.documents_relevant:
        if check_document_in_relevant_list(document_relevant_id, results):
            counter = counter + 1
    return counter


def check_document_in_relevant_list(document_relevant_id, results):
    for result in results:
        if result.document_id == document_relevant_id:
            return True
    return False


def get_mean_average_precision_ci(result):
    total = 0.0
    counter = 0
    for i in range(56):
        if lists.queries_ci[i].query_precision != -1.0:
            total = total + lists.queries_ci[i].query_precision
            counter = counter + 1
    if total == 0 or counter == 0:
        return 0.0
    return total / counter


def get_mean_reciprocal_rank_ci(result):
    total = 0.0
    counter = 0
    for i in range(56):
        if lists.queries_ci[i].query_re_call != -1.0:
            total = total + lists.queries_ci[i].query_re_call
            counter = counter + 1
    if total == 0 or counter == 0:
        return 0.0
    return total / counter


def get_mean_average_precision_ca_cm(result):
    total = 0.0
    counter = 0
    for i in range(56):
        if lists.queries_ca_cm[i].query_precision != -1.0:
            total = total + lists.queries_ca_cm[i].query_precision
            counter = counter + 1
    if total == 0 or counter == 0:
        return 0.0
    return total / counter


def get_mean_reciprocal_rank_ca_cm(result):
    total = 0.0
    counter = 0
    for i in range(56):
        if lists.queries_ca_cm[i].query_re_call != -1.0:
            total = total + lists.queries_ca_cm[i].query_re_call
            counter = counter + 1
    if total == 0 or counter == 0:
        return 0.0
    return total / counter


def get_ids(results):
    ids = []
    for i in results:
        ids.append(i.document_id)
    return ids
