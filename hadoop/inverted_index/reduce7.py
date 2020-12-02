#!/usr/bin/env python3

"""<term> <idf> <doc_id><freq><norm_factor>... reduced"""

import sys

term_dict = {}

for line in sys.stdin:
  words = line.split()
  term = words[0]
  idf = words[1]
  docs = words[2:]

  for idx in range(0, len(docs), 3):
    doc_id = docs[idx]
    freq = docs[idx + 1]
    norm_factor = docs[idx + 2]

    if term not in term_dict:
      term_dict[term] = {}

    term_dict[term]['idf'] = idf
    term_dict[term][doc_id] = {
      'freq': freq,
      'norm_factor': norm_factor
    }


for term in term_dict:
  term_data = []
  term_data.append(term)
  term_data.append(term_dict[term]['idf'])

  for doc_id in term_dict[term]:
    if not doc_id == 'idf':
      term_data.append(doc_id)
      term_data.append(term_dict[term][doc_id]['freq'])
      term_data.append(term_dict[term][doc_id]['norm_factor'])

  print(' '.join(term_data))
