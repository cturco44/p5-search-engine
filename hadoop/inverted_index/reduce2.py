#!/usr/bin/env python3
"""Reduce 2 outputs <doc_id> <term x> <freq> <term y>..."""

import sys

word_dict = {}

# dictionary of docs with dictionaries of terms and frequencies
for line in sys.stdin:
  words = line.split()
  doc_id = words[0]
  word_dict[doc_id] = {}

  for word in words[1:]:
    if word in word_dict[doc_id]:
      word_dict[doc_id][word] += 1
    else:
      word_dict[doc_id][word] = 1

# formatting for printing
for doc_id in word_dict:
  term_freqs = []

  for term in word_dict[doc_id]:
    term_freqs.append(term)
    term_freqs.append(str(word_dict[doc_id][term]))

  print(doc_id + '\t' + ' '.join(term_freqs))
