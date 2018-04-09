#! /usr/bin/env python3

# read the genome (FASTA format), store it in a variable - use seqIO for this.

# open the .gff file

# read it in line by line using a for loop
#for line in 
#    split the line into a list 
#    use begin and end coords to extract the sebseq from the genome
#    print to screen
# close the .gff file

# from BCBio import GFF
# from Bio import SeqIO

#in_seq_file = "watermelon.fsa"
#in_seq_handle = open(in_seq_file)
#seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
#in_seq_handle.close()

#in_file = "watermelon.gff"
#in_handle = open(in_file)
#for record in GFF.parse(in_handle, base_dict=seq_dict):
#    print(record)
#in_handle.close()

# (species_name, type, begin, end) = line.split('\t')


from Bio import SeqIO
import csv
import argparse
genome = SeqIO.read("watermelon.fsa", "fasta")
print("seqence is: ", len(genome.seq))

gff = open("watermelon.gff", "r")
for line in gff:
	words = line.split("\t")
	species = (words[0])
	start = int(words[3])
	end = int(words[4])
	gene = (words[8])
	print(">" + species + " | " + gene + genome.seq[start-1:end])
gff.close()

#for seq_record in SeqIO.parse("watermelon.fsa", "fasta"):
#	print(seq_record.id)
#	print(repr(seq_record.seq))
#	print(len(seq_record))
