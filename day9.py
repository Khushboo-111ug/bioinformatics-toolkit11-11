from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.Seq import Seq
record = SeqIO.read("day8.gb","genbank")

cds_seq = None
for f in record.features:
     if f.type == "CDS":
          cds_seq = f.extract(record.seq)
          break


protein= cds_seq[:len(cds_seq)//3*3].translate(to_stop = True)

pa = ProteinAnalysis(str(protein))
print(f"File read:{record.id},Length:{len(record.seq)}bp")
print(f"Feature found:{len(record.features)}")
print(f"CDS Length: {len(cds_seq)}bp")

print(f"protein Length:{len(protein)}aa")#TP53=393
print(protein[:50])#first 50 amino acid


print(f"Mol.Wt:{pa.molecular_weight():.2f},pI:{pa.isoelectric_point():>2f}")
















                    
 
