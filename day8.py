from Bio import  SeqIO
#IMPORT DAY 7 FILE
record = SeqIO.read("NM_000546.fasta","fasta")

if "molecule_type" not in record.annotations:
     record.annotations["molecule_type"] = "mRna"

print(f"ID:{record.id}")
print(f"Length:{len(record.seq)} bp")
print(f"First 60 base :{record.seq[:60]}")

gc = (record.seq.count('G') + record.seq.count('C'))/len(record.seq)*100
print(f"GC%:{gc:.1f} %")

trimmed_seq = record.seq[:len(record.seq)//3*3]
protein = trimmed_seq.translate()
print(f"protein:{protein[:20]}")

SeqIO.write(record,"day8.gb","genbank")








      
