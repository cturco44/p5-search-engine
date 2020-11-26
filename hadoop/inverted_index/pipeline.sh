#!/bin/bash
#
# Example of how to chain mapreduce jobs together.  The output of one
# job is the input to the next.
#
# Hadoop options
# jar index/hadoop/hadoop-streaming-2.7.2.jar   # Hadoop configuration
# -input <directory>                            # Input directory
# -output <directory>                           # Output directory
# -mapper <exec_name>                           # Mapper executable
# -reducer <exec_name>                          # Reducer executable

# Stop on errors
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail

# Job 0
rm -rf output0

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input input \
  -output output0 \
  -mapper ./map0.py \
  -reducer ./reduce0.py \

# Job 1
rm -rf output

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input input \
  -output output \
  -mapper ./map1.py \
  -reducer ./reduce1.py \

# Job 2
rm -rf output2

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input output \
  -output output2 \
  -mapper ./map2.py \
  -reducer ./reduce2.py \

# Job 3
rm -rf output3

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input output2 \
  -output output3 \
  -mapper ./map3.py \
  -reducer ./reduce3.py

# Job 4
rm -rf output4

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input output3 \
  -output output4 \
  -mapper ./map4.py \
  -reducer ./reduce4.py

# Job 5
rm -rf output5

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input output4 \
  -output output5 \
  -mapper ./map5.py \
  -reducer ./reduce5.py


# Job 6
rm -rf output6

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input output5 \
  -output output6 \
  -mapper ./map6.py \
  -reducer ./reduce6.py

# Job 7
rm -rf output7

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input output6 \
  -output output7 \
  -mapper ./map7.py \
  -reducer ./reduce7.py \

# concatenate all output files
cat output7/* > inverted_index.txt
