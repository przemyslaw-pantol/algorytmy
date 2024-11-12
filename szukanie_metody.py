import time
'''
Dekorator mierzący czas wykonania funkcji.
Działa, opakowując oryginalną funkcję w dodatkową logikę mierzenia czasu.
Po wywoładniu funkcji zapisuje czas rozpoczęcia i zakończenia, a następnie oblicza różnicę.
Zwraca listę zawierającą wynik funkcji oraz czas wykonania.
'''

def time_mesure(func):
    def wrapper(*args, **kwargs):
        start=time.perf_counter()
        results=func(*args, **kwargs)
        end=time.perf_counter()
        return [results,end-start]
    return wrapper

'''
Funkcja realizujca wyszukiwanie liniowe.
Przeszukuje listę od początku do końca, porównując każdy element z wartością, której szukamy.
-jeśli znajdzie element pasujący, zwraca jego indeks.
-jeśli nie znajdzie, zwraca None.

Wyszukiwanie liniowe jest prostym algorytmem, ale może być nieefektywne 
przy dużych listach, ponieważz sprawdza każdy element po kolei.
'''

@time_mesure
def linear_search(input_list, value):
    i = 0  
    while i < len(input_list):  
        if input_list[i] == value:
            return i  
        i += 1  
    return None  

'''
Funkcja realizująca wyszukiwanie binarne.
Działa na posortowanej liście, co pozwala na szybsze znalezienie wartości.
W każdym kroku dzieli zakres poszukiwań na pół:
- jeśli wartość poszukiwana jest rónwa środkowemu elementowi, zwraca liczbę iteracji.
- jeśli wartość poszukiwana jest mniejsza, przeszukuje lewą połowę.
- jeśli wartość poszukiwna jest większa, przeszukuje lewą połowę.

Funkcja zwraca liczbę iteracji potrzebnych do znalezienia wartości lub None, jeśli wartość nie istnieje.

'''

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

'''
Funkcja grupująca elementy listy w słowniku na podstawie ich pierwszej litery.
-Klucz w słowniku to pierwsza litera (np. 'a', 'b', ... )
-Wartość to lista wszystkich elementów zaczynających się na tę literę.

Funckja iteruje przez podaną listę, usuwa zbędne białe znaki i organizuje elementy w grupy.
Przydaje się do szybkiego wyszukiwania elementów na podstawie ich pierwszej litery.
'''

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

'''
Funkcja grupująca elementy listy w liście list, gdzie każda podlista odpowiada jednej literze alfabetu (a-z)
- Tworzy 26 pustych list, odpowiadających literom 'a' do 'z'.
- Dodaje każdy element listy wejściowej do odpowiedniej podlisty na podstawie pierwszej litery eleemtnu
'''

def serching_list(lista):
    lista_koncowa=[[] for _ in range(26)]
    for name in lista:
        lista_koncowa[ord(name[0])-97].append(name)
    return lista_koncowa
