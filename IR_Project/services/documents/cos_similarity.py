import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import dot
from numpy.linalg import norm
from scipy import spatial

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    # print("tfidf = ", tfidf)
    return (tfidf * tfidf.T).A[0, 1]


def enhanced_cosine_sim(a, b):
    print("a = ", a)
    print("b = ", b)
    dataSetI = [3, 45, 7, 2]
    dataSetII = [2, 54, 13, 15]
    result = 1 - spatial.distance.cosine(b, b)
    return result


print(cosine_sim("How to install python on widows", "python on windows ois very useful"))
print(cosine_sim("""The present study is a history of the DEWEY Decimal
                Classification.  The first edition of the DDC was published
                in 1876, the eighteenth edition in 1971, and future editions
                will continue to appear as needed.  In spite of the DDC's
                long and healthy life, however, its full story has never
                been told.  There have been biographies of Dewey
                that briefly describe his system, but this is the first
                attempt to provide a detailed history of the work that
                more than any other has spurred the growth of
                librarianship in this country and abroad.""", "what is the history of decimal"))
