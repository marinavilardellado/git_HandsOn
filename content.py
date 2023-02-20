#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

args = parser.parse_args()

args.seq = args.seq.upper()

lenght = len(args.seq)
g_content = args.seq.count("G") / lenght *100
c_content = args.seq.count("C") / lenght *100
a_content = args.seq.count("A") / lenght *100

#To identify if the given sequence is DNA or RNA:
if re.search("^[ACGTU]+$", args.seq):
    if re.search("^[^U]+$", args.seq) and re.search("T", args.seq):
     #If the sequence do not contains U, but has T, it is DNA for sure
        t_content = args.seq.count("T") / lenght *100
        print(f"The G content is {g_content}, the proportion of C is {c_content}, the proportion of a is {a_content}, the proportion of t is {t_content}")
    elif re.search("^[^T]+$", args.seq) and re.search("U", args.seq):
     #If the sequence do not contains T, but it contains U, for sure it is RNA
        u_content = args.seq.count("U") / lenght *100
        print(f"The G content is {g_content}, the proportion of C is {c_content}, the proportion of A is {a_content}, the proportion of U is {u_content}")
