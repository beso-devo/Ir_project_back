def recall(number_documents_retrieved, total_documents_relevant):
    return number_documents_retrieved / total_documents_relevant


def precision(number_documents_retrieved, total_documents_retrieved):
    return number_documents_retrieved / total_documents_retrieved


def mean_avg_precision(list_of_precision):
    result = 0.0
    for p in list_of_precision:
        result += p
    return result


def reciprocal_rank(rank):
    return 1 / rank


def mean_reciprocal_rank(list_of_rr):
    result = 0.0
    for r in list_of_rr:
        result += r
    return result


def f_score(precision_val, re_call_val):
    return (2 * precision_val * re_call_val) / (precision_val + re_call_val)
