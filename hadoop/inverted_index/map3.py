#!/usr/bin/env python3
"""Map 3 outputs <doc_id> <term x> <freq> <# docs containing term x>..."""

import sys


input_dict = {}
term_dict = {}  # counts how many docs contain each term

for line in sys.stdin:
  words = line.split()
  if len(words) > 0:
    doc_id = words[0]
    terms = words[1:]

    input_dict[doc_id] = {}

    for idx in range(0, len(terms), 2):
      term = terms[idx]
      count = int(terms[idx + 1])

      # add to input_dict
      input_dict[doc_id][term] = count

      # add to term_dict
      if term in term_dict:
        term_dict[term] += 1
      else:
        term_dict[term] = 1

# formatting for printing
for doc_id in input_dict:
  term_freqs = []
  for term in input_dict[doc_id]:
    term_freqs.append(term)  # term
    term_freqs.append(str(input_dict[doc_id][term]))  # freq in this doc
    term_freqs.append(str(term_dict[term]))  # number of docs containing term

  print(doc_id + '\t' + ' '.join(term_freqs))
