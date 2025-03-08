from pathlib import Path
from collections import deque

PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_DIR / "data"
data_dir = DATA_DIR


# Algoritmo de busca em largura
def bfs(graph, start) -> bool:
    visited = {start}
    queue = deque([start])

    # Lista para armazenar a ordem de visitação
    traversal_order = [start]

    while queue:
        vertex = queue.popleft()

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                traversal_order.append(neighbor)

    # Opcional: imprimir a ordem de travessia
    print(" -> ".join(str(v) for v in traversal_order))

    return len(visited) == len(graph)  # Retorna True se visitou todos os vértices


# Algoritmo de busca em profundidade
def dfs(graph, start) -> bool:
    visited = {start}
    stack = [start]

    traversal_order = [start]

    while stack:
        vertex = stack.pop()

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                traversal_order.append(neighbor)

    print(" -> ".join(str(v) for v in traversal_order))

    return len(visited) == len(graph)  # Retorna True se visitou todos os vértices
