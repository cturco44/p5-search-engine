"""REST API for available directories."""
import flask
import index
import re

index_package_dir = pathlib.Path(__file__).parent.parent
stopwords_filename = index_package_dir/"stopwords.txt"
pagerank_filename = index_package_dir/"pagerank.out"
inverted_index_filename = index_package_dir/"inverted_index.txt"

stopwords = get_stopwords()
pagerank = get_pagerank()
inverted_index = get_inverted_index()

@index.app.route("/api/v1/", methods=["GET"])
def get_dir():
    context = {"hits": "/api/v1/hits/", "url": "/api/v1/"}
    return flask.jsonify(**context)

@index.app.route("/api/v1/hits/", methods=["GET"])
def get_hits():
    weight = flask.request.args.get('w')
    query = flask.request.args.get('q')
    queries = [word for word in query.split("+") if word not in stopwords]





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
