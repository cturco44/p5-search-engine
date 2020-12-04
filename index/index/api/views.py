"""REST API for available directories."""
from math import sqrt
import flask
import index


@index.app.route("/api/v1/", methods=["GET"])
def get_dir():
    """Return directory."""
    context = {"hits": "/api/v1/hits/", "url": "/api/v1/"}
    return flask.jsonify(**context)


@index.app.route("/api/v1/hits/", methods=["GET"])
def get_hits():
    """Return hits."""
    weight = float(flask.request.args.get('w'))
    queries = []
    for word in flask.request.args.get('q').split(" "):
        if word not in index.stopwords:
            queries.append("".join(filter(str.isalnum, word.lower())))

    queries = [x for x in queries if x != '']
    if not queries:
        return flask.jsonify({"hits": []})
    q_vec = []
    docs = set()  # doc_ids that contain all words in queries
    q_unique = list(set(queries))  # unique words in queries
    for word in q_unique:
        if word in index.inverted_index:
            if not docs:
                docs = set(index.inverted_index[word][1].keys())
            else:
                docs = docs.intersection(index.inverted_index[word][1].keys())
            if not docs:
                return flask.jsonify({"hits": []})
            tfq = float(queries.count(word))
            idf = index.inverted_index[word][0]
            q_vec.append(tfq*idf)
        else:
            return flask.jsonify({"hits": []})
    norm_q = sqrt(sum([x**2 for x in q_vec]))
    hits = []  # (weighted_score * -1, doc_id)
    for doc in docs:
        d_vec = []
        norm_d = None
        for word in q_unique:
            tfd = index.inverted_index[word][1][doc][0]
            idf = index.inverted_index[word][0]
            d_vec.append(tfd*idf)
            if not norm_d:
                norm_d = sqrt(index.inverted_index[word][1][doc][1])
        tfidf = sum(map(lambda x: x[0]*x[1],
                    zip(q_vec, d_vec))) / (norm_q * norm_d)
        hits.append({"docid": doc,
                    "score": weight*index.pagerank[doc] + (1 - weight)*tfidf})
    hits.sort(key=lambda x: (x["score"] * -1, x["docid"]))
    return flask.jsonify({"hits": hits})
