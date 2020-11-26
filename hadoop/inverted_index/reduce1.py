#!/usr/bin/env python3
"""Reduce 1 outputs Map 1's output with all lowercase and alphanumeric."""

import sys
import re

for line in sys.stdin:
  words = line.split()
  if len(words) > 0:
    doc_line = []
    
    doc_id = words[0]
    body = words[1:]

    for idx, word in enumerate(body):
      lowercase = word.lower()
      alphanum = re.sub(r'[^a-zA-Z0-9]+', '', lowercase)

      body[idx] = alphanum

  print(doc_id + '\t' + ' '.join(body))