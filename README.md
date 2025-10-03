# python_labs

#Лабораторная работа 1

## Задание 1
```py
name = str(input("Имя:"))
age = int(input("возраст:"))
print("Привет,", f'{name}''!', ' Через год тебе будет', age+1)
```
![Картинка 1](./images/lab01/01.png)

## Задание 2
```py
a = input("a: ")
cleaned_string = a.replace(",", ".")
float_a = float(cleaned_string)
b = float(input("b:"))
print("sum=", float_a + b, ";", "avg=", round(((float_a + b) / 2), 2))
```
![Картинка 2](./images/lab01/02.png)
## Задание 3
```py
price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print('База после скидки: 'f'{base:.2f}''₽')
print('НДС: 'f'{vat_amount:.2f}''₽')
print('Итого к оплате: 'f'{total:.2f}''₽')
```
![Картинка 3](./images/lab01/03.png)
## Задание 4
```py
m = int(input('Минуты: '))
hours = m//60
minute = m%60
print(f'{hours}:{minute:02d}')
```
![Картинка 4](./images/lab01/04.png)
## Задание 5
```py
FIO = input('ФИО: ').split()
answer = ''
for i in range(len(FIO)):
    answer+= FIO[i][0] 
fio_with_spaces = ' '.join(FIO)
length = len(fio_with_spaces)
print('Инициалы:', answer+'.')
print('Длина (символов):', length)
```
![Картинка 5](./images/lab01/05.png)
## Задание 6
```py
N = int(input('Количество студентов: '))
count_true = 0
count_false = 0
for i in range(N):
    data = input().split()
    format = data[3]
    if format == 'True':
        count_true += 1
    else: count_false += 1
print('очно/заочно:', count_true, count_false)
```
![Картинка 6](./images/lab01/06.png)

#Лабораторная работа 2
## Задание 1
#1 min_max
```py
array1 = [3, -1, 5, 5, 0]
array2 = [42]
array3 = [-5, -2, -9]
array4 = [1.5, 2, 2.0, -3.1]
def min_max(nums: list[float | int]):
    n =[a for a in nums]
    return min(nums),max(nums)
print(min_max(array1), min_max(array2), min_max(array3), min_max(array4))
```
#2 unique_sorted
```py
array1 = [3, 1, 2, 1, 3]
array2 = [-1, -1, 0, 2, 2]
array3 = [1.0, 1, 2.5, 2.5, 0]
def unique_sorted(nums: list[float | int]):
    n =[a for a in nums]
    return sorted(set(nums))
print(unique_sorted(array1), unique_sorted(array2), unique_sorted(array3),)
```
#3 flatten
```py
array1 = [[1, 2], [3, 4]]
array2 = [[1, 2], (3, 4, 5)]
array3 = [[1], [], [2, 3]]
def flatten(mat: list[list | tuple]):
    answer = []
    for n in mat:
        for y in n:
            answer += [y]
    return answer
print(flatten(array1), flatten(array2), flatten(array3),)
```
![Картинка 1](./images/lab01/lab02/01.png)
## Задание 2
```py
#1 transpose
def transpose(mat: list[list[float | int]]):
    return [list(x) for x in zip(*mat)]
array1=[[1,2,3]]
array2=[[1],[2],[3]]
array3=[[1,2],[3,4]]
print(transpose(array3),transpose(array2),transpose(array1))
#2 row_sums
array1=[[1,2,3],[4,5,6]]
array2=[[-1,1],[10,-10]]
def row_sums(mat: list[list[float | int]]):
    res=[sum(x) for x in mat]
    return res
print(row_sums(array1),row_sums(array2))
#3 col_sums
array1=[[1,2,3],[4,5,6]]
array2=[[-1,1],[10,-10]]
array3=[[0,0],[0,0]]
def col_sums(mat: list[list[float | int]]):
    return [sum(x) for x in zip(*mat)]
print(col_sums(array1),col_sums(array2), col_sums(array3))
```
![Картинка 2](./images/lab01/lab02/02.png)
## Задание 3
```py
def format_record(rec: tuple[str, str, float]):
    fio, group, gpa = rec
    fio = " ".join(fio.strip().split())
    group = group.strip()
    parts = fio.split()
    surname = parts[0].title()
    initials = ""
    if len(parts) > 1:
        for name in parts[1:3]:
            initials += name[0].upper() + "."
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"
rec = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("  cидорова  анна   сергеевна ", "ABB-01", 3.999)
]
for x in rec:
    print(format_record(x)) 
```
![Картинка 3](./images/lab01/lab02/03.png)