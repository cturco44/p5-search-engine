#!/usr/bin/env python3
"""Reduce 4 outputs <doc id> <norm factor w/o sqrt> <term> <freq> <idf>..."""
import sys


for line in sys.stdin:
  words = line.split()
  if len(words) > 0:
    doc_id = words[0]
    terms = words[1:]

    # calculate norm factor (without sqrt) of doc
    sum = 0.0
    for idx in range(0, len(terms), 3):
      term = terms[idx]
      freq = float(terms[idx + 1])
      idf = float(terms[idx + 2])

      freq_sq = float(freq ** 2)
      idf_sq = float(idf ** 2)

      sum += (freq_sq * idf_sq)

    print(doc_id + '\t' + str(sum) + ' ' + ' '.join(terms))
