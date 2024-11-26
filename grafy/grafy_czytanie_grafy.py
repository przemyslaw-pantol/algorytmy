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

print(graf_plik(file))