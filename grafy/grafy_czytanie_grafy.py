file="graf.txt"

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

def spójność(graf: dict):
    nodes = list(graf.keys())
    for x in graf:
        lista=graf.get(x)
        for y in lista:
            if y in nodes:
                nodes.remove(y)
    if len(nodes) == 0:
        return True
    else:
        return False

print(spójność(graf_plik(file)))