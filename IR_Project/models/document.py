class Document:
    document_id = -1
    title = ""
    author = ""
    words = ""
    tokens = []
    stemmed_list = []
    lemmas = []
    filtered_list = []

    def __init__(self, document_id, title, author, words, tokens, stemmed_list, lemmas, filtered_list):
        self.document_id = document_id
        self.title = title
        self.author = author
        self.words = words
        self.tokens = tokens
        self.stemmed_list = stemmed_list
        self.lemmas = lemmas
        self.filtered_list = filtered_list

    def set_tokens(self, tokens):
        self.tokens = tokens

    def set_stemmed_list(self, stemmed_list):
        self.stemmed_list = stemmed_list

    def set_lemmas_list(self, lemmas):
        self.lemmas = lemmas

    def set_filtered_list(self, filtered_list):
        self.filtered_list = filtered_list

    def get_words(self):
        return self.words

    def display(self):
        print("document_id = " + str(self.document_id))
        print("title = " + str(self.title))
        print("author = " + str(self.author))
        print("words = " + str(self.words))
        print("tokens = " + str(self.tokens))
        print("stemmed_list = " + str(self.stemmed_list))
        print("lemmas = " + str(self.lemmas))
        print("filtered_list = " + str(self.filtered_list))


