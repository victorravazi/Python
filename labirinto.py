from queue import PriorityQueue

# Labirinto: 0 = livre, 1 = obstáculo
maze = [
    [0,0,0,0,1],
    [1,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0]
]

start = (0,0)
goal = (4,4)


# Neste caso, usamos a distância de Manhattan (soma das diferenças absolutas das coordenadas)
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# Algoritmo A* para encontrar o caminho mais curto
def astar(maze, start, goal):
    # Lista de nós a serem explorados, priorizados pelo custo estimado total (f_score)
    open_list = PriorityQueue()
    # Adicionamos o ponto de partida com custo 0
    open_list.put((0, start))

    # Dicionário para rastrear de onde viemos para reconstruir o caminho
    came_from = {}

    # Dicionário para armazenar o custo do caminho do início até cada nó
    g_score = {start: 0}

    # Enquanto houver nós para explorar na lista aberta
    while not open_list.empty():
        # Pegamos o nó com o menor custo estimado total (g_score)
         current = open_list.get()

        # Se chegamos ao objetivo, refazemos e retornamos o caminho
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1] # Retorna o caminho na ordem correta

        # Vizinhos possíveis (cima, baixo, esquerda, direita)
        neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
        for dx, dy in neighbors:
            # Calcula as coordenadas do vizinho
            neighbor = (current[0] + dx, current[1] + dy)

            # Verifica se o vizinho está dentro dos limites do labirinto e não é um obstáculo
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == 0:
                # Calcula o custo do caminho do início até este vizinho através do nó atual
                tentative_g = g_score[current] + 1

                # Se este caminho para o vizinho for o melhor encontrado até agora
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    # Atualiza o custo g_score para o vizinho
                    g_score[neighbor] = tentative_g
                    # Calcula o custo estimado total (f_score = g_score + heurística)
                    f_score = tentative_g + heuristic(neighbor, goal)
                    # Adiciona o vizinho à lista aberta com seu f_score
                    open_list.put((f_score, neighbor))
                    # Registra que viemos do nó atual para chegar a este vizinho
                    came_from[neighbor] = current
    # Se a lista aberta estiver vazia e não encontramos o objetivo, não há caminho
    return None

# Executa o algoritmo A* e imprime o caminho encontrado
path = astar(maze, start, goal)
print("Caminho encontrado:", path)
