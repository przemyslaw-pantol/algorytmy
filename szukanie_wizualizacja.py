from szukanie_metody import linear_search,binary_search,serching_dict,serching_list
import matplotlib.pyplot as plt
import random
from functools import reduce

FILE_PATH = "filtered_words.txt"

def file_read(input_file):
    with open(input_file, 'r') as file:
        lista = file.read().splitlines()
        lista = [word.strip() for word in lista]
    return lista

def lista_filtered(char, list):
    return  list[ord(char)-97]

file = file_read(FILE_PATH)
file.sort()
lista_losowa = [random.choice(file) for _ in range(501)]  
dictionary = serching_dict(file)
lista_podzial = serching_list(file)


total_binarne = [[],[],[]]  
total_liniowe = [[],[],[]]  
total_binarne_czas = [[],[],[]]  
total_liniowe_czas = [[],[],[]] 


for WORD in lista_losowa:
    dictionary_filtered = (dictionary.get(WORD[0]))
    lista_filter = (lista_filtered(WORD[0], lista_podzial))
    
    binarne_bez,time_bin_bez = binary_search(file, WORD, 0, len(file) - 1)
    liniowe_bez,time_lin_bez = linear_search(file, WORD)
    binarne_lista,time_bin_lis = binary_search(lista_filter, WORD, 0, len(lista_filter) - 1)
    liniowe_lista,time_lin_lis = linear_search(lista_filter, WORD)
    binarne_dict,time_bin_dic = binary_search(dictionary_filtered, WORD, 0, len(dictionary_filtered) - 1)
    liniowe_dict,time_lin_dic = linear_search(dictionary_filtered, WORD)

    total_binarne[0].append(binarne_bez)
    total_binarne[1].append(binarne_lista)
    total_binarne[2].append(binarne_dict)

    total_liniowe[0].append(liniowe_bez)
    total_liniowe[1].append(liniowe_lista)
    total_liniowe[2].append(liniowe_dict)

    total_binarne_czas[0].append(time_bin_bez) 
    total_binarne_czas[1].append(time_bin_lis)
    total_binarne_czas[2].append(time_bin_dic)

    total_liniowe_czas[0].append(time_lin_bez)
    total_liniowe_czas[1].append(time_lin_lis)
    total_liniowe_czas[2].append(time_lin_dic)

binarne = [reduce(lambda x,y:x+y,x,0)/500 for x in total_binarne]
liniowe = [reduce(lambda x,y:x+y,x,0)/500 for x in total_liniowe]
binarne_czas = [reduce(lambda x,y:x+y,x,0)/500 for x in total_binarne_czas]
liniowe_czas = [reduce(lambda x,y:x+y,x,0)/500 for x in total_liniowe_czas]

lab_binarne=['Binarne_bez_podziału','Binarne_lista','Binarne_slownik']
lab_liniowe=['Liniowe_bez_podziału','Liniowe_lista','Liniowe_slownik']

fig, axs = plt.subplots(3, 2, figsize=(12, 12))

axs[0, 0].bar(lab_binarne, binarne, color='purple')
axs[0, 0].set_title("Szukanie binarne iteracje")


axs[0, 0].bar_label(axs[0, 0].containers[0])  

axs[0, 1].bar(lab_liniowe, liniowe, color='red')
axs[0, 1].set_title("Szukanie liniowe iteracje")

axs[0, 1].bar_label(axs[0, 1].containers[0])  

bars_binarne_czas = axs[1, 0].bar(lab_binarne, binarne_czas, color='lime')
axs[1, 0].set_title("Szukanie binarne czas (s)")


axs[1, 0].bar_label(bars_binarne_czas, labels=[str(round(value, 10)) for value in binarne_czas])  

bars_liniowe_czas = axs[1, 1].bar(lab_liniowe, liniowe_czas, color='pink')
axs[1, 1].set_title("Szukanie liniowe czas (s)")


axs[1, 1].bar_label(bars_liniowe_czas, labels=([str(round(value, 5)) for value in liniowe_czas]))

axs[2,0].plot(total_binarne[0])
axs[2,0].plot([sum(total_binarne[0])/500 for _ in range(0,501)],color="red")

axs[2,1].plot(total_liniowe[0])
axs[2,1].plot([sum(total_liniowe[0])/500 for _ in range(0,501)],color="red")

plt.subplots_adjust(hspace=0.3, bottom=0.038, top=0.966,left=0.03,right=0.97)
plt.show()