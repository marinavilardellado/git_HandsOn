#!/usr/bin/env python

#Import the necessary modules
import sys, re
from argparse import ArgumentParser

#Create a parser object
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')

#Add arguments to the parser object
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

#If nothing is provided, exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

#Convert the sequence to upper case
args.seq = args.seq.upper()

#Check if the sequence contains nucleotides for identifying if the sequence is DNA or RNA
if re.search("^[ACGTU]+$", args.seq):
    if re.search("^[^U]+$", args.seq) and re.search("T", args.seq):
     #If the sequence do not contains U, but has T, it is DNA for sure
        print("The sequence is DNA")
    elif re.search("^[^T]+$", args.seq) and re.search("U", args.seq):
     #If the sequence do not contains T, but it contains U, for sure it is RNA
        print("The sequence is RNA")
    elif re.search("^[^T]+$", args.seq) and re.search("^[^U]+$", args.seq):
     #If the sequence doesn't contain T neither U, we don't know which type of sequence do we have
        print("The sequence can be DNA or RNA")
    else:
     #Then, we can have a mixted sequence, where we have T and U
        print("Your sequence is mixted")

# If the sequence contains a letter that that is not C,G,A,T or U, we don't have a DNA/RNA sequence
else:
    print("The sequence is not DNA neither RNA")





#Search for a motif in the sequence, if it is provided
if args.motif:
	#covert motif to uppercase
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq): #if the given motif is within the sequence, it is found
        print("FOUND")
    else: #if not, the motif  is not found in the sequence
        print("NOT FOUND MOTIF")

