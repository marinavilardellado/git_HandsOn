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
if re.search('^[ACGTU]+$', args.seq): 
    if re.search('T', args.seq):  #If we find a T, for sure it will be DNA
        print ('The sequence is DNA')
    elif re.search('U', args.seq): #If we find a U, the sequence will be RNA
        print ('The sequence is RNA')
    else: #If we have a sequence that contains A,C, and G, we don't know if it is RNA or DNA.
        print ('The sequence can be DNA or RNA')
else: #If the input sequence contains a letter that is not A,C,G,T or U, it is not DNA nor RNA
    print ('The sequence is not DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq): #if the given motif is within the sequence, it is found
        print("FOUND")
    else: #if not, the motif  is not found in the sequence
        print("NOT FOUND MOTIF")

