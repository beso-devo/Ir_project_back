class Query:
    query_id = -1
    query_text = ""

    def __init__(self, query_id, query_text):
        self.query_id = query_id
        self.query_text = query_text

    def display(self):
        print("query_id = " + str(self.query_id))
        print("query_text = " + str(self.query_text))
