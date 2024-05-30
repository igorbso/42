import sys
arquivo = open(sys.argv[1])
texto = arquivo.read()

def tamnho_e_gc(fasta):
    from Bio.SeqUtils import gc_fraction
    bases = 0
    for i in fasta:
        bases += 1
    gc = (gc_fraction(fasta))
    gc = round(gc*100)
    print(f"O genoma possui {bases} nucleotídeos e conteúdo GC de {gc}%")
    return fasta

resultado = tamnho_e_gc(texto)