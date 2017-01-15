import sys, getopt
from selectFunctions import selectByName, selectByCode, filterByName, selectJourneys

argv = sys.argv[1:]

inputfile=''
outputfile=''
try:
    opts, args = getopt.getopt(argv, "c:n:f:j:", ["cfile=", "nfile=", "ffile=", "jfile="])
except getopt.GetoptError:
    print('test.py -i <inputfile> -o <outputfile>')
    sys.exit(1)

for opt, arg in opts:
    if opt in ("-n"):
        print arg
        selectByName(arg)
    elif opt in ("-c", "--code"):
        selectByCode(arg)

    elif opt in ("-f", "--filter"):
        filterByName(arg)

    elif opt in ("-j", "--journey"):
        selectJourneys(arg)