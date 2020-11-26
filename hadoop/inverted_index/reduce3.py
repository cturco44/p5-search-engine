#!/usr/bin/env python3
"""<term> <doc_id> <freq> <doc_id> <freq>... reduced"""

import sys

term_dict = {}

for line in sys.stdin:
  words = line.split()
  term = words[0]
  docs = words[1:]

  for idx in range(0, len(docs), 2):
    doc_id = docs[idx]
    freq = int(docs[idx + 1])

    if term not in term_dict:
      term_dict[term] = {}

    term_dict[term][doc_id] = freq


# print
for term in term_dict:
  term_freqs = []
  for doc_id in term_dict[term]:
    term_freqs.append(doc_id)
    term_freqs.append(str(term_dict[term][doc_id]))

  print(term + '\t' + ' '.join(term_freqs))