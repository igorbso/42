# README.txt

## Instru��es de Uso dos Scripts

Este conjunto de scripts foi desenvolvido para realizar diversas an�lises em sequ�ncias de DNA e prote�nas. Abaixo, segue descri��o e instru��es de uso para cada um dos scripts.

### 1. 42.py

Este � o script principal que coordena a execu��o dos scripts auxiliares (a.py, b.py, c.py, d.py). Ele extrai uma sequ�ncia de DNA a partir de um arquivo FASTA e a processa usando os scripts auxiliares.

**Como executar:**

py 42.py -i <caminho_para_arquivo_FASTA>


### 2. a.py

Este script calcula o tamanho e o conte�do GC da sequ�ncia de DNA.

**Como executar:**

Este script � chamado automaticamente pelo `42.py` e n�o necessita ser executado separadamente.

### 3. b.py

Este script gera k-mers (fragmentos de sequ�ncia) de 31 nucleot�deos a partir da sequ�ncia de DNA e os salva em um arquivo FASTA.

**Como executar:**

Este script � chamado automaticamente pelo `42.py` e n�o necessita ser executado separadamente.

### 4. c.py

Este script identifica ORFs (Open Reading Frames), extrai as CDSs (Coding Sequences) e salva cada CDS em arquivos FASTA separados.

**Como executar:**

Este script � chamado automaticamente pelo `42.py` e n�o necessita ser executado separadamente.

### 5. d.py

Este script traduz as sequ�ncias de DNA em prote�nas, procura por padr�es espec�ficos de amino�cidos e salva a sequ�ncia correspondente em um arquivo FASTA.

**Como executar:**

Este script � chamado automaticamente pelo `42.py` e n�o necessita ser executado separadamente.

### 6. e.py

Este script � utilizado para gerar mapas de dist�ncia e contato de uma prote�na a partir de um arquivo PDB. Ele deve ser executado separadamente do script principal.

**Como executar:**

```bash
py e.py <caminho_para_arquivo_PDB>
```

### Notas Adicionais

- Certifique-se de ter todos os scripts e os arquivos necess�rios no diret�rio correto antes de executar o `42.py`.
- O `42.py` espera que os scripts auxiliares (a.py, b.py, c.py, d.py) estejam localizados na pasta `./lib/`.
- Os resultados gerados pelos scripts ser�o salvos em pastas nomeadas `saida` e `cds`.

### Requisitos

- Python 3
- BioPython
- MDAnalysis
- Matplotlib
- Numpy

Instale os pacotes necess�rios com o seguinte comando:

```bash
pip install biopython MDAnalysis matplotlib numpy
```
