class Query:
    query_id = -1
    query_text = ""
    query_re_call = -1.0
    query_precision = -1.0

    documents_relevant = []

    def __init__(self, query_id, query_text, documents_relevant, query_re_call, query_precision):
        self.query_id = query_id
        self.query_text = query_text
        self.documents_relevant = documents_relevant
        self.query_re_call = query_re_call
        self.query_precision = query_precision

    def to_json(self):
        return {
            'query_id': self.query_id,
            'query_text': self.query_text,
            'query_re_call': self.query_re_call,
            'query_precision': self.query_precision,
            'documents_relevant': self.documents_relevant
        }

    def display(self):
        print("query_id = " + str(self.query_id))
        print("query_text = " + str(self.query_text))
        print("documents_relevant = " + str(self.documents_relevant))
        print("query_re_call = " + str(self.query_re_call))
        print("query_precision = " + str(self.query_precision))
