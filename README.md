# 🧬 bioinformatics-toolkit11-11

My bioinformatics learning journey—from sequence-handling basics to genomic analysis using Python.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Biopython](https://img.shields.io/badge/Biopython-Enabled-green)
![Progress](https://img.shields.io/badge/Day-9%20Completed-success)

## 👋 About This Repository

A 30-day bioinformatics challenge documenting daily learning, coding, and analysis—from basic sequence handling to genomic analysis.

## 📅 Progress Tracker

| Day | Topic | Gene / Task | Status |
|-----|-------|-------------|--------|
| Days 1–6 | Basics and sequence handling | Python + Biopython | ✅ Done |
| Day 7 | GenBank file creation | NM_000546.6 | ✅ Done |
| Day 8 | TP53 gene analysis and warning fixes | NM_000546.6; 2,512 bp; 53.4% GC | ✅ Done |
| Day 9 | TP53 sequence and isoform analysis | 393-aa canonical sequence, 373-aa short isoform, and 31-aa deletion region | ✅ Done |
| Day 10 | TP53 poster and presentation | Pathway visualization and mutation hotspot mapping | 🔄 Today's task |

## ✅ Day 9 Completion Notes — TP53 Sequence Analysis

**Gene:** TP53 (Tumor Protein p53)  
**Organism:** *Homo sapiens*  
**Tools and resources:** UniProt, NCBI, and Biopython

Completed work:
- Reviewed the canonical TP53 protein sequence (393 amino acids; UniProt P04637).
- Characterized the short 373-amino-acid isoform.
- Studied the region associated with the 31-amino-acid deletion.

## 🎯 Today's Task — Day 10

- Create a visualization of the TP53 pathway.
- Map TP53 mutation hotspots.
- Prepare the final poster and presentation.

## 🔬 Previous Work — Day 8

Analyzed the TP53 reference sequence NM_000546.6 and generated a clean GenBank file.

- Sequence length: 2,512 bp
- GC content: 53.4%
- Output: `day8.gb`
- Fixed the partial-codon warning by trimming the sequence to a complete codon.
- Set `record.annotations["molecule_type"] = "DNA"` to resolve the molecule type error.

## 🛠️ Tech Stack

- Python 3.14.7
- Biopython (SeqIO, Seq, SeqRecord)
- Git and GitHub

## 🚀 How to Run

```bash
pip install biopython
python day8.py
```

⭐ Star this repository if you're also on a bioinformatics journey!
