#!/usr/bin/env python3

"""<doc_id> <term> <freq> <idf>..."""

import sys

doc_dict = {}

for line in sys.stdin:
  words = line.split()
  term = words[0]
  idf = float(words[1])
  docs = words[2:]

  for idx in range(0, len(docs), 2):
    doc_id = docs[idx]
    freq = int(docs[idx + 1])

    new_term = {
      "freq": freq,
      "idf": idf
    }

    if doc_id in doc_dict:
      doc_dict[doc_id][term] = new_term
    else:
      new_doc = {
        term: new_term
      }

      doc_dict[doc_id] = new_doc


for doc_id in doc_dict:
  term_freqs = []

  for term in doc_dict[doc_id]:
    term_freqs.append(term)
    term_freqs.append(str(doc_dict[doc_id][term]['freq']))
    term_freqs.append(str(doc_dict[doc_id][term]['idf']))

  print(doc_id + '\t' + ' '.join(term_freqs))