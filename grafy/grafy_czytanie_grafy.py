file="graf_2.txt"

def graf_plik(file_path):
    with open(file_path,"r") as file:
        graf={}
        lista = file.read().splitlines()
        for x in lista:
            if x:
                graf[x[0]]=[]
                for y in x[1:]:
                    if y not in graf:
                        graf[y] = []
                        graf[x[0]].append(y)
                    else:
                        graf[x[0]].append(y)
    return graf

def spójność(graf):
    wierzchołki = list(graf.keys())
    
    odwiedzone = []
    q = []
    
    start = wierzchołki[0] 
    odwiedzone.append(start)
    q.append(start)
    
    while q:
        obecny = q[0]
        q.pop(0)
        for x in graf.get(obecny):
            if x not in odwiedzone:
                odwiedzone.append(x)
                q.append(x)

    return len(odwiedzone) == len(wierzchołki)

print(graf_plik(file))
print(spójność(graf_plik(file)))