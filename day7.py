from Bio import Entrez , SeqIO
# email
Entrez.email ="khushboo_srkggg38@gmail.com"
#fetch id to the gene bank
gene_id = "NM_000546"

print(f"Fetching{gene_id}from genbank...")
with Entrez.efetch(db="nucleotide",id=gene_id,rettype="gb",retmode="text")as handle:
     record =SeqIO.read(handle,"genbank")
     

print(f"ID :{record.id}")
print(f"Name:{record.name}")
print(f"Length:{len(record.seq)}bp")
print(f"Organism:{record.annotations.get('organism')}")
print("Description:{record.description[:100]}...")

#features
for features in record.features[:5]:
     print(features.type,features.location )
#save record in fasta and gene bank
SeqIO.write(record,f"{gene_id}.fasta","fasta")
SeqIO.write(record,f"{gene_id}.gb","genbank")
print(f"saves{gene_id}.fasta and {gene_id}.gb")
     




































