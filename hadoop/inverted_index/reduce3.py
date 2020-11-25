#!/usr/bin/env python3
"""Reduce 3 outputs <doc_id> <term x> <freq of x in doc> <idf>..."""

import sys
from math import log


# import total number of docs (from job 0)
doc_count_file = open("total_document_count.txt", "r")
total_docs = float(doc_count_file.readline())

idf_dict = {}

for line in sys.stdin:
  words = line.split()
  if len(words) > 0:
    doc_id = words[0]
    terms = words[1:]

    for idx in range(0, len(terms), 3):
      term = terms[idx]
      freq = terms[idx + 1]
      num_docs = terms[idx + 2]

      # either refer to or add to idf_dict
      if term in idf_dict:
        idf = idf_dict[term]
      else:
        div = float(total_docs/float(num_docs))
        idf = log(div, 10)
        idf_dict[term] = idf

      # replace num of docs with idf
      terms[idx + 2] = str(idf)
      
    # format for printing - by line
    print(doc_id + '\t' + ' '.join(terms))
