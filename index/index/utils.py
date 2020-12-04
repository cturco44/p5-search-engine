"""Reads stopwords, pagerank, inverted_index into memory."""
import pathlib
import re

index_package_dir = pathlib.Path(__file__).parent

stopwords_filename = index_package_dir/"stopwords.txt"
pagerank_filename = index_package_dir/"pagerank.out"
inverted_index_filename = index_package_dir/"inverted_index.txt"


def get_stopwords():
    """Read stopwords."""
    stop = set()
    with open(stopwords_filename, "r") as stopwords_file:
        for line in stopwords_file:
            word = re.sub(r'[^a-zA-Z0-9]+', '', line)
            stop.add(word)
    return stop


def get_pagerank():
    """Read pagerank."""
    rank = {}
    with open(pagerank_filename, "r") as pr_file:
        for line in pr_file:
            line = line.strip()
            data = line.split(',')
            rank[int(data[0])] = float(data[1])
            # data[0] == doc_id, data[1] == pagerank(doc_id)
    return rank


def get_inverted_index():
    """Read inverted_index."""
    index = {}  # {term: [idf, {doc_id: [freq in doc, squared norm factor]}]}
    with open(inverted_index_filename, "r") as idx:
        for line in idx:
            line = line.strip()
            data = line.split(" ")
            term = data[0]
            idf = float(data[1])
            index[term] = [idf]
            freqs = {}
            for i in range(2, len(data)):
                if (i - 2) % 3 == 0:
                    doc_id = int(data[i])
                elif (i - 2) % 3 == 1:
                    freq = int(data[i])
                else:
                    norm = float(data[i])
                    freqs[doc_id] = [freq, norm]
            index[term].append(freqs)
    return index


stopwords = get_stopwords()
pagerank = get_pagerank()
inverted_index = get_inverted_index()
# {term: [idf, {doc_id: [freq in doc, squared norm factor]}]}
