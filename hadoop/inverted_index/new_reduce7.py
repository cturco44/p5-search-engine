#!/usr/bin/env python3

"""<term> <idf> <doc_id><freq><norm_factor>"""

import sys

for line in sys.stdin:
  words = line.split()
  term = words[0]
  data = words[1:]
  print(term + ' ' + ' '.join(data))
