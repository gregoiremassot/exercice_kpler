import argparse
parser = argparse.ArgumentParser(prog = 'shipviewer', description="Hello World")
parser.add_argument('action', action="store")
parser.add_argument('-n', action="store")
parser.add_argument('-c', action="store")
print(parser.parse_args())