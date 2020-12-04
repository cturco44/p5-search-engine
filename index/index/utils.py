"""Utils file for index server."""
import pathlib
import re

index_package_dir = pathlib.Path(__file__).parent

stopwords_filename = index_package_dir/"stopwords.txt"
pagerank_filename = index_package_dir/"pagerank.out"
inverted_index_filename = index_package_dir/"inverted_index.txt"


def get_stopwords():
    """Get stopwords from stopwords.txt file."""
    stopwords_set = set()
    with open(stopwords_filename, "r") as stopwords_file:
        for line in stopwords_file:
            word = re.sub(r'[^a-zA-Z0-9]+', '', line)
            stopwords_set.add(word)
    return stopwords_set


def get_pagerank():
    """Get PageRank from pagerank.out file."""
    pagerank_dict = {}
    with open(pagerank_filename, "r") as pr_file:
        for line in pr_file:
            line = line.strip()
            data = line.split(',')
            pagerank_dict[data[0]] = data[1]
            # data[0] == doc_id, data[1] == pagerank_dict(doc_id)
    return pagerank_dict


def get_inverted_index():
    """Get inverted index from inverted_index.txt file."""
    inverted_index_dict = {}
    # {term: [idf, {doc_id: [freq in doc, squared norm factor]}]}
    with open(inverted_index_filename, "r") as idx:
        for line in idx:
            line = line.strip()
            data = line.split(" ")
            term = data[0]
            idf = data[1]
            inverted_index_dict[term] = [idf]
            freqs = {}
            for i in range(2, len(data)):
                if (i - 2) % 3 == 0:
                    doc_id = data[i]
                elif (i - 2) % 3 == 1:
                    freq = data[i]
                else:
                    norm = data[i]
                    freqs[doc_id] = [freq, norm]
            inverted_index_dict[term].append(freqs)
    return inverted_index_dict


stopwords = get_stopwords()
pagerank = get_pagerank()
inverted_index = get_inverted_index()
# {term: [idf, {doc_id: [freq in doc, squared norm factor]}]}
