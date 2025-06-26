# summary_alignment_coverage.py

import os
from Bio import SeqIO

# Path to alignment files and gene list
alignment_folder = "/data1/evakristinawatiekp/FINAL/trimal_automated/"
list_file = "/data1/evakristinawatiekp/FINAL/trimal_automated/trimal_list.txt"

# Read gene IDs to be processed
with open(list_file) as f:
    gene_ids = [line.strip() for line in f if line.strip()]

# Print table header
print("GeneID\tNumTaxa\tAlignmentLength")

# Loop through all genes and summarize alignment
for gene_id in gene_ids:
    alignment_file = os.path.join(alignment_folder, f"aligned_{gene_id}_supercontig_trimal.fasta")
    if os.path.isfile(alignment_file):
        records = list(SeqIO.parse(alignment_file, "fasta"))
        if records:
            num_taxa = len(records)
            alignment_length = len(records[0].seq)  # Assumes trimmed alignments are length-consistent
            print(f"{gene_id}\t{num_taxa}\t{alignment_length}")
        else:
            print(f"{gene_id}\t0\t0")
    else:
        print(f"{gene_id}\t0\t0")
