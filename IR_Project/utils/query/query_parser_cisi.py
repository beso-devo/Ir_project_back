import IR_Project.models.query as query_cisi


def parse_ci_si_query_all():
    print("Now parse_ci_si_query_all...")
    documents_objects = []
    ci_file_all = open("H:\PyCharm Projects\FirstOne\datasets\cisi.txt", "r")
    content = ci_file_all.read()
    documents = content.split(".I ")
    for doc in documents:
        # print("------->")
        doc_obj = get_query_from_ci_text(doc)
        if doc_obj is not None:
            documents_objects.append(doc_obj)

    # print(documents_objects)
    ci_file_all.close()
    return documents_objects


def get_query_from_ci_text(query_str):
    if query_str != "":
        # print(query_str)
        doc = query_cisi.Query(
            int(query_str.splitlines()[0]),
            get_from_to_last(query_str, ".W").strip(),
            get_relevant_document_from_result_file(int(query_str.splitlines()[0]))
        )
        # query_cisi.Query.display(doc)
        return doc


def get_from_to_last(s, from_str):
    try:
        start = s.index(from_str) + len(from_str)
        return s[start:]
    except ValueError:
        return ""


def get_relevant_document_from_result_file(query_id):
    return []


# parse_ci_si_query_all()
