#fasta_translate.py
def translate_dna(seq):
     codon_table = {"ATG":"M ","TTT":"F","TTA":"L","TTC":"F","TTG":"L","TAA":"*","TAG":"*","TGA":"*"}#ALL 64 CODON
     protein = " "
     seq = seq.upper().strip()
     for i in range ( 0, len(seq),3):
          codon = seq[i:i+3]
          if len(codon)== 3:
               
               protein += codon_table.get(codon,"x")
          
     return protein
try:
     with open ( "sequence.fasta") as f:
          
          lines = f.readlines()
          dna = "".join([l.strip() for l in lines if not l.startswith(">")])
except  FileNotFoundError:
     dna = "ATGTTCTAA"
     print("file not found , extract sample dna :",dna)


print("protein:", translate_dna(dna))          
