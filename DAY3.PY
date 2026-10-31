# DAY3 Reverse Complement +GC%
dna = "ATGCATGCATGCATGCATGC"
complement = " "

for base in dna:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "G":
        complement += "C"
    elif base == "C":
        complement +="G"

#Reverse Complement +GC%
        
reverse_complement = complement[::-1]
print("Reverse Complement:",reverse_complement)

#GC%
g_count =dna.count("G")
c_count =dna.count("C")
gc_percent = (g_count + c_count)/len(dna)*100



print("Original:", dna)            
print("Complement:", complement)   
print("Length:", len(dna))
print("GC%:", gc_percent)
