import os
import sys
from Bio import SeqIO

#extrai a sequência do arquivo
seq = ""
for i in SeqIO.parse(f"./{sys.argv[2]}", "fasta"):
        seq = i.seq
with open("tmp.txt", "w") as tmp_file:
    tmp_file.write(str(seq))

#executa o programa a
os.system(f"py ./lib/a.py tmp.txt")

#executa o programa b
os.system(f"py ./lib/b.py tmp.txt")

#executa o programa c
os.system(f"py ./lib/c.py tmp.txt")

#executa o programa d
os.system(f"py ./lib/d.py tmp.txt")
