

with open (r'C:\fastafile1\DAY1.fasta.py') as f:
     for line in f:
          if line.startswith('>'):
               print("header found:",line.strip())
          else:
                print("sequences length:", len(line.strip()))
