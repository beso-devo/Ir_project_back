import spacy

from spacy.lang.en import English
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
import random
import IR_Project.API.variables.lists as lists
from gensim import corpora
import pickle
import gensim

parser = English()
text_data = []


def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


def prepare_text_for_lda(text):
    en_stop = set(nltk.corpus.stopwords.words('english'))
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens


def parse_data():
    for i in range(5):
        tokens = prepare_text_for_lda(lists.documents_ci[i].words)
        print(tokens)
        text_data.append(tokens)
        ask_lda_to_fetch_results(text_data)


# sounds like a topic related to database.
def ask_lda_to_fetch_results(data):
    dictionary = corpora.Dictionary(data)
    corpus = [dictionary.doc2bow(text) for text in data]
    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')

    NUM_TOPICS = 3  # 10
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)  # 15
    ldamodel.save('model5.gensim')
    topics = ldamodel.print_topics(num_words=5)  # 4
    for topic in topics:
        print(topic)
    print("-------- end of fetching --------")


def search_query_in_topics():
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')
    NUM_TOPICS = 1
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
    ldamodel.save('model5.gensim')
    new_doc = 'Practical Bayesian Optimization of Machine Learning Algorithms'
    new_doc = prepare_text_for_lda(new_doc)
    new_doc_bow = dictionary.doc2bow(new_doc)
    print(new_doc_bow)
    print(ldamodel.get_document_topics(new_doc_bow)[0])
    print("-------- end of search --------")


parse_data()
# ask_lda_to_fetch_results()
# search_query_in_topics()
