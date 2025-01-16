lista = [1]

total = 0
for item in lista:
    if item:
        total = total + item

try:
    media = total / len(lista)
except ZeroDivisionError:
    print('Lista vazia')

print(media)