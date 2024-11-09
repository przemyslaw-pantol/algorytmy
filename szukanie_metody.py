import time

def time_mesure(func):
    def wrapper(*args, **kwargs):
        start=time.perf_counter()
        results=func(*args, **kwargs)
        end=time.perf_counter()
        return [results,end-start]
    return wrapper

@time_mesure
def linear_search(input_list, value):
    i = 0  
    while i < len(input_list):  
        if input_list[i] == value:
            return i  
        i += 1  
    return None  

@time_mesure
def binary_search(input_list, value, start, end):
    i=0
    while start <= end:
        i+=1

        mid = (start + end) // 2
        mid_value=input_list[mid].strip()

        if mid_value== value:
            return  i
        elif mid_value < value:
            start=mid + 1
        else:
            end=mid-1
    return None

def serching_dict(lista):
    dictionary = {}
    for name in lista:
        name = name.strip()
        if name:
            first_letter = name[0]
            if first_letter not in dictionary:
                dictionary[first_letter] = []
            dictionary[first_letter].append(name)
    return dictionary

def serching_list(lista):
    lista_koncowa=[[] for _ in range(26)]
    for name in lista:
        lista_koncowa[ord(name[0])-97].append(name)
    return lista_koncowa
