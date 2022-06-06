import IR_Project.models.query_cacm as query_cacm
import IR_Project.API.variables.lists as lists
import IR_Project.utils.results.result_ca_cm_parser as ca_cm_result


def parse_ca_cm_query_all():
    print("Now parse_ci_si_query_all...")
    queries_objects = []
    ca_cm_file_all = open("H:\PyCharm Projects\FirstOne\datasets\cacm\query.txt", "r")
    content = ca_cm_file_all.read()
    queries = content.split(".I ")
    for query in queries:
        # print("------->")
        doc_obj = get_query_from_ca_cm_text(query)
        if doc_obj is not None:
            queries_objects.append(doc_obj)
    lists.results_ca_cm = ca_cm_result.parse_ca_cm_result_file()

    for query in queries_objects:
        list_ids = []
        for res in lists.results_ca_cm:
            if res[0] == query.query_id:
                list_ids.append(res[1])
        query.documents_relevant = list_ids
    # print(query_cacm.QueryCaCm.display(queries_objects[0]))
    ca_cm_file_all.close()
    return queries_objects


def get_query_from_ca_cm_text(query_str):
    if query_str != "":
        # print(query_str)
        query = query_cacm.QueryCaCm(
            int(query_str.splitlines()[0]),
            find_between(query_str, ".W", ".N").strip(),
            get_relevant_document_from_result_file(int(query_str.splitlines()[0])),
            -1.0,
            -1.0
        )
        # query_cacm.QueryCaCm.display(query)
        return query


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def get_relevant_document_from_result_file(query_id):
    return []


parse_ca_cm_query_all()
