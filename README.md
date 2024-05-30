# README.txt

## Instruções de Uso dos Scripts

Este conjunto de scripts foi desenvolvido para realizar diversas análises em sequências de DNA e proteínas. Abaixo, segue descrição e instruções de uso para cada um dos scripts.

### 1. 42.py

Este é o script principal que coordena a execução dos scripts auxiliares (a.py, b.py, c.py, d.py). Ele extrai uma sequência de DNA a partir de um arquivo FASTA e a processa usando os scripts auxiliares.

**Como executar:**

py 42.py -i <caminho_para_arquivo_FASTA>


### 2. a.py

Este script calcula o tamanho e o conteúdo GC da sequência de DNA.

**Como executar:**

Este script é chamado automaticamente pelo `42.py` e não necessita ser executado separadamente.

### 3. b.py

Este script gera k-mers (fragmentos de sequência) de 31 nucleotídeos a partir da sequência de DNA e os salva em um arquivo FASTA.

**Como executar:**

Este script é chamado automaticamente pelo `42.py` e não necessita ser executado separadamente.

### 4. c.py

Este script identifica ORFs (Open Reading Frames), extrai as CDSs (Coding Sequences) e salva cada CDS em arquivos FASTA separados.

**Como executar:**

Este script é chamado automaticamente pelo `42.py` e não necessita ser executado separadamente.

### 5. d.py

Este script traduz as sequências de DNA em proteínas, procura por padrões específicos de aminoácidos e salva a sequência correspondente em um arquivo FASTA.

**Como executar:**

Este script é chamado automaticamente pelo `42.py` e não necessita ser executado separadamente.

### 6. e.py

Este script é utilizado para gerar mapas de distância e contato de uma proteína a partir de um arquivo PDB. Ele deve ser executado separadamente do script principal.

**Como executar:**

```bash
py e.py <caminho_para_arquivo_PDB>
```

### Notas Adicionais

- Certifique-se de ter todos os scripts e os arquivos necessários no diretório correto antes de executar o `42.py`.
- O `42.py` espera que os scripts auxiliares (a.py, b.py, c.py, d.py) estejam localizados na pasta `./lib/`.
- Os resultados gerados pelos scripts serão salvos em pastas nomeadas `saida` e `cds`.

### Requisitos

- Python 3
- BioPython
- MDAnalysis
- Matplotlib
- Numpy

Instale os pacotes necessários com o seguinte comando:

```bash
pip install biopython MDAnalysis matplotlib numpy
```
