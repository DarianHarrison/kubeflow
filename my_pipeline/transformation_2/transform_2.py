#!/usr/bin/env python3

# Function doing the actual work (Outputs first N lines from a text file)
def do_work(input1_file, output1_file):
  for x, line in enumerate(input1_file):
    transformed_line = "verify this is prepended ___" + line
    # _ = print(transformed_line)
    _ = output1_file.write(transformed_line)

def main():

  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument('--transform_2_input1')
  parser.add_argument('--transform_2_output1')
  args = parser.parse_args()

  from pathlib import Path

  Path(args.transform_2_output1).parent.mkdir(parents=True, exist_ok=True)
  
  with open(args.transform_2_input1, mode='r', encoding='utf-8') as input1_file:
    with open(args.transform_2_output1, mode='w', encoding='utf-8') as output1_file:
      do_work(input1_file, output1_file)

if __name__ == "__main__":
  main()