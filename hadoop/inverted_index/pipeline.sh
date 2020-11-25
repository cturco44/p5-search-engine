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
rm -rf output_test
# TODO: CHANGE SMALL_INPUT TO INPUT
hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input small_input \
  -output output_test \
  -mapper ./map0.py \
  -reducer ./reduce0.py \

# Job 1
rm -rf small_output1

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input small_input \
  -output small_output1 \
  -mapper ./map1.py \
  -reducer ./reduce1.py \

# Job 2
rm -rf small_output2

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input small_output1 \
  -output small_output2 \
  -mapper ./map2.py \
  -reducer ./reduce2.py \

# Job 3
rm -rf small_output3

hadoop \
  jar ../hadoop-streaming-2.7.2.jar \
  -input small_output2 \
  -output small_output3 \
  -mapper ./map3.py \
  -reducer ./reduce3.py
