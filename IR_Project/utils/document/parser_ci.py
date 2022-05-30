import IR_Project.models.document as document
import re


# cos similarity

def parse_ci_all():
    print("Now parse_ci_all...")
    documents_objects = []
    ci_file_all = open("H:\PyCharm Projects\FirstOne\datasets\CISI\CISI.txt", "r")
    content = ci_file_all.read()
    documents = content.split(".I ")
    for doc in documents:
        # print("------->")
        doc_obj = get_document_from_ci_text(doc)
        if doc_obj is not None:
            documents_objects.append(doc_obj)
    ci_file_all.close()
    print("----> length = ", len(documents_objects))
    return documents_objects


def get_document_from_ci_text(document_str):
    if document_str != "":
        doc = document.Document(
            int(document_str.splitlines()[0]),
            find_between(document_str, ".T", ".A").strip(),
            find_between(document_str, ".A", ".W").strip(),
            find_between(document_str, ".W", ".X").strip(),
            get_from_to_last(document_str, ".X"),
            [],
            -1,
            [],
            [],
            [],
            [],
            0.0
        )
        for line in doc.references_text.strip().splitlines():
            doc.references_list.append(convert_list_string_to_int(re.split('\s+', line)))
        # document.Document.display(doc)
        return doc


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def get_from_to_last(s, from_str):
    try:
        start = s.index(from_str) + len(from_str)
        return s[start:]
    except ValueError:
        return ""


def convert_list_string_to_int(list_test):
    list_test = list_test[:-1]
    for i in range(0, len(list_test)):
        list_test[i] = int(list_test[i])
    return list_test


parse_ci_all()
