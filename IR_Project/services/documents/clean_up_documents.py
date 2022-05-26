import IR_Project.utils.parser_ci as ci
import nltk
from nltk import ngrams
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import IR_Project.models.document as document


def set_tokens_to_documents_ci():
    documents = []
    documents = ci.parse_ci_all()
    # res = list(filter(None, documents))
    print(document.Document.display(documents[0]))
    for doc in documents:
        tokens = nltk.word_tokenize(doc.words)
        doc.set_tokens(tokens)
    ci.document.Document.display(documents[0])
    return documents


def get_lemmatization_tokens_ci():
    documents = set_tokens_to_documents_ci()
    # Stemming
    p_stemmer = PorterStemmer()
    for doc in documents:
        nltk_stemmed_list = []
        for word in doc.tokens:
            nltk_stemmed_list.append(p_stemmer.stem(word))
        doc.set_stemmed_list(nltk_stemmed_list)
        nltk_stemmed_list = []
    ci.document.Document.display(documents[0])

    # Lemmatization
    word_lemmatizer = WordNetLemmatizer()
    for doc in documents:
        lemmas_list = []
        for word in doc.stemmed_list:
            lemmas_list.append(word_lemmatizer.lemmatize(word))
        doc.set_lemmas_list(lemmas_list)
        lemmas_list = []
    ci.document.Document.display(documents[0])

    # Filter stopword
    nltk_stop_words = set(stopwords.words("english"))
    punctuations = "?:!.,;"

    for doc in documents:
        filtered_sentence = []
        for w in doc.lemmas:
            if w not in nltk_stop_words and w not in punctuations:
                filtered_sentence.append(w)
        doc.set_filtered_list(filtered_sentence)

    ci.document.Document.display(documents[0])

    # # Removing Punctuation
    # for doc in documents:
    #     for word in doc.filtered_list:
    #         if word in punctuations:
    #             doc.filtered_list.remove(word)
    #
    # ci.document.Document.display(documents[0])


get_lemmatization_tokens_ci()
