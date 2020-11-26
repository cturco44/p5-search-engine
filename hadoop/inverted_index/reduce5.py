#!/usr/bin/env python3
"""Reduce 5 outputs <term> <idf> <doc_id> <freq in doc> <norm factor of doc>..."""
import sys

for line in sys.stdin:
  words = line.split()
  data = words[1:]
  print(words[0] + " " + ' '.join(data))
