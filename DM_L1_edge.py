# Задача про покриття. Метод граничного перебору

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

# номер покриття
i = 0

#  множина покриттів
P = {}


# Основний код
def main():
    # якщо D - покриття то запам'ятати D
    if P_actions(0):
        P_actions(1)
    
    # Початок основного циклу
    while True:    
        find_j() # Знайти j
            
        # якщо j  дорінює N
        if j == N:
            D.pop(f"A{N}") # Видалити A(N) 
            
            # Якщо D не пуста множина
            if D:
                find_j() # Знайти j
                D.pop(f"A{j}") # Видалити A(j) 
                D[f"A{j+1}"] = globals()[f"A{j+1}"] # Додати A(j+1) в D 
                
            # Якщо D пуста множина: зупинити цикл 
            else:
                break
            
        # Якщо j не дорівнює N
        else:
            # Якщо D - покриття: видалити A(j) з D 
            if P_actions(0): 
                D.pop(f"A{j}")
            D[f"A{j+1}"] = globals()[f"A{j+1}"] # Додати A(j+1) в D 
            
        # Якщо D - покриття
        if P_actions(0):
            
            # Запам'ятати надлишкові покриття
            p_to_del = []
            for p in P:
                indexes = P[p][0]
                if all(x in indexes for x in D):
                    p_to_del.append(p)
                    global i
                    i -= 1
            
            # Видалити надлишкові покриття
            for p in p_to_del:
                P.pop(p)
                
            # Запам'ятати D як P(i)
            P_actions(1)
    
    # відсортувати покриття по кількості та ціні
    sorted_l = sorted(P.items(), key = lambda x: int(x[1][1]))
    sorted_a = sorted(P.items(), key = lambda x: int(x[1][2]))

    # вивести покриття з найменшою кількістю
    print(f"покриття з найменшою кількістю ({sorted_l[0][1][1]}):  {sorted_l[0][0]} =", "{", end="")
    for i in range(len(sorted_l[0][1][0])):
        if i != len(sorted_l[0][1][0]) - 1:
            print(f"{sorted_l[0][1][0][i]},", end="")
        else:
            print(f"{sorted_l[0][1][0][i]}", end="")
    print("}")

    # вивести покриття з найменшою ціною
    print(f"покриття з найменшою ціною ({sorted_a[0][1][2]}):  {sorted_a[0][0]} =", "{", end="")
    for i in range(len(sorted_a[0][1][0])):
        if i != len(sorted_a[0][1][0]) - 1:
            print(f"{sorted_a[0][1][0][i]},", end="")
        else:
            print(f"{sorted_a[0][1][0][i]}", end="")
    print("}")


# Допоміжні функції

# Функція для знажодження j
def find_j():
    
    global j
    for j in range(N,0,-1):
        try:
            globals()['D'][f"A{j}"]
            break
        except:
            pass

# функція для визначення або запам'ятовування P
def P_actions(remember):
    
    element_sum = [0] * len(A1)
    elements = []
    
    for element in D:
        elements.append(element)
        element_sum = [sum(i) for i in zip(element_sum, D[element])]
        
    if remember:
        l = len(D)
        a = element_sum[len(element_sum) - 1]
        global i
        i += 1
        P[f"P{i}"] = ([elements, l, a])  
        return
        
    if all(element > 0 for element in element_sum):
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()
