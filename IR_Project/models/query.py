class Query:
    query_id = -1
    query_text = ""

    documents_relevant = []

    def __init__(self, query_id, query_text, documents_relevant):
        self.query_id = query_id
        self.query_text = query_text
        self.documents_relevant = documents_relevant

    def display(self):
        print("query_id = " + str(self.query_id))
        print("query_text = " + str(self.query_text))
        print("documents_relevant = " + str(self.documents_relevant))
