# generate_sample_gene_matrix.py

import os
from collections import defaultdict
from Bio import SeqIO

# Path settings
alignment_folder = "/data1/evakristinawatiekp/FINAL/trimal_automated/"
list_file = "/data1/evakristinawatiekp/FINAL/trimal_automated/trimal_list.txt"
output_matrix = "/data1/evakristinawatiekp/FINAL/trimal_automated/sample_gene_matrix.tsv"
output_summary = "/data1/evakristinawatiekp/FINAL/trimal_automated/sample_recovery_summary.tsv"

# Read gene list
with open(list_file) as f:
    gene_ids = [line.strip() for line in f if line.strip()]

# Dictionary to track presence/absence of genes
presence = defaultdict(lambda: defaultdict(int))
all_samples = set()

# Iterate through alignments and collect gene recovery
for gene_id in gene_ids:
    alignment_file = os.path.join(alignment_folder, f"aligned_{gene_id}_supercontig_trimal.fasta")
    if os.path.isfile(alignment_file):
        records = SeqIO.parse(alignment_file, "fasta")
        for record in records:
            sample = record.id.split()[0]
            presence[sample][gene_id] = 1
            all_samples.add(sample)

# Sort for consistent output
all_samples = sorted(all_samples)
gene_ids = sorted(gene_ids)

# Write matrix file: sample × gene presence/absence
with open(output_matrix, "w") as out:
    out.write("Sample\t" + "\t".join(gene_ids) + "\n")
    for sample in all_samples:
        row = [sample] + [str(presence[sample].get(gene, 0)) for gene in gene_ids]
        out.write("\t".join(row) + "\n")

# Write recovery summary per sample
with open(output_summary, "w") as out:
    out.write("Sample\tGenesRecovered\tRecoveryRate(%)\n")
    total_genes = len(gene_ids)
    for sample in all_samples:
        genes_recovered = sum(presence[sample].values())
        recovery_rate = genes_recovered / total_genes * 100
        out.write(f"{sample}\t{genes_recovered}\t{recovery_rate:.2f}\n")
