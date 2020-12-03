"""REST API for available directories."""
import flask
import index
import re
import numpy as np
from collections import Counter

index_package_dir = pathlib.Path(__file__).parent.parent

stopwords_filename = index_package_dir/"stopwords.txt"
pagerank_filename = index_package_dir/"pagerank.out"
inverted_index_filename = index_package_dir/"inverted_index.txt"

stopwords = get_stopwords()
pagerank = get_pagerank()
inverted_index = get_inverted_index() #{term: [idf, {doc_id: [freq in doc, squared norm factor]}]}

@index.app.route("/api/v1/", methods=["GET"])
def get_dir():
    context = {"hits": "/api/v1/hits/", "url": "/api/v1/"}
    return flask.jsonify(**context)

@index.app.route("/api/v1/hits/", methods=["GET"])
def get_hits():
    weight = flask.request.args.get('w')
    query = flask.request.args.get('q')

    context = {"hits": []}
    queries = ["".join(filter(str.isalnum(), word)) for word in query.split("+") if word not in stopwords]
    counts = Counter(queries)
    q_vec = []
    s = set() # doc_ids that contain all words in queries
    q_unique = lisst(counts.keys()) # unique words in queries
    for word in q_unique:
        if word in inverted_index:
            s = s.intersection(inverted_index[word][1].keys())
            if not s:
                return flask.jsonify({"hits": []})
            else:
                tfq = counts[word]
                idf = inverted_index[word][0]
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
            tfd = inverted_index[word][1][doc][0]
            idf = inverted_index[word][0]
            d_vec.append(tfd*idf)
            if not norm_d:
                norm_d_squared = inverted_index[word][1][doc][1]
                norm_d = sqrt(norm_d_squared)
        tfidf = np.dot(q_vec, d_vec) / (norm_q * norm_d)
        weighted_score = weight * pagerank[doc] + (1 - weight) * tfidf
        tmp.append((-1*weighted_score, doc))
    tmp.sort()
    for data in tmp:
        context["hits"].append({"docid": data[1], "score": (data[0] * -1)})
    return flask.jsonify(**context)

def get_stopwords():
    stopwords = set()
    with open(stopwords_filename, "r") as stopwords_file:
        for line in stopwords_file:
          word = re.sub(r'[^a-zA-Z0-9]+', '', line)
          stopwords.add(word)
    return stopwords

def get_pagerank():
    pagerank = {}
    with open(pagerank_filename, "r") as pr_file:
        for line in pr_file:
            data = line.split(',')
            pagerank[data[0]] = data[1] #data[0] == doc_id, data[1] == pagerank(doc_id)
    return pagerank

def get_inverted_index():
    inverted_index = {} #{term: [idf, {doc_id: [freq in doc, squared norm factor]}]}
    with open(inverted_index_filename, "r") as idx:
        for line in idx:
            data = line.split(" ")
             term = data[0]
             idf = data[1]
             inverted_index[term] = [idf]
             freqs = {}
             for i in range(2, len(data)):
                 if (i - 2) % 3 == 0:
                     doc_id = data[i]
                 elif (i - 2) % 3 == 1:
                     freq = data[i]
                 else:
                     norm = data[i]
                     freqs[doc_id] = [freq, norm]
             inverted_index[term].append(freqs)
    return inverted_index
