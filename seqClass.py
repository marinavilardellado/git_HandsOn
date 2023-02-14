#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()

# Check if the sequence is DNA or RNA
if re.search("^[ACGTU]+$", args.seq):
    if re.search("^[^U]+$", args.seq) and re.search("T", args.seq):
        print("The sequence is DNA")
    elif re.search("^[^T]+$", args.seq) and re.search("U", args.seq):
        print("The sequence is RNA")
    elif re.search("^[^T]+$", args.seq) and re.search("^[^U]+$", args.seq):
        print("The sequence can be DNA or RNA")
    else:
        print("Your sequence is mixted")
else:
    print("The sequence is not DNA neither RNA")

#Motifs
if args.motif:
    #convert it to upper cases
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq): #if the given motif is within the sequence, it is found
        print("FOUND")
    else: #if not, the motif  is not found in the sequence
        print("NOT FOUND MOTIF")

