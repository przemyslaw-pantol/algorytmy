graf_wagi = {
    "A": [("B", 4), ("C", 2), ("D", 3)],
    "B": [("A", 4), ("C", 2), ("D", 5), ("E", 1)],
    "C": [("A", 2), ("B", 2), ("E", 3)],
    "D": [("A", 3), ("B", 5), ("E", 2)],
    "E": [("B", 1), ("C", 3), ("D", 2)]
}

keys = list(graf_wagi.keys())
start = keys[0]  # Startujemy od wierzchołka "A"
visited = [start]  # Lista odwiedzonych wierzchołków
edges = []  # Lista krawędzi 

while len(visited) < len(keys):
    smalest_edge = None
    for x in visited:  # Sprawdzamy wszystkie wierzchołki już odwiedzone
        for y in graf_wagi[x]:  # Przechodzimy po wszystkich sąsiadach
            if y[0] not in visited: 
                if smalest_edge is None or y[1] < smalest_edge[2]:
                    smalest_edge = (x, y[0], y[1])  # (wierzchołek_start, wierzchołek_koniec, waga)

    if smalest_edge:  # Dodajemy wierzchołek i krawędź
        visited.append(smalest_edge[1])
        edges.append(smalest_edge)
        smalest_edge = None

print("Odwiedzone wierzchołki:", visited)
print("Krawędzie w minimalnym drzewie rozpinającym:", edges)
