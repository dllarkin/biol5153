#! /usr/bin/env python3

import sys
from Bio import SeqIO

fasta_file = sys.argv[1]
remove_file = sys.argv[2]
result_file = sys.argv[3]

remove = set()
with open(remove_file) as f:
	for line in f:
		line = line.strip()
		if line !="":
			remove.add(line)

fasta_sequences = SeqIO.parse(open(fasta_file), 'fasta')

with open(result_file, "w") as f:
	for seq in fasta_sequences:
		nam = seq.id
		nuc = str(seq.seq)
		if nam not in remove and len(nuc) > 0:
			SeqIO.write([seq], f, "fasta")

for record in SeqIO.parse("filtered_file.fasta", "fasta"):
	print(record)

