import os

def solicitar_numero() -> int:
    numero_aleatorio = int(input('Insira um número aleatório: '))
    return numero_aleatorio

def verificar_impar_ou_par(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else: 
        print(f'O número {numero} é impar.')

def main():
    os.system('cls')
    numero_do_usuario = solicitar_numero()
    verificar_impar_ou_par(numero_do_usuario)
    
if __name__ == '__main__':
    main()