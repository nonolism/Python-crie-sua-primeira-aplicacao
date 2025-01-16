def definir_lista() -> list[int]:
    numeros = input('Me diga uma lista de numeros separados por vírgula: ')
    lista = numeros.split(',')
    try:
        lista_int = []
        for item in lista:
            item = int(item)
            lista_int.append(item)
        return lista_int
    except ValueError:
        print('Você inseriu um valor inválido na lista')

def calcular_soma(numeros:list):
    total = 0
    for numero in numeros:
        total = total + numero
    print(f'A soma dos números {numeros} é igual a {total}')

def main():
    numeros = definir_lista()
    calcular_soma(numeros)

if __name__ == '__main__':
    main()