class DocumentReference:
    rank = -1
    document = None

    def __init__(self, rank, document):
        self.rank = rank
        self.document = document
