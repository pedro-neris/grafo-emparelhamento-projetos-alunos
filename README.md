# SOBRE O PROJETO
O seguinte projeto tem como objetivo, dado um arquivo contendo informações sobre projetos e alunos, fazer a leitura desse arquivo e produzir um programa em Python que realiza um **emparelhamento estável máximo** entre o conjunto de alunos e o conjunto de projetos.

---

# OBJETIVO
Dado um arquivo (`"info.txt"`) contendo informações sobre projetos e alunos, o programa realiza a leitura desse arquivo e fornece as seguintes informações:
- **Alocação (emparelhamento)** de alunos a projetos, respeitando preferências e requisitos.
- Impressão na tela das **10 iterações de emparelhamento**.
- Impressão na tela do **emparelhamento máximo e estável** ao final das 10 iterações.

---

# ITERAÇÕES
É executado um algoritmo para encontrar um emparelhamento **10 vezes**. É utilizada a biblioteca **random** do Python para embaralhar a lista de alunos e inseri-la na fila, o que traz grandes chances de sempre executar o algoritmo em ordens diferentes. Os resultados de cada iteração são exibidos da seguinte forma na tela:

- **Número da iteração**
- **"EMPARELHAMENTO FINAL ENCONTRADO COM (número de vértices do emparelhamento final) VÉRTICES"**
  - A seguir, são mostrados os pares **Projeto x Aluno** finais encontrados na iteração, na seguinte formatação:
    - Quando há aluno(s) alocado(s) no projeto:  
      `"(código do projeto): (código(s) do(s) aluno(s) alocado(s))"`
    - Quando não há nenhum aluno alocado no projeto:  
      `"(código do projeto): nenhum aluno"`

---

# EMPARELHAMENTO MÁXIMO ESTÁVEL
Ao final das 10 iterações, é comparada qual iteração obteve o maior emparelhamento; daí, é retirado o emparelhamento com maior número de vértices, que é considerado o **emparelhamento máximo** (a estabilidade é garantida pelo algoritmo de emparelhamento). O emparelhamento máximo é mostrado na tela da seguinte forma:

- **"Emparelhamento máximo estável encontrado com (número de vértices do emparelhamento máximo) vértices:"**
  - Quando há aluno(s) alocado(s) no projeto:  
    `"(código do projeto): (código(s) do(s) aluno(s) alocado(s))"`
  - Quando não há nenhum aluno alocado no projeto:  
    `"(código do projeto): nenhum aluno"`

---

# REQUISITOS PARA FUNCIONAMENTO
Para o funcionamento correto do código, o arquivo (`"info.txt"`) contendo as informações sobre os alunos e os projetos deve estar na mesma pasta do arquivo do programa (`"main.py"`), e o programa deve ser executado nesta pasta.  

- **Python** deve estar instalado, além do gerenciador de pacotes **pip**.  
  - Link para instalação do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
  - Para instalar o pip, execute o seguinte comando no terminal do dispositivo:  
    ```bash
    python get-pip.py
    ```  
    *(Da versão 3.4 para frente do Python, o pip já está incluído na instalação)*  

- A biblioteca **NetworkX** também deve ter sido baixada.  
  - Comando para instalação (executar no terminal do dispositivo):  
    ```bash
    pip install networkx
    ```  


---

# COMO EXECUTAR O PROGRAMA
1. Navegue até o diretório contendo o arquivo do programa (`"main.py"`) e o arquivo com as informações do grafo (`"info.txt"`) no terminal.  
2. Ao chegar ao diretório, digite e execute o comando:  
   ```bash
   python main.py
   ```
---
   
# DOCUMENTAÇÃO DO NETWORKX
- NetworkX: networkx.org/documentation



