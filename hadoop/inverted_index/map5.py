#!/usr/bin/env python3
"""Map 5 outputs <term> <idf> <doc_id> <freq in doc> <norm factor of doc>..."""

import sys

term_dict = {}

for line in sys.stdin:
  words = line.split()
  if len(words) > 0:
    doc_id = words[0]
    doc_norm_fact = words[1]
    terms = words[2:]

    for idx in range(0, len(terms), 3):
      term = terms[idx]
      freq = terms[idx + 1]
      idf = terms[idx + 2]

      # add term or doc to term_dict
      new_doc = {
        "freq": str(freq),
        "norm": str(doc_norm_fact)
      }

      if term in term_dict:
        term_dict[term][doc_id] = new_doc
      else:
        new_term = {
          "idf": str(idf),
          doc_id: new_doc
        }

        term_dict[term] = new_term

# print
for term in term_dict:
  term_info = []

  #term_info.append(term)
  term_info.append(term_dict[term]["idf"])
  
  for doc_id in term_dict[term]:
    if not doc_id == 'idf':
      term_info.append(doc_id)
      term_info.append(term_dict[term][doc_id]['freq'])
      term_info.append(term_dict[term][doc_id]['norm'])

  print(term + '\t' + ' '.join(term_info))