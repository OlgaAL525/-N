def count_letter(list_,letter):
    count_ = 0
    for i in list_:
        if letter in i:
            count_ += 1
    return count_

list_1 = ['солнце', 'море', 'параход']
let = 'я'
print(count_letter(list_1,let))

