#! /usr/bin/env python3

# this script will parse a GFF file, extracting sequences for the annotated features

# load required modules
import sys
import os
import re
import argparse
from Bio import SeqIO
from collections import defaultdict


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
def get_feature_sequence(dna, start, end, strand):
	# extract the corresponding sequence
	fragment = dna[int(start)-1:int(end)]
	# print the sequence, either forward or reverse complemented
	if(strand == "+"):
		return fragment
	else:
		return fragment.reverse_complement()

def parse_gff(dna):
	# open and parse the gff file
	gff_file = open(args.gff, 'r')
	# dictionary to store exons: key = gene name, value = list of exon sequences
	exons_dictionary = {}

	for line in gff_file:
		# split each line on a tab
		(seqid, source, feature, start, end, length, strand, phase, attributes) = line.split('\t')
		
		if(feature == 'CDS' or feature == 'tRNA' or feature == 'rRNA'):
			# split the attributes field
			atts = attributes.split(" ; ")
			# grab the gene name and, if present, the exon number
			gene = re.search("^Gene\s+(\S+)", atts[0])
			exon = re.search("exon\s+(\d+)",  atts[0])
			# if both the gene and exon are defined, meaning that this gene has introns and muliple exons, store the feature sequence
			if(gene and exon):
				# Is this gene already in our dictionary? If yes, store the feature sequence, indexed by the exon number 
				if gene.group(1) in exons_dictionary:
					exons_dictionary[gene.group(1)][int(exon.group(1))] = get_feature_sequence(dna, start, end, strand)
				# else it's not in our dictionary, so initialize the exons list, then store the feature sequence in it
				else:
					exons_dictionary[gene.group(1)] = defaultdict(list) # initializing the list
					exons_dictionary[gene.group(1)][int(exon.group(1))] = get_feature_sequence(dna, start, end, strand) # storing the sequence

			# else _only_ gene is defined, so there aren't introns, and we can just print it here
			else:
				print(">" + seqid.replace(" ", "_") + "_" + gene.group(1))
				print(get_feature_sequence(dna, start, end, strand))


	gff_file.close() # close the gff file

	# splice and print CDS sequences for genes with introns, stored in exons_dictionary{}
	for gene, exons in exons_dictionary.items():
		# print the FASTA header
		print(">" + gene)
		# initialize a new variable, cds, that will hold the CDS sequence
		cds = ''
		# assemble the CDS sequence by looping over each exon in the list and appending it to the cds string
		for i in exons:
			print(">" + gene + "exon_" + i)
			print(i)
			cds += exons[i]
		# print the CDS sequence
		print(cds)

def main():
	genome = parse_fasta()
	parse_gff(genome)

# get the command line arguments
args = get_args()

main()





