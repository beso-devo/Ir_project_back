from sklearn.cluster import KMeans
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

import IR_Project.API.variables.lists as lists

cluster = {"0.0": [], "0.25": [], "0.50": [], "0.75": []}


def distribute_documents():
    kmeans = KMeans(n_clusters=4)
    vectorizer_cv = CountVectorizer(analyzer='word')
    X_cv = vectorizer_cv.fit_transform(get_documents_words(lists.documents_ci))  #  [ 'dddd'  , 'ddd'  ]
    kmeans.fit(X_cv)

    result = pd.concat(["CISI", pd.DataFrame(X_cv.toarray(), columns=vectorizer_cv.get_feature_names())], axis=1)
    result['cluster'] = kmeans.predict(X_cv)
    print("result = ", result)


def get_documents_words(docs):
    result = []
    for doc in docs:
        result.append(doc.words)
    return result


distribute_documents()