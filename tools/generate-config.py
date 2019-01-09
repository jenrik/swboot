#!/usr/bin/env python3
from lib import generate
import sys

if len(sys.argv) < 3:
  print('Generate the complete configuration for a switch given it\'s name and model')
  print('')
  print('Usage: {} name model'.format(sys.argv[0]))
  print('Example: {} D29-A WS-C2950T-24'.format(sys.argv[0]))
  sys.exit(1)

switch = sys.argv[1]
model = sys.argv[2]

print(generate.generate(switch, model))
