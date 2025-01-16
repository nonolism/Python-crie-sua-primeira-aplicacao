def solicitar_numero() -> int:
    try:
        numero = int(input('Me diga um número inteiro: '))
        return numero
    except ValueError:
        print('Valor inserido inválido')

def montar_tabuada(valor):
    for i in range(1, 11):
        print(f'{valor} x {i} = {valor * i}')

def main():
    valor = solicitar_numero()
    montar_tabuada(valor)
    
if __name__ == '__main__':
    main()