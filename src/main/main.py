from pathlib import Path
from collections import deque
from typing import Dict, List, Optional, Tuple

PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_DIR / "data"
data_dir = DATA_DIR


# Função para ler um grafo de um arquivo
# Substituida pela função get_graph_from_file da interface!


def parse_line(line: str) -> Optional[Tuple[str, str, bool]]:
    """Analisa uma linha do arquivo e retorna os vértices e se é direcionada."""
    line = line.strip()
    if not line:
        return None  # Ignora linhas vazias

    if "->" in line:
        v1, v2 = map(str.strip, line.split("->"))
        return v1, v2, True  # Grafo direcionado
    elif " - " in line:
        v1, v2 = map(str.strip, line.split(" - "))
        return v1, v2, False  # Grafo não direcionado

    return None  # Linha inválida


def detect_graph_type(edges: List[Tuple[str, str, bool]]) -> bool:
    """Determina se o grafo é direcionado ou não."""
    types = {is_directed for _, _, is_directed in edges}
    if len(types) > 1:
        raise ValueError(
            "O arquivo mistura notações de grafos direcionados e não direcionados"
        )
    return types.pop() if types else False  # Padrão para não direcionado


def build_graph(
    edges: List[Tuple[str, str]], is_directed: bool
) -> Dict[str, List[str]]:
    """Constroi o grafo a partir da lista de arestas."""
    graph = {
        vertex: [] for edge in edges for vertex in edge
    }  # Inicializa todos os vértices
    for v, u in edges:
        graph[v].append(u)
        if not is_directed:
            graph[u].append(v)
    print(graph)

    return graph


def get_graph_from_file(file_path: Path) -> Dict[str, List[str]]:
    """
    Lê um grafo de um arquivo e retorna um dicionário representando o grafo.

    O arquivo pode conter um grafo direcionado ("A -> B")
    ou um grafo não direcionado ("A - B").

    Args:
        file_path (Path): Caminho do arquivo contendo o grafo.

    Returns:
        dict: Dicionário representando o grafo.
    """
    edges_with_type = []

    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_line(line)
            if parsed:
                edges_with_type.append(parsed)

    edges = [(v1, v2) for v1, v2, _ in edges_with_type]
    is_directed = detect_graph_type(edges_with_type)
    graph = build_graph(edges, is_directed)

    print(f"Carregado grafo {'direcionado' if is_directed else 'não direcionado'}")

    return graph


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

    return (
        "O grafo é conexo 😁👍"
        if len(visited) == len(graph)
        else "O grafo não é conexo 😢"
    )  # Retorna True se visitou todos os vértices


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

    return (
        "O grafo é conexo 😁👍"
        if len(visited) == len(graph)
        else "O grafo não é conexo 😢"
    )  # Retorna True se visitou todos os vértices


if __name__ == "__main__":
    # Exemplo de uso
    graph = get_graph_from_file(data_dir / "graph_input.txt")
    start = "A"
    print("BFS:", bfs(graph, start))
    print("DFS:", dfs(graph, start))
