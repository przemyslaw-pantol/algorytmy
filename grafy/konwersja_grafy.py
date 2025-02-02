matrix = [
    [0,1,1,1],
    [1,0,1,1],
    [1,1,0,0],
    [1,1,0,0]
]

list=[(1, 2), (2, 3), (3, 2)]

dict={1: [2], 2: [3], 3: [2]}

def add_row(matrix):
    matrix.append([0]*len(matrix[0]))
    for list in matrix:
        list.append(0)
    return matrix
    
def del_row(matrix):
    matrix.pop(-1)
    for list in matrix:
        list.pop(-1)
    return matrix

def matrix_to_list(matrix):
    end_list=[]
    for i,list in enumerate(matrix):
        for  j,number in enumerate(list):
            if number == 1:
                end_list.append((i,j))
    return end_list

def matrix_to_dict(matrix):
    dict={}
    for i in range(0,len(matrix)):
        dict[i]=[]
    for i,list in enumerate(matrix):
        for j,number in enumerate(list):
            if number == 1:
                dict[i].append(j)
    return dict

def list_to_matrix(list):
    matrix=[[0]*len(list) for _ in range(len(list))]
    for x in list:
        matrix[x[0]][x[1]]=1
    return matrix

def list_to_dict(list):
    dict={}
    for x in list:
        if x[0] in dict:
            dict[x[0]].append(x[1])
        else:
            dict[x[0]] = x[1]
    return dict

def dict_to_list(dict):
    list=[]
    for key in dict:
        key_data=dict.get(key)
        for num in key_data:
            list.append((key,num))
    return list

def dict_to_matrix(dict):
    am_of_keys=dict.keys()
    matrix=[[0] * len(am_of_keys) for _ in range(len(am_of_keys))]
    for list in dict:
       key_value=dict.get(list)
       for num in key_value:
           matrix[list][num]=1
    return matrix
print(matrix_to_dict(matrix))
