import IR_Project.models.query as query_cisi


def parse_ci_si_query_all():
    print("Now parse_ci_si_query_all...")
    documents_objects = []
    ci_file_all = open("H:\PyCharm Projects\FirstOne\datasets\cisi.txt", "r")
    content = ci_file_all.read()
    documents = content.split(".I ")
    for doc in documents:
        # print("------->")
        doc_obj = get_document_from_ci_text(doc)
        if doc_obj is not None:
            documents_objects.append(doc_obj)

    print(documents_objects)
    ci_file_all.close()
    return documents_objects


def get_document_from_ci_text(document_str):
    if document_str != "":
        print(document_str)
        doc = query_cisi.Query(
            int(document_str.splitlines()[0]),
            get_from_to_last(document_str, ".W").strip(),
        )
        # query_cisi.Query.display(doc)
        return doc


def get_from_to_last(s, from_str):
    try:
        start = s.index(from_str) + len(from_str)
        return s[start:]
    except ValueError:
        return ""


parse_ci_si_query_all()
