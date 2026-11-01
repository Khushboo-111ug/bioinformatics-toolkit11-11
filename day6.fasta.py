from Bio import SeqIO



file_name = "my_genes.fasta"
with open( file_name,"w")  as f:
     f.write(">test\nATGCATGC")


print(f" '{file_name}' file successfully generted .\n")


for record in SeqIO.parse(file_name,"fasta"):
     print(f"Gene ID    : {record.id}")
     print(f" Description  : {record.description}")
     print(f" Sequence Length : {len (record.seq)}bp")
     print(f"🔤 Sequence (5'->3'): {record.seq}")
     
      
     
