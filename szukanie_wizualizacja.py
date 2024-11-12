from szukanie_metody import linear_search, binary_search, serching_dict, serching_list
import matplotlib.pyplot as plt
import random

# Ścieżka do pliku z danymi tekstowymi
FILE_PATH = "filtered_words.txt"

def file_read(input_file):
    """
    Funkcja odczytująca dane z pliku tekstowego.
    - Zwraca listę słów, usuwając białe znaki (spacje, nowe linie) z każdego słowa.
    """
    with open(input_file, 'r') as file:
        lista = file.read().splitlines()  # Odczyt linii
        lista = [word.strip() for word in lista]  # Usuwanie zbędnych znaków
    return lista

def lista_filtered(char, list):
    """
    Filtruje listę list, wybierając tę grupę, która zaczyna się od określonej litery.
    - char: litera, na podstawie której filtrujemy.
    - list: lista list grupowanych według pierwszej litery.
    - Zwraca posortowaną podlistę lub False, jeśli brak pasującej grupy.
    """
    for group in list:
        if group[0][0] == char:  # Szukanie grupy zaczynającej się na literę
            group.sort()
            return group
    return False

# Przygotowanie danych
file = file_read(FILE_PATH)  # Odczyt słów z pliku
file.sort()  # Posortowanie listy słów
lista_losowa = [random.choice(file) for _ in range(501)]  # Generowanie losowych słów z pliku
dictionary = serching_dict(file)  # Grupowanie słów w słowniku
lista_podzial = serching_list(file)  # Grupowanie słów w liście list

# Tablice sumujące wyniki wyszukiwań i czasów
total_binarne = [0, 0, 0]  # Iteracje dla różnych wersji wyszukiwania binarnego
total_liniowe = [0, 0, 0]  # Iteracje dla różnych wersji wyszukiwania liniowego
total_binarne_czas = [0, 0, 0]  # Czas dla różnych wersji wyszukiwania binarnego
total_liniowe_czas = [0, 0, 0]  # Czas dla różnych wersji wyszukiwania liniowego
wariancja_iter_binarne = []  # Iteracje dla każdego wyszukiwania binarnego
wariancja_iter_liniowe = []  # Iteracje dla każdego wyszukiwania liniowego

# Pętla testująca efektywność wyszukiwania na losowych słowach
for WORD in lista_losowa:
    dictionary_filtered = (dictionary.get(WORD[0]))  # Słownik dla danej litery
    lista_filter = (lista_filtered(WORD[0], lista_podzial))  # Lista z grupą dla danej litery
    
    # Testy wyszukiwania binarnego i liniowego
    binarne_bez, time_bin_bez = binary_search(file, WORD, 0, len(file) - 1)
    liniowe_bez, time_lin_bez = linear_search(file, WORD)
    binarne_lista, time_bin_lis = binary_search(lista_filter, WORD, 0, len(lista_filter) - 1)
    liniowe_lista, time_lin_lis = linear_search(lista_filter, WORD)
    binarne_dict, time_bin_dic = binary_search(dictionary_filtered, WORD, 0, len(dictionary_filtered) - 1)
    liniowe_dict, time_lin_dic = linear_search(dictionary_filtered, WORD)

    # Zbieranie danych iteracji
    total_binarne[0] += binarne_bez
    total_binarne[1] += binarne_lista
    total_binarne[2] += binarne_dict
    wariancja_iter_binarne.append(binarne_bez)

    total_liniowe[0] += liniowe_bez
    total_liniowe[1] += liniowe_lista
    total_liniowe[2] += liniowe_dict
    wariancja_iter_liniowe.append(liniowe_bez)

    # Zbieranie danych czasów
    total_binarne_czas[0] += time_bin_bez
    total_binarne_czas[1] += time_bin_lis
    total_binarne_czas[2] += time_bin_dic

    total_liniowe_czas[0] += time_lin_bez
    total_liniowe_czas[1] += time_lin_lis
    total_liniowe_czas[2] += time_lin_dic

# Obliczanie średnich wyników iteracji i czasów
binarne = [x / 500 for x in total_binarne]
liniowe = [x / 500 for x in total_liniowe]
binarne_czas = [x / 500 for x in total_binarne_czas]
liniowe_czas = [x / 500 for x in total_liniowe_czas]

# Etykiety dla wykresów
lab_binarne = ['Binarne_bez_podziału', 'Binarne_lista', 'Binarne_slownik']
lab_liniowe = ['Liniowe_bez_podziału', 'Liniowe_lista', 'Liniowe_slownik']

# Tworzenie wykresów
fig, axs = plt.subplots(3, 2, figsize=(12, 12))

# Wykres 1: Średnia liczba iteracji dla wyszukiwania binarnego
axs[0, 0].bar(lab_binarne, binarne, color='purple')
axs[0, 0].set_title("Szukanie binarne iteracje")
axs[0, 0].bar_label(axs[0, 0].containers[0])

# Wykres 2: Średnia liczba iteracji dla wyszukiwania liniowego
axs[0, 1].bar(lab_liniowe, liniowe, color='red')
axs[0, 1].set_title("Szukanie liniowe iteracje")
axs[0, 1].bar_label(axs[0, 1].containers[0])

# Wykres 3: Średni czas wyszukiwania binarnego
bars_binarne_czas = axs[1, 0].bar(lab_binarne, binarne_czas, color='lime')
axs[1, 0].set_title("Szukanie binarne czas (s)")
axs[1, 0].bar_label(bars_binarne_czas, labels=[str(round(value, 10)) for value in binarne_czas])

# Wykres 4: Średni czas wyszukiwania liniowego
bars_liniowe_czas = axs[1, 1].bar(lab_liniowe, liniowe_czas, color='pink')
axs[1, 1].set_title("Szukanie liniowe czas (s)")
axs[1, 1].bar_label(bars_liniowe_czas, labels=[str(round(value, 5)) for value in liniowe_czas])

# Wykres 5: Wariancja liczby iteracji dla wyszukiwania binarnego
axs[2, 0].set_title("Wariancja liczby iteracji - binarne")
axs[2, 0].plot(wariancja_iter_binarne)
axs[2, 0].plot([total_binarne[0] / 500 for _ in range(0, 501)], color="red")

# Wykres 6: Wariancja liczby iteracji dla wyszukiwania liniowego
axs[2, 1].set_title("Wariancja liczby iteracji - liniowe")
axs[2, 1].plot(wariancja_iter_liniowe)
axs[2, 1].plot([total_liniowe[0] / 500 for _ in range(0, 501)], color="red")

# Dostosowanie wykresów
plt.subplots_adjust(hspace=0.3, bottom=0.038, top=0.966, left=0.03, right=0.97)
plt.show()
