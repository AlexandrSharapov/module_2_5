#Цель: закрепить навык написания функций и их вызовов. Задача "Матрица воплоти":

def get_matrix(n, m, value):
    matrix = [] #пустой список внутри функции
    for i in range(n): #первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
        matrix.append([]) #добавляем пустой список в список matrix
                     # Вложенный список - это строка матрицы, элементы вложенных списков(глубже) - это столбцы матрицы.
        for j in range(m): #второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            matrix[i].append(value) #добавляем пустой список значениями value.
    return matrix #возврат значения переменной matrix.

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)


print(result1)
print(result2)
print(result3)