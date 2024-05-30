import os
import sys
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


arquivo = open(sys.argv[1])
texto = arquivo.read()
pasta = "saida" 
os.system("mkdir "+ pasta)

def kmers(genoma):
    a = []
    all = []
    for i in range(len(genoma)-30):
        kmer = genoma[i:i + 31]
        a.append(kmer)
    print(f"{len(a)} reads foram obtidas")
    for i in range(len(a)):
        id = str(i+1)
        seq = Seq(a[i])  
        b = SeqRecord(seq, id=id, description="")
        all.append(b)
    output_path = os.path.join(pasta, "reads.fasta")
    SeqIO.write(all, output_path, "fasta")


kmers(texto)

