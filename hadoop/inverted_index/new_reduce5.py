#!/usr/bin/env python3

"""<doc_id> <term> <freq> <idf>...reduced."""

import sys

doc_dict = {}

for line in sys.stdin:
  words = line.split()
  doc_id = words[0]
  terms = words[1:]

  for idx in range(0, len(terms), 3):
    term = terms[idx]
    freq = int(terms[idx + 1])
    idf = float(terms[idx + 2])

    if doc_id not in doc_dict:
      doc_dict[doc_id] = {}
    
    if term not in doc_dict[doc_id]:
      doc_dict[doc_id][term] = {
        'freq': freq,
        'idf': idf
      }
    else:
      doc_dict[doc_id][term]['freq'] += freq

for doc_id in doc_dict:
  term_freqs = []

  for term in doc_dict[doc_id]:
    term_freqs.append(term)
    term_freqs.append(str(doc_dict[doc_id][term]['freq']))
    term_freqs.append(str(doc_dict[doc_id][term]['idf']))

  print(doc_id + '\t' + ' '.join(term_freqs))
