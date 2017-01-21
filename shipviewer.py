import argparse
from selectFunctions import *

parser = argparse.ArgumentParser(prog = 'shipviewer', description="Hello World")
parser.add_argument('action', action="store")
parser.add_argument('-n', action="store")
parser.add_argument('-c', action="store")
parser.add_argument('-l', action="store")
parser.add_argument('-f', action="store")

args = vars(parser.parse_args())

if args['action'] == "show" and args['n'] is not None:
    if args['f'] is None:
        selectByName(args['n'])
    elif args['f'] == 'json':
        selectByNameJSON(args['n'])

elif args['action'] == "show" and args['c'] is not None:
    selectByCode(str(args['c']))

elif args['action'] == "search" and args['n'] is not None:
    filterByName(args['n'])

elif args['action'] == "status" and args['n'] is not None:
    selectJourneys(args['n'])

elif args['action'] == "arriving" and args['l'] is not None:
    arriving(args['l'])