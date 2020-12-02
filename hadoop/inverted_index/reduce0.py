#!/usr/bin/env python3
"""Reduce 0."""

import sys

count = 0

for line in sys.stdin:
  count += 1

new_file = open("total_document_count.txt", "w")
new_file.write(str(count))
new_file.close()
