class DocumentCaCm:
    document_id = -1
    title = ""
    production_date = ""
    author = ""
    printing_date = ""
    references = ""
    tf_idf = 0.0

    def __init__(self, document_id, title, production_date, author, printing_date, references, tf_idf):
        self.document_id = document_id
        self.title = title
        self.production_date = production_date
        self.author = author
        self.printing_date = printing_date
        self.references = references
        self.tf_idf = tf_idf

    def set_tf_idf(self, tf_idf):
        self.tf_idf = tf_idf

    def display(self):
        print("document_id = " + str(self.document_id))
        print("title = " + str(self.title))
        print("production_date = " + str(self.production_date))
        print("author = " + str(self.author))
        print("printing_date = " + str(self.printing_date))
        print("references = " + str(self.references))
