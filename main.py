import networkx as nx
import random
import collections
import copy

# criação dos grafos de alunos e de projetos
grafo_alunos = nx.Graph()
grafo_projetos = nx.Graph()

# lista que irá guardar o maior emparelhamento encontrado
emparelhamento_max = []

# função que imprime o emparelhamento e recebe como argumento a lista de vértices de um dos conjuntos de vértices do grafo bipartido, e o grafo bipartido em si
# imprime cada vértice presente na lista passada como argumento, juntamente dos seus vizinhos (que estão no outro conjunto de vértices do grafo bipartido)
# imprime na seguinte ordem: (código do projeto): (códigos dos alunos que estão inscritos no projeto)
def mostra_emparelhamento(lista_vertices: list, grafo_bip: nx.Graph):
    for vertice in lista_vertices:
        lista_vizinhos_vertice = list(grafo_bip.neighbors(vertice))
        if lista_vizinhos_vertice:
            print(f"{vertice}: ", end="")
            for vizinho in range(len(lista_vizinhos_vertice)):
                if vizinho < len(lista_vizinhos_vertice) - 1:
                    print(lista_vizinhos_vertice[vizinho], end=", ")
                else:
                    print(lista_vizinhos_vertice[vizinho])
        else:
            print(f"{vertice}: nenhum aluno")


def cria_grafo_bipartido(grafo_1: nx.Graph, grafo_2: nx.Graph):
    # cria cópias dos grafos, juntamente dos nós, para evitar que a referência original seja alterada
    copia_grafo_1 = copy.deepcopy(grafo_1)
    copia_grafo_2 = copy.deepcopy(grafo_2)
    grafo_bipartido_comp = nx.compose(copia_grafo_1, copia_grafo_2)
    return grafo_bipartido_comp


# função para ordenar uma lista de vértices de alunos passada como argumento, a partir da nota de cada aluno
def sort_lista_nota(lista_unsorted: list, grafo: nx.Graph):
    for a in range(len(lista_unsorted) - 1):
        aluno_atual = grafo.nodes[lista_unsorted[a]]
        prox_aluno = grafo.nodes[lista_unsorted[a + 1]]
        if aluno_atual["nota_media"] > prox_aluno["nota_media"]:
            temp = lista_unsorted[a]
            lista_unsorted[a] = lista_unsorted[a + 1]
            lista_unsorted[a + 1] = temp

def filtra_alunos (lista_alunos:list, grafo:nx.Graph):
    lista_final = []
    for aluno in lista_alunos:
        atributos_aluno = grafo.nodes[aluno]
        nota_aluno = atributos_aluno["nota_media"]
        for projeto in atributos_aluno["preferencia"]:
            atributos_projeto_atual = grafo.nodes[projeto]
            if nota_aluno >= atributos_projeto_atual["nota_minima"]:
                lista_final.append(aluno)
                break
    return lista_final

# função que executa uma variação do algoritmo de Gale-Shapley no grafo passado como argumento, além de receber uma fila que representa a fila de escolhas de um conjunto de vértices do grafo
def gale_shapley(fila: collections.deque, grafo: nx.Graph):
    while (
        len(fila) > 0
    ):  # se o deque não estiver vazio, significa que ainda existem alunos que podem tentar aplicar para algum projeto
        no_aluno, atributos_aluno = fila[0]
        lista_preferencias = atributos_aluno["preferencia"]
        for (
            projeto
        ) in (
            lista_preferencias
        ):  
           # itera pela lista de preferências do aluno, ou seja, pelos projetos que ele ainda pode aplicar
            projeto_grafo = grafo.nodes[
                projeto
            ]  # resgata os atributos do projeto da atual iteração na lista de preferências do aluno
            if (
                atributos_aluno["nota_media"] >= projeto_grafo["nota_minima"]
            ):  # se o projeto ainda possui vagas livres, é feita a atribuição entre aluno e projeto
                if projeto_grafo["vagas"] > 0:
                    projeto_grafo["vagas"] -= 1
                    grafo.add_edge(projeto, no_aluno)
                    grafo.nodes[no_aluno]["preferencia"].remove(
                        projeto
                    )  # projeto removido da lista de preferencia do aluno, para evitar que se itere por ele de novo futuramente
                    break
                else:
                    lista_alunos_escolhidos = list(
                        grafo.neighbors(projeto)
                    ).copy()  # caso o projeto não tenha mais vagas, é feita a iteração por cada aluno inscrito atualmente no projeto
                    sort_lista_nota(lista_alunos_escolhidos, grafo)
                    aluno = lista_alunos_escolhidos[0] #comparando com o aluno de menor nota já alocado no projeto
                    aluno_grafo = grafo_bipartido.nodes[aluno]
                    if (
                        atributos_aluno["nota_media"] > aluno_grafo["nota_media"]
                    ):  # caso o aluno que está aplicando tenha uma nota maior do que algum aluno já inscrito no projeto, é feita a troca
                        grafo.add_edge(projeto, no_aluno)
                        grafo.remove_edge(projeto, aluno)
                        grafo.nodes[no_aluno]["preferencia"].remove(projeto)
                        fila.append((aluno, aluno_grafo))  # adiciona o aluno removido a fila para que ele possa tentar aplicar para algum outro projeto
                        break
                    else:
                        grafo.nodes[no_aluno]["preferencia"].remove(projeto)
            else:
                grafo.nodes[no_aluno]["preferencia"].remove(projeto)  # projeto removido da lista de preferencia do aluno, para evitar que se itere por ele de novo futuramente
        fila.popleft()  # após processar o vértice do aluno, retira ele da fila de escolha


# leitura do arquivo de entrada
arquivo_grafo = open("info.txt", "r")
while True:
    linha = arquivo_grafo.readline()
    if linha == "":
        break
    linha = linha.split(":")
    # leitura dos projetos
    if len(linha) == 1 and linha[0][0] != "/" and linha[0] != "":
        junta_linha = "".join(linha)
        junta_linha = junta_linha.replace("(", "")
        junta_linha = junta_linha.replace(")", "")
        separa_linha = junta_linha.split(",")
        if len(separa_linha) > 1:
            codigo_projeto = separa_linha[0]
            num_vagas = separa_linha[1]
            num_vagas = int(num_vagas)
            min_nota = separa_linha[2]
            min_nota = int(min_nota)
            # adiciona o vértice de projeto ao grafo, com o número máximo de vagas e a nota mínima necessária para o aluno se inscrever
            grafo_projetos.add_node(
                codigo_projeto, vagas=num_vagas, nota_minima=min_nota
            )

    # leitura dos alunos
    elif len(linha) > 1 and linha[0][0] != "/" and linha[0] != "":
        codigo_aluno = linha[0]
        codigo_aluno = codigo_aluno.replace("(", "")
        codigo_aluno = codigo_aluno.replace(")", "")
        separa_linha = linha[1].split(")")
        preferencias = separa_linha[0]
        preferencias = preferencias.replace("(", "")
        preferencias = preferencias.replace(")", "")
        separa_preferencias = preferencias.split(",")
        for i in range(len(separa_preferencias)):
            separa_preferencias[i] = separa_preferencias[i].replace(" ", "")
        media = separa_linha[1]
        media = media.replace("(", "")
        media = media.replace(")", "")
        media = int(media)
        # adiciona o vértice de aluno ao grafo, com a lista de projetos preferidos e a nota do aluno
        grafo_alunos.add_node(
            codigo_aluno, preferencia=separa_preferencias, nota_media=media
        )

grafo_bipartido = nx.Graph()
grafo_bipartido = cria_grafo_bipartido(grafo_alunos, grafo_projetos)
for k in range(10):
    grafo_bipartido = cria_grafo_bipartido(grafo_alunos, grafo_projetos)
    lista_alunos = list(
    grafo_alunos.nodes
    ).copy() 
    lista_alunos= filtra_alunos(lista_alunos,grafo_bipartido) # cria copia da lista de nós no grafo de alunos
    # faz o grafo bipartido compondo as copias dos grafos de alunos e de projetos
    random.shuffle(
        lista_alunos
    )  # embaralha a lista para começar de um novo vértice a cada iteração
    fila_escolha = (
        collections.deque()
    )  # cria deque que é tratado como fila, e adiciona os elementos da lista de alunos embaralhada nele
    for node in lista_alunos:
        fila_escolha.append((node, grafo_alunos.nodes[node]))
    print(f"Iteração {k+1}: ")
    gale_shapley(fila_escolha, grafo_bipartido) #chama a função que realiza o emparelhamento passando a fila de alunos embaralhada e o grafo com alunos e projetos como argumentos
    print(
        f"Emparelhamento encontrado com {len(grafo_bipartido.edges)} vértices: "
    )
    # imprime o emparelhamento encontrada na iteração atual
    mostra_emparelhamento(grafo_projetos.nodes, grafo_bipartido)
    print()
    if len(list(grafo_bipartido.edges)) > len(emparelhamento_max): #caso o emparelhamento achado na atual iteração seja maior que o emparelhamento máximo no momento, é feita a troca
        emparelhamento_max.clear()
        emparelhamento_max = list(grafo_bipartido.edges).copy()

grafo_bipartido.clear_edges()
#adiciona as arestas do emparelhamento máximo encontrado ao grafo bipartido
grafo_bipartido.add_edges_from(emparelhamento_max)
print(f"Emparelhamento máximo estável encontrado com {len(emparelhamento_max)} vértices: ")
mostra_emparelhamento(grafo_projetos.nodes, grafo_bipartido)
