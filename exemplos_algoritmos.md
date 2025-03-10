# Exemplos de Execução: DFS vs BFS

Este documento mostra exemplos práticos das diferenças entre os algoritmos de Busca em Profundidade (DFS) e Busca em Largura (BFS).

## Exemplo 1: Grafo em Árvore

Considere o seguinte grafo em formato de árvore:

```
         A
       /   \
      B     C
     / \   / \
    D   E F   G
```

### Código para construir este grafo:

```
A - B
A - C
B - D
B - E
C - F
C - G
```

### Execução do DFS a partir do vértice A:

1. Começamos em A
2. Empilhamos os vizinhos de A: C, B (empilhamos em ordem reversa para explorar B primeiro)
3. Removemos B da pilha e o visitamos
4. Empilhamos os vizinhos de B: E, D
5. Removemos D da pilha e o visitamos (D não tem vizinhos não visitados)
6. Removemos E da pilha e o visitamos (E não tem vizinhos não visitados)
7. Removemos C da pilha e o visitamos
8. Empilhamos os vizinhos de C: G, F
9. Removemos F da pilha e o visitamos (F não tem vizinhos não visitados)
10. Removemos G da pilha e o visitamos (G não tem vizinhos não visitados)

**Ordem de visitação DFS:** A → B → D → E → C → F → G

O DFS segue um caminho até o fim antes de retroceder. Note como ele explora completamente o subgrafo enraizado em B antes de ir para C.

### Execução do BFS a partir do vértice A:

1. Começamos em A
2. Enfileiramos os vizinhos de A: B, C
3. Removemos B da fila e o visitamos
4. Enfileiramos os vizinhos de B: D, E
5. Removemos C da fila e o visitamos
6. Enfileiramos os vizinhos de C: F, G
7. Removemos D da fila e o visitamos (D não tem vizinhos não visitados)
8. Removemos E da fila e o visitamos (E não tem vizinhos não visitados)
9. Removemos F da fila e o visitamos (F não tem vizinhos não visitados)
10. Removemos G da fila e o visitamos (G não tem vizinhos não visitados)

**Ordem de visitação BFS:** A → B → C → D → E → F → G

O BFS visita todos os vértices de um nível antes de passar para o próximo. Note como ele visita todos os vértices à distância 1 de A (B e C) antes de visitar qualquer vértice à distância 2.

## Exemplo 2: Grafo com Múltiplos Caminhos

Considere um grafo mais complexo com múltiplos caminhos entre os vértices:

```
    A --- B --- C
    |     |     |
    |     |     |
    D --- E --- F
    |           |
    |           |
    G --- H --- I
```

### Código para construir este grafo:

```
A - B
B - C
A - D
B - E
C - F
D - E
E - F
D - G
G - H
H - I
F - I
```

### Execução do DFS a partir do vértice A:

1. Começamos em A
2. Empilhamos os vizinhos de A: D, B
3. Removemos B da pilha e o visitamos
4. Empilhamos os vizinhos de B: E, C
5. Removemos C da pilha e o visitamos
6. Empilhamos os vizinhos de C: F
7. Removemos F da pilha e o visitamos
8. Empilhamos os vizinhos de F: I, E (E já está na pilha, então não adicionamos novamente)
9. Removemos I da pilha e o visitamos
10. Empilhamos os vizinhos de I: H
11. Removemos H da pilha e o visitamos
12. Empilhamos os vizinhos de H: G
13. Removemos G da pilha e o visitamos
14. Empilhamos os vizinhos de G: D
15. Removemos D da pilha e o visitamos
16. Empilhamos os vizinhos de D: E, A (A já visitado, E já visitado)
17. Como não há mais vértices não visitados para explorar, o algoritmo termina

**Ordem de visitação DFS:** A → B → C → F → I → H → G → D → E

O DFS segue profundamente por um caminho, explorando completamente um ramo antes de retroceder. Note como ele vai de A até G através do caminho mais profundo antes de retornar para explorar D e E.

### Execução do BFS a partir do vértice A:

1. Começamos em A
2. Enfileiramos os vizinhos de A: B, D
3. Removemos B da fila e o visitamos
4. Enfileiramos os vizinhos de B: C, E
5. Removemos D da fila e o visitamos
6. Enfileiramos os vizinhos de D: E (já na fila, então ignorado), G
7. Removemos C da fila e o visitamos
8. Enfileiramos os vizinhos de C: F
9. Removemos E da fila e o visitamos
10. Enfileiramos os vizinhos de E: F (já na fila, então ignorado)
11. Removemos G da fila e o visitamos
12. Enfileiramos os vizinhos de G: H
13. Removemos F da fila e o visitamos
14. Enfileiramos os vizinhos de F: I
15. Removemos H da fila e o visitamos
16. Enfileiramos os vizinhos de H: I (já na fila, então ignorado)
17. Removemos I da fila e o visitamos

**Ordem de visitação BFS:** A → B → D → C → E → G → F → H → I

O BFS visita os vértices em ordem crescente de distância a partir do vértice inicial. Note como todos os vértices à distância 1 (B, D) são visitados antes de qualquer vértice à distância 2.

## Conclusão

-   **DFS (Busca em Profundidade)**: Explora o mais longe possível ao longo de cada ramo antes de retroceder.

    -   Usa uma estrutura de **pilha** (último a entrar, primeiro a sair)
    -   Pode encontrar caminhos muito profundos rapidamente
    -   Útil para problemas como labirintos, onde é preciso explorar caminhos completos

-   **BFS (Busca em Largura)**: Explora todos os vizinhos no nível atual antes de passar para o próximo nível.
    -   Usa uma estrutura de **fila** (primeiro a entrar, primeiro a sair)
    -   Garante encontrar o caminho mais curto em grafos não ponderados
    -   Útil para problemas que exigem a menor distância ou o menor número de passos
