import IR_Project.models.document_cacm as document_ca_cm
import re


def parse_ca_cm_all():
    print("Now parse_ca_cm_all...")
    documents_objects = []
    ca_cm_file_all = open("H:\PyCharm Projects\FirstOne\datasets\cacm\cacm.txt", "r")
    content = ca_cm_file_all.read()
    documents = content.split(".I ")
    for doc in documents:
        # print("------->")
        documents_objects.append(get_document_from_ca_cm_text(doc))
    ca_cm_file_all.close()
    print("----> cacm length = ", len(documents_objects))
    return documents_objects


def get_document_from_ca_cm_text(document_str):
    if document_str != "":
        doc = document_ca_cm.DocumentCaCm(
            int(document_str.splitlines()[0]),
            find_between(document_str, ".T", ".B").strip(),
            find_between(document_str, ".B", ".A").strip(),
            find_between(document_str, ".A", ".N").strip(),
            find_between(document_str, ".N", ".X").strip(),
            get_from_to_last(document_str, ".X"),
            0.0
        )
        # document_ca_cm.DocumentCaCm.display(doc)
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

# parse_ca_cm_all()
