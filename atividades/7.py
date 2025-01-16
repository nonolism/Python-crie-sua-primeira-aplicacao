lista = [1,2,3,4,5,6,7,8,9,10]
total = 0

for item in lista:
    if item % 2 != 0:
        total = total + item
    print(total)