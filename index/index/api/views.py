"""REST API for available directories."""
import flask
import index
import numpy as np
from collections import Counter
from math import sqrt
from index.api.utils import *

@index.app.route("/api/v1/", methods=["GET"])
def get_dir():
    context = {"hits": "/api/v1/hits/", "url": "/api/v1/"}
    return flask.jsonify(**context)

@index.app.route("/api/v1/hits/", methods=["GET"])
def get_hits():
    weight = flask.request.args.get('w')
    query = flask.request.args.get('q')
    print("weight: ", weight)
    print("query: ", query)
    context = {"hits": []}
    queries = [ "".join(filter(str.isalnum, word)) for word in query.split(" ") if word not in stopwords]
    print(queries)
    print(inverted_index['armadillo'])
    counts = Counter(queries)
    q_vec = []
    s = None # doc_ids that contain all words in queries
    q_unique = list(counts.keys()) # unique words in queries
    for word in q_unique:
        if word in inverted_index:
            if not s:
                s = set(inverted_index[word][1].keys())
            else:
                s = s.intersection(inverted_index[word][1].keys())
            if not s:
                return flask.jsonify({"hits": []})
            else:
                tfq = float(counts[word])
                idf = float(inverted_index[word][0])
                q_vec.append(tfq*idf)
        else:
            return flask.jsonify({"hits": []})
    squared_sum = sum([x**2 for x in q_vec])
    norm_q = sqrt(squared_sum)
    tmp = [] #(weighted_score * -1, doc_id)
    for doc in s:
        d_vec = []
        norm_d = None
        for word in q_unique:
            tfd = float(inverted_index[word][1][doc][0])
            idf = float(inverted_index[word][0])
            d_vec.append(tfd*idf)
            if not norm_d:
                norm_d_squared = float(inverted_index[word][1][doc][1])
                norm_d = sqrt(norm_d_squared)
        tfidf = np.dot(q_vec, d_vec) / (norm_q * norm_d)
        weighted_score = float(weight) * float(pagerank[doc]) + (1 - float(weight)) * tfidf
        tmp.append((-1*weighted_score, doc))
    tmp.sort()
    for data in tmp:
        context["hits"].append({"docid": int(data[1]), "score": (data[0] * -1)})
    return flask.jsonify(**context)
