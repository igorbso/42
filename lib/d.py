from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import re
import sys
import os
from Bio import SeqIO

# Função para ler sequências de DNA de um arquivo
def ler_sequencias_dna(arquivo):
    dna_sequences = []
    with open(arquivo, "r") as file:
        current_seq = ""
        for line in file:
            if line.startswith(">"):
                if current_seq:
                    dna_sequences.append(current_seq)
                    current_seq = ""
            else:
                current_seq += line.strip()
        if current_seq:
            dna_sequences.append(current_seq)
    return dna_sequences

# Função para traduzir sequências de DNA em proteínas
def traduzir(dna_sequences):
    protein_sequences = []
    for dna in dna_sequences:
        seq = Seq(dna)
        protein = seq.translate()
        protein_sequences.append(str(protein))
    return protein_sequences

# Função para encontrar a sequência específica de aminoácidos
def find_specific_pattern(protein_sequences):
    pattern = re.compile(r"G[KRH]{2}[DE]G")
    matching_proteins = []
    
    for protein in protein_sequences:
        if pattern.search(protein):
            matching_proteins.append(protein)
    
    return matching_proteins

# Main script
arquivo_dna = f"./{sys.argv[1]}"
dna_sequences = ler_sequencias_dna(arquivo_dna)
protein_sequences = traduzir(dna_sequences)
matching_proteins = find_specific_pattern(protein_sequences)

pasta = "saida" 
seq = Seq(matching_proteins[0])
aux = SeqRecord(seq, id="Spike", description="")
output_path = os.path.join(pasta, "Spike.fasta")
SeqIO.write(aux, output_path, "fasta")
