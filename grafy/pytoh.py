import heapq

def prim(graph, start="A"):
    """
    Algorytm Prima do znajdowania minimalnego drzewa rozpinającego (MST) w grafie ważonym.

    :param graph: Lista sąsiedztwa reprezentująca graf. Format:
                  graph[u] = [(waga, v), ...], gdzie `u` to wierzchołek,
                  `v` to sąsiad `u`, a `waga` to waga krawędzi.
    :param start: Wierzchołek początkowy (domyślnie "A").
    :return: Minimalne drzewo rozpinające jako lista krawędzi [(u, v, waga), ...].
    """
    mst = []  # Minimalne drzewo rozpinające
    visited = set()  # Zbiór odwiedzonych wierzchołków
    min_heap = []  # Kopiec przechowujący krawędzie (waga, u, v)

    # Dodaj krawędzie wychodzące z wierzchołka startowego do kopca
    visited.add(start)
    for v, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, v))

    # Przetwarzaj kopiec do momentu dodania wszystkich wierzchołków do MST
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)  # Pobierz najlżejszą krawędź

        if v not in visited:
            # Dodaj wierzchołek `v` do MST
            visited.add(v)
            mst.append((u, v, weight))

            # Dodaj krawędzie wychodzące z `v` do kopca
            for next_vertex, next_weight in graph[v]:
                if next_vertex not in visited:
                    heapq.heappush(min_heap, (next_weight, v, next_vertex))

    return mst


# Przykład użycia
if __name__ == "__main__":
    # Graf reprezentowany jako lista sąsiedztwa
    graph = {
        "A": [("B", 4), ("C", 2), ("D", 3)],
        "B": [("A", 4), ("C", 2), ("D", 5), ("E", 1)],
        "C": [("A", 2), ("B", 2), ("E", 3)],
        "D": [("A", 3), ("B", 5), ("E", 2)],
        "E": [("B", 1), ("C", 3), ("D", 2)]
    }

    mst = prim(graph)
    print("Minimalne drzewo rozpinające (MST):")
    for edge in mst:
        print(edge)
