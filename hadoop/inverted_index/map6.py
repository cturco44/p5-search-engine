#!/usr/bin/env python3

"""<doc_id> <norm_factor s/o sqrt> <term><freq><idf>..."""

import sys

doc_dict = {}

for line in sys.stdin:
  words = line.split()
  doc_id = words[0]
  terms = words[1:]

  sum = 0.0
  for idx in range(0, len(terms), 3):
    term = terms[idx]
    freq = int(terms[idx + 1])
    idf = float(terms[idx + 2])

    freq_sq = freq ** 2
    idf_sq = idf ** 2

    sum += (freq_sq * idf_sq)

  print(doc_id + '\t' + str(sum) + ' ' + ' '.join(terms))
