# Задача про покриття. Метод повного перебору

# 7 підмножин A
N = 7

# варіант завдання - 8
A1 = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
A2 = [0, 1, 0, 1, 0, 0, 1, 0, 1, 3]
A3 = [0, 0, 0, 1, 1, 0 ,0, 1, 1, 2]
A4 = [0, 0, 1, 0, 0, 1, 0, 0, 1, 2]
A5 = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
A6 = [1, 0, 1, 1, 0, 0, 0, 0, 0, 2]
A7 = [1, 0, 1, 0, 1, 1, 0, 1, 0, 3]

# можливе покриття
D = {"A1": A1}

# номер можливого покриття
i = 0

# місце в якому будуть усі підмножини D
D_elements = {}
D_indexes = {}

# функція для знаходження j
def find_j():
    global j
    for j in range(N,0,-1):
        try:
            globals()['D'][f"A{j}"]
            break
        except:
            pass

# заповнення D_elements та D_indexes
while True:
    # збільшити номер елемента на 1
    i += 1
    
    # запам'ятати підмножину
    elements = []
    indexes = []
    for element in D:
        elements.append(D[element])
        indexes.append(element)
    D_elements[f"D{i}"] = elements
    D_indexes[f"D{i}"] = indexes

    # знайти j
    find_j()
    
    # опрацювання D
    if j != N:
        D[f"A{j+1}"] = globals()[f"A{j+1}"]
    else:
        D.pop(f"A{N}")
        
        if D:
            find_j()
            D.pop(f"A{j}")
            D[f"A{j+1}"] = globals()[f"A{j+1}"]
        else:
            break

# множина покриттів
P = []

# заповнити множину покриттів
while True:
    if i > 0:        
        element_sum = [0] * len(A1)
        for element in D_elements[f"D{i}"]:
            element_sum = [sum(i) for i in zip(element_sum, element)] 
        
        if all(element > 0 for element in element_sum):
            l = len(D_elements[f"D{i}"])
            a = element_sum[len(element_sum) - 1]
            P.append([D_indexes[f"D{i}"], l, a])
            
        i -= 1
    else:
        break
    
# відсортувати покриття по кількості та ціні
sorted_l = sorted(P, key = lambda x: int(x[1]))
sorted_a = sorted(P, key = lambda x: int(x[2]))

# вивести покриття з найменшою кількістю
print(f"покриття з найменшою кількістю ({sorted_l[0][1]}): ", "{", end="")
for i in range(len(sorted_l[0][0])):
    if i != len(sorted_l[0][0]) - 1:
        print(f"{sorted_l[0][0][i]},", end="")
    else:
        print(f"{sorted_l[0][0][i]}", end="")
print("}")

# вивести покриття з найменшою ціною
print(f"покриття з найменшою ціною ({sorted_a[0][2]}): ", "{", end="")
for i in range(len(sorted_a[0][0])):
    if i != len(sorted_a[0][0]) - 1:
        print(f"{sorted_a[0][0][i]},", end="")
    else:
        print(f"{sorted_a[0][0][i]}", end="")
print("}")
