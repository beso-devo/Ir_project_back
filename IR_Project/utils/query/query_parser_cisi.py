import IR_Project.models.query as query_cisi
import IR_Project.API.variables.lists as lists
import IR_Project.utils.results.result_ci_parser as ci_result
import IR_Project.services.documents.calculate_tf_idf as calculate_tf_idf


def parse_ci_si_query_all():
    print("Now parse_ci_si_query_all...")
    queries_objects = []
    ci_file_all = open("H:\PyCharm Projects\FirstOne\datasets\cisi.txt", "r")
    content = ci_file_all.read()
    queries = content.split(".I ")
    for query in queries:
        # print("------->")
        query_obj = get_query_from_ci_text(query)
        if query_obj is not None:
            queries_objects.append(query_obj)
    lists.results_ci = ci_result.parse_ci_result_file()

    for query in queries_objects:
        list_ids = []
        for res in lists.results_ci:
            if res[0] == query.query_id:
                list_ids.append(res[1])
        query.documents_relevant = list_ids
    # print(query_cisi.Query.display(queries_objects[0]))
    ci_file_all.close()
    return queries_objects


def get_query_from_ci_text(query_str):
    if query_str != "":
        # print(query_str)
        query = query_cisi.Query(
            int(query_str.splitlines()[0]),
            get_from_to_last(query_str, ".W").strip(),
            get_relevant_document_from_result_file(int(query_str.splitlines()[0])),
            -1.0,
            -1.0,
            []
            # calculate_tf_idf.tf_idf(get_from_to_last(query_str, ".W").strip())
        )
        # query_cisi.Query.display(query)
        return query


def get_from_to_last(s, from_str):
    try:
        start = s.index(from_str) + len(from_str)
        return s[start:]
    except ValueError:
        return ""


def get_relevant_document_from_result_file(query_id):
    return []

parse_ci_si_query_all()
