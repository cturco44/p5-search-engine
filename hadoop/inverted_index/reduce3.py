#!/usr/bin/env python3
"""Reduce 3 outputs <doc_id> <term x> <freq> <# docs containing term>..."""
import sys

input_dict = {}
term_dict = {}  # number of docs containing each term

for line in sys.stdin:
  words = line.split()
  if len(words) > 0:
    doc_id = words[0]
    terms = words[1:]

    input_dict[doc_id] = {}

    for idx in range(0, len(terms), 3):
      term = terms[idx]
      freq = int(terms[idx + 1])
      count = int(terms[idx + 2])

      if term in term_dict:
        term_dict[term] += count
      else:
        term_dict[term] = count
      
      input_dict[doc_id][term] = freq

# formatting for printing
for doc_id in input_dict:
  term_freqs = []
  for term in input_dict[doc_id]:
    term_freqs.append(term)  # term
    term_freqs.append(str(input_dict[doc_id][term]))  # freq in this doc
    term_freqs.append(str(term_dict[term]))  # number of docs containing term

  print(doc_id + '\t' + ' '.join(term_freqs))

