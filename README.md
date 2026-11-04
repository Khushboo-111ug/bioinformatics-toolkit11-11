# bioinformatics-toolkit11-11
My Bioinformatics Learning Journey - From Day 1 to Advanced | Python for DNA, RNA & Protein Analysis
# 🧬 bioinformatics-toolkit11-11
My Bioinformatics Learning Journey - From Day 1 to Advanced | Python for Genomic Analysis

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Biopython](https://img.shields.io/badge/Biopython-Enabled-green)
![Status](https://img.shields.io/badge/Day-8%20Completed-success)

### 👋 About This Repo
30 Days of Bioinformatics challenge - Daily learning, coding and documenting from basic sequence handling to advanced genomic analysis.

### 📅 Progress Tracker
| Day | Topic | Gene / Task | Status |
|-----|-------|-------------|--------|
| Day 1-6 | Basics & Sequence Handling | Python + Biopython | ✅ Done |
| Day 7 | GenBank File Creation | NM_000546.6 | ✅ Done |
| Day 8 | TP53 Gene Analysis & Warning Fix | NM_000546.6 - 2512 bp, GC% 53.4% | ✅ Done |
| Day 9 |Sequence Analysis (Completed)  |  **31aa deletion** region study | ✅DONE |

### 🔬 Day 8 - TP53 Gene Analysis (Latest)

**Objective:** Clean GenBank file generation without Biopython warnings.

**Results:**
- **ID:** NM_000546.6 (TP53 Tumor Protein)
- **Length:** 2512 bp
- **First 60 bases:** CTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGG...
- **GC Content:** 53.4%
- **Protein:** LKSLEPPSREQVAAGLRGHF
- **Output File:** `day8.gb` - No Warnings, All Metrics Passed

**Key Learning & Fixes:**
1.  `Partial codon warning` -> Solved by `trimmed_seq = seq[:len(seq) - (len(seq) % 3)]`
2.  `molecule_type error` -> Solved by `record.annotations["molecule_type"] = "DNA"`
3.  IDLE default path issue - files were auto-detected from Python install folder.

**Files Added:**
- `day8.py` - Analysis script
- `day8.gb` - Final clean GenBank file

### 🛠️ Tech Stack
- Python 3.14.7
- Biopython (SeqIO, Seq, SeqRecord)
- Git & GitHub

### 🚀 How to Run
```bash
pip install biopython
python day8.py


DAY-9 COMPLETED✅
# TP53 Gene Analysis Project

**Gene:** TP53 (Tumor Protein P53) - Guardian of the Genome  
**Organism:** Homo sapiens  
**Analysis Period:** Day 8-10 Internship Project

## 🧬 Overview
This project focuses on the analysis of different isoforms and mutations of the TP53 gene, which is one of the most crucial genes in cancer research.

## 📅 Day 8-9: Sequence Analysis (Completed)
- **Canonical Sequence:** 393aa (UniProt P04637)
- **Short Isoform Analysis:** Characterization of the 373aa isoform
- **31aa deletion** region study
- Tools Used: UniProt, NCBI, Biopython

## 📅 Day 10: Poster and Presentation (Upcoming)
- TP53 pathway visualization
- Mutation hotspot mapping
- Final poster design and presentation

## 📁 Project Structure

⭐ Star this repo if you are also on a Bioinformatics journey!
