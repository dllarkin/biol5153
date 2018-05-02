#! /usr/bin/env python3

# this script will parse a GFF file, extracting sequences for the annotated features

# load required modules
import sys
import os
import re
import argparse
from Bio import SeqIO


def get_args():
	# create an ArgumentParser object ('parser')
	parser = argparse.ArgumentParser()

	# add required/positional arguments
	parser.add_argument("gff", help="name of gff file")
	parser.add_argument("fasta", help="name of fasta file")

	# parse the argument
	return parser.parse_args()


def parse_fasta():
	# open and read the fasta file
	genome = SeqIO.read(args.fasta, 'fasta')
	return genome.seq
def reverse_comp(dna):
	return dna.reverse_complement()

def parse_gff(dna):
	# open and parse the gff file
	gff_file = open(args.gff, 'r')
	for line in gff_file:
		# split each line on a tab
		(seqid, source, feature, start, end, length, strand, phase, attributes) = line.split('\t')
		
		if(feature == 'CDS' or feature == 'tRNA' or feature == 'rRNA'):
			# split the attributes field
			atts = attributes.split(" ; ")
			# grab the gene name and, if present, the exon number
			gene = re.search("^Gene\s+(\S+)", atts[0])
			exon = re.search("exon\s+(\d+)",  atts[0])
			
			if(gene and exon):
				print(">" + seqid.replace(" ", "_") + "_" + gene.group(1) + "_" + exon.group(1))
			else:
				print(">" + seqid.replace(" ", "_") + "_" + gene.group(1))

			# extract the corresponding sequence
			fragment = dna[int(start)-1:int(end)]
			if(strand == "+"):
				print(fragment)
			else:
				print(reverse_comp(fragment))
			
	gff_file.close()

def main():
	genome = parse_fasta()
	parse_gff(genome)
	




# get the command line arguments
args = get_args()

main()

# Gene -> cox1 nad1 rpl1...
gene = [gene.group] 
# Exon -> 1,2 1,2,3,4,5 none...
exon = [exon.group]
# Sequence 2exons 5exons
# gene name = key
# Genes.Key:Value
gene_exon_dict = {}
for i in range(len(gene)):
	gene_exon_dict[genes[i]] = exon[i]
gene_seq_dict = {}
for i in range(len(gene_exon_dict)):
	gene_seq_dict[gene_exon_dict[i]] = fragment[i]
# exon numbers could be sorted as list or as a dictionary with sorted keys = value
# Value = [list of exons (1,2,3,4,5)] sequences instead of exon number
# Or as dictionary where key is exon number and value is sequence
# could sort by exon number in the end
# for loop of gff then loop over with for loop with genes
# this is a complex datastructure



