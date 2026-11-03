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
| Day 9 | Upcoming | - | ⏳ |

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
⭐ Star this repo if you are also on a Bioinformatics journey!
