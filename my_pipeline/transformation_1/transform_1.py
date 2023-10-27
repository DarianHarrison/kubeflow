#!/usr/bin/env python3

# Function doing the actual work (Outputs first N lines from a text file)
def do_work(input1_file, output1_file, param_1):
  for x, line in enumerate(input1_file):
    if x >= param_1:
      break
    _ = output1_file.write(line)

def main():

  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument('--transform_1_input1')
  parser.add_argument('--param_1', type=int, default=100)
  parser.add_argument('--transform_1_output1') # we dont hardcode output paths, we allow for the system to create 
  args = parser.parse_args()

  from pathlib import Path
  import os

  file_in=os.path.join(os.path.dirname(os.path.realpath(__file__)), args.transform_1_input1) # because we passed in local data
  Path(args.transform_1_output1).parent.mkdir(parents=True, exist_ok=True) # we dont hardcode paths, makue sure parent exists

  with open(file_in, mode='r', encoding='utf-8') as input1_file:
    with open(args.transform_1_output1, mode='w', encoding='utf-8') as output1_file:
      do_work(input1_file, output1_file, args.param_1)

if __name__ == "__main__":
  main()