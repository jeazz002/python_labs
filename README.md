# python_labs

#Лабораторная работа 1

## Задание 1
```
name = str(input("Имя:"))
age = int(input("возраст:"))
print("Привет,", f'{name}''!', ' Через год тебе будет', age+1)
```
![Картинка 1](./images/lab01/01.png)

## Задание 2
```
a = input("a: ")
cleaned_string = a.replace(",", ".")
float_a = float(cleaned_string)
b = float(input("b:"))
print("sum=", float_a + b, ";", "avg=", round(((float_a + b) / 2), 2))
```
![Картинка 2](./images/lab01/02.png)
## Задание 3
```
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
```
m = int(input('Минуты: '))
hours = m//60
minute = m%60
print(f'{hours}:{minute:02d}')
```
![Картинка 4](./images/lab01/04.png)
## Задание 5
```
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
```
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