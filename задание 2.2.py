HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход."""

today = []
tomorrow = []
other = []
tasks = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    task = input("Введите название задачи: ")
    date = input('Ввдите срок выполнения задачи: ')
    if date == 'Сегодня':
      today.append(task)
    elif date == 'Завтра':
      tomorrow.append(task)
    else:
      other.append(task)
    tasks.append(task)
    print(today, tasks)
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    break
  else:
    print("Неизвестная команда")
    break

print("До свидания!")