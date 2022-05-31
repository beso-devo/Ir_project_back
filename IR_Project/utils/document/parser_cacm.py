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
        doc_obj = get_document_from_ca_cm_text(doc)
        if doc_obj is not None:
            documents_objects.append(doc_obj)
    ca_cm_file_all.close()
    print("----> cacm length = ", len(documents_objects))
    return documents_objects


def get_document_from_ca_cm_text(document_str):
    if document_str != "":
        doc = document_ca_cm.DocumentCaCm(
            int(document_str.splitlines()[0]),
            get_document_title(document_str),
            # find_between(document_str, ".W", ".B").strip(),
            get_document_words(document_str),
            # find_between(document_str, ".B", ".A").strip(),
            get_document_production_date(document_str),
            # find_between(document_str, ".A", ".N").strip(),
            get_document_authors(document_str),
            find_between(document_str, ".N", ".X").strip(),
            get_from_to_last(document_str, ".X"),
            [],
            -1,
            0.0
        )
        # document_ca_cm.DocumentCaCm.display(doc)
        for line in doc.references_text.strip().splitlines():
            doc.references_list.append(convert_list_string_to_int(re.split('\s+', line)))
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


def convert_list_string_to_int(list_test):
    list_test = list_test[:-1]
    for i in range(0, len(list_test)):
        list_test[i] = int(list_test[i])
    return list_test


def get_document_title(document_str):
    if find_between(document_str, ".T", ".W").strip() == "":
        return find_between(document_str, ".T", ".B")
    return find_between(document_str, ".T", ".W")


def get_document_words(document_str):
    if find_between(document_str, ".T", ".W").strip() == "":
        return ""
    return find_between(document_str, ".W", ".B")


def get_document_authors(document_str):
    if ".K" in find_between(document_str, ".A", ".N").strip() or ".C" in find_between(document_str, ".A", ".N").strip():
        if find_between(document_str, ".A", ".K").strip() == "":
            return find_between(document_str, ".A", ".C").strip()
        return find_between(document_str, ".A", ".K").strip()
    return find_between(document_str, ".A", ".N").strip()


def get_document_production_date(document_str):
    if ".K" in find_between(document_str, ".B", ".N") or ".C" in find_between(document_str, ".B", ".N"):
        if find_between(document_str, ".B", ".K").strip() == "":
            return find_between(document_str, ".B", ".C").strip()
        return find_between(document_str, ".B", ".K").strip()
    if find_between(document_str, ".B", ".A").strip() == "":
        return find_between(document_str, ".B", ".N").strip()
    return find_between(document_str, ".B", ".A").strip()


parse_ca_cm_all()
