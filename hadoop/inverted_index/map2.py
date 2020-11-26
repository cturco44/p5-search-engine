#!/usr/bin/env python3
"""Map 2 removes stopwords."""

import sys
import re

# import stopwords
stopwords_file = open("stopwords.txt", "r")
stopwords = []
for line in stopwords_file:
  word = re.sub(r'[^a-zA-Z0-9]+', '', line)
  stopwords.append(word)
  
stopwords_file.close()

for line in sys.stdin:
  words = line.split()
  if len(words) > 0:
    doc_id = words[0]
    body = words[1:]

    # remove stopwords
    for term in body:
      if term in stopwords:
        body.remove(term)
    
    print(doc_id + '\t' + ' '.join(body))