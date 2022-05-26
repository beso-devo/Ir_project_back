class Document:
    document_id = -1
    title = ""
    author = ""
    words = ""

    def __init__(self, document_id, title, author, words):
        self.document_id = document_id
        self.title = title
        self.author = author
        self.words = words

    def display(self):
        print("document_id = " + str(self.document_id))
        print("title = " + str(self.title))
        print("author = " + str(self.author))
        print("words = " + str(self.words))
