# Урок 3. Списки и словари

"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:* 
5
    1 2 3 4 5
    3
    -> 1
"""
count =0
n=int(input("Введите размер N массива: "))
a=[int(i) for i in input('Введите элементы массива через пробел: ').split()]
x=int(input("Введите искомое значение X: "))
for i in range(n):
    if a[i]==x:
        count += 1
print(f'Искомое {x} встречается {count} раз')


"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""
import math
n=int(input("Введите размер N массива: "))
a=[int(i) for i in input('Введите элементы массива через пробел: ').split()]
x=int(input("Введите заданное число X: "))
minOffsetValue=a[0]
minOffset=math.fabs(a[0]-x)
for i in range(1,n):
    if math.fabs(a[i]-x)<minOffset:
        minOffset=math.fabs(a[i]-x)
        minOffsetValue=a[i]
print(minOffsetValue)

"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 
А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; 
Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
либо только русские буквы.
*Пример:*
ноутбук
    12
"""
dictionary_LAT = {'A': '1', 'E': '1', 'I': '1', 'O': '1', 'U': '1', 'L': '1', 'N': '1', 'S': '1', 'T': '1', 'R': '1', 'D': '2',
                  'G': '2', 'B': '3', 'C': '3', 'M': '3', 'P': '3', 'F': '4', 'H': '4', 'V': '4', 'W': '4', 'Y': '4', 'K': '5',
                  'J': '8', 'X': '8', 'Q': '10', 'Z': '10'}
dictionary_CIR = {'А': '1', 'В': '1', 'Е': '1', 'И': '1', 'Н': '1', 'О': '1', 'Р': '1', 'С': '1', 'Т': '1', 'Д': '2', 'К': '2',
                  'Л': '2', 'М': '2', 'П': '2', 'У': '2', 'Б': '3', 'Г': '3', 'Ё': '3', 'Ь': '3', 'Я': '3', 'Й': '4', 'Ы': '4', 'Ж': '5', 'З': '5', 'Х': '5',
                  'Ц': '5', 'Ч': '5', 'Ш': '8', 'Э': '8', 'Ю': '8', 'Ф': '10', 'Щ': '10', 'Ъ': '10'}

user_word = [str(i) for i in input('Введите слово : ').upper()]

sum_Scrabble_LAT = 0
sum_Scrabble_CIR = 0
for i in range(len(user_word)):
    if ord(user_word[i]) >= 65 and ord(user_word[i]) <= 90:
        sum_Scrabble_LAT = sum_Scrabble_LAT+int(dictionary_LAT[user_word[i]])

    elif ord(user_word[i]) >= 1040 and ord(user_word[i]) <= 1071:
        sum_Scrabble_CIR = sum_Scrabble_CIR+int(dictionary_CIR[user_word[i]])

if sum_Scrabble_LAT > 0:
    print(f'стоимость введенного слова=: {sum_Scrabble_LAT}')
if sum_Scrabble_CIR > 0:
    print(f'стоимость введенного слова=: {sum_Scrabble_CIR}')
