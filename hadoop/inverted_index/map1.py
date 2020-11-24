#!/usr/bin/env python3
"""Map 1."""

import sys
import re
import csv
csv.field_size_limit(sys.maxsize)


with sys.stdin as csv_file:
  reader = csv.reader(csv_file, delimiter=',')
  data = list(reader)

for row in data:
  title_body = row[1] + " " + row[2]
  title_body = re.sub(r'[^a-zA-Z0-9\s]+', '', title_body)
  print(row[0] + '\t' + title_body)
