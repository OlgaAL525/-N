i = 1
dict1 = {}
while i <= 3:
    date = input('введите дату')
    task = input('введтие задачу')
    dict1.update({date: task})
    i = i + 1
print(dict1)