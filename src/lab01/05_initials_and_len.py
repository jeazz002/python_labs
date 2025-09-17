FIO = input('ФИО: ').split()
answer = ''
for i in range(len(FIO)):
    answer+= FIO[i][0] 
fio_with_spaces = ' '.join(FIO)
length = len(fio_with_spaces)
print('Инициалы:', answer+'.')
print('Длина (символов):', length)