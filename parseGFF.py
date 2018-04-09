#! /usr/bin/env python3

# read the genome (FASTA format), store it in a variable - use seqIO for this.

# open the .gff file

# read it in line by line using a for loop
#for line in 
#    split the line into a list 
#    use begin and end coords to extract the sebseq from the genome
#    print to screen
from BCBio import GFF
from Bio import SeqIO

in_seq_file = "watermelon.fsa"
in_seq_handle = open(in_seq_file)
seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
in_seq_handle.close()

in_file = "watermelon.gff"
in_handle = open(in_file)
for rec in GFF.parse(in_handle, base_dict=seq_dict):
    print rec
in_handle.close()


# close the .gff file



