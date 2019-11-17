import logging
import argparse
import sys

#command line arguments parsing

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-i', '--input', help='Path to CCTV cam ip file')
arg_parser.add_argument('-l', '--log', help='Path to log file')

args = arg_parser.parse_args()

if args.input:
    pass
else:
    raise Exception('No input file')

if args.log:
    logging.basicConfig(filename=args.log, level=logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)