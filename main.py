#!/usr/bin/python

import sys, getopt
from p1.main import execute as exec1
from p0.main import execute as exec0

def getProblem(num: int) -> None:
  if 0 < num < 1000:
    exec0(num)
  elif 2000 > num >= 1000:
    exec1(num)


if __name__ == '__main__':
  argv = sys.argv[1:]

  try:
    opts, args = getopt.getopt(argv, "n:")
  except getopt.GetoptError:
    print('main.py -n <problem number>')
    sys.exit(2)

  problem = None
  for opt, arg in opts:
    if opt == '-n':
      problem = int(arg)

  if problem is None:
    print('Unknown problem number: ', problem)
    sys.exit(2)

  getProblem(problem)
