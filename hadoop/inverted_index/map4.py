#!/usr/bin/env python3
"""<term> <idf> <doc_id> <freq>..."""

import sys
from math import log

# import total number of docs (from job 0)
doc_count_file = open("total_document_count.txt", "r")
total_docs = float(doc_count_file.readline())
doc_count_file.close()


for line in sys.stdin:
  words = line.split()
  term = words[0]
  docs = words[1:]

  num_docs = len(docs)/2

  div = float(total_docs/float(num_docs))
  idf = log(div, 10)

  print(term + '\t' + str(idf) + ' ' + ' '.join(docs))
