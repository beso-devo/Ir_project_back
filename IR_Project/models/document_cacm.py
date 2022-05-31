class DocumentCaCm:
    document_id = -1
    title = ""
    words = ""
    production_date = ""
    author = ""
    printing_date = ""
    references_text = ""
    references_list = []
    reference_rank = -1
    tf_idf = 0.0

    def __init__(self, document_id, title, words, production_date, author, printing_date, references_text,
                 references_list,
                 reference_rank, tf_idf):
        self.document_id = document_id
        self.title = title
        self.words = words
        self.production_date = production_date
        self.author = author
        self.printing_date = printing_date
        self.references_text = references_text
        self.references_list = references_list
        self.reference_rank = reference_rank
        self.tf_idf = tf_idf

    def set_tf_idf(self, tf_idf):
        self.tf_idf = tf_idf

    def to_json(self):
        return {
            'document_id': self.document_id,
            'title': self.title,
            'author': self.author,
            'text': self.words,
            'tf_idf': self.tf_idf,
            'production_date': self.production_date,
            'printing_date': self.printing_date,
            'reference_rank': self.reference_rank
        }

    def display(self):
        print("document_id = " + str(self.document_id))
        print("words = " + str(self.words))
        print("title = " + str(self.title))
        print("production_date = " + str(self.production_date))
        print("author = " + str(self.author))
        print("printing_date = " + str(self.printing_date))
        print("references_text = " + str(self.references_text))
        print("references_list = " + str(self.references_list))
        print("reference_rank = " + str(self.reference_rank))
