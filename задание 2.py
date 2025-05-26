i = 1
list1 = []
while i <= 3:
    date = input('введите дату')
    task = input('введтие задачу')
    list1.append(date + task)
    i = i + 1
j = 0
while j <= 2:
    print(list1[j])
    j = j + 1