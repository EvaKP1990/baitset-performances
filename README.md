# Patristic Distance & Gene Recovery Scripts

This repository contains two utility scripts for summarizing gene recovery and patristic distances from alignment data processed with HybPiper and TrimAl.

## Contents

- `summary_alignment_coverage.py`  
  Outputs the number of taxa and alignment length for each gene in a multi-locus alignment dataset.

- `generate_sample_gene_matrix.py`  
  Generates a presence/absence matrix of genes per sample and a summary table of recovery rates per sample.

## Requirements

- Python 3.10
- Biopython

Install dependencies (if needed):

```bash
pip install biopython
```

## Usage

Edit the paths inside each script to match your directory structure and file names, then run:

```bash
python summary_alignment_coverage.py
python generate_sample_gene_matrix.py
```

Both scripts are optimized for datasets from target capture projects using HybPiper + MAFFT + TrimAl.
