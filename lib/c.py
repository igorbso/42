from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os
import sys

arquivo = open(sys.argv[1])
seq = arquivo.read()

#Função para identificar ORFs
def orf(genoma):
    starts = []
    orfs = []
    for i in range(len(genoma)-2):
        kmer = genoma[i:i + 3]
        if kmer == "ATG":
            starts.append(i)
    for i in starts:
        orfs.append(genoma[i:])
    return(orfs)

#Função para identificar CDSs
def criar_cds(sequence):
    stop_codons = ["TAA", "TAG", "TGA"]
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if codon in stop_codons:
            return sequence[:i+3]
    return sequence

orfs = orf(seq)
new_orfs = []

#executar as funções anteriores
for i in range(len(orfs)):
    cds2 = criar_cds(orfs[i])
    orfs[i] = cds2
for i in range(len(orfs)):
    stop_codons = ["TAA", "TAG", "TGA"]
    if (orfs[i][-3:]) in stop_codons:
        new_orfs.append(orfs[i])

pasta = "cds" 
os.system("mkdir "+ pasta)
all_sequences = []
for i in range(len(new_orfs)):
        all = []
        id = str(i+1)
        seq = Seq(new_orfs[i])
        b = SeqRecord(seq,id)
        all.append(b)
        all_sequences.append(b)
        output_path = os.path.join(pasta, f"{i + 1}.fasta")  
        SeqIO.write(all, output_path, "fasta")
print(f"{len(new_orfs)} cds foram obtidas")
with open("tmp.txt", "w") as all_file:
    SeqIO.write(all_sequences, all_file, "fasta")        