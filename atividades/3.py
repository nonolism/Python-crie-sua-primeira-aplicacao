
import os

USUARIO_MESTRE = 'teste'
SENHA_MESTRA = 'pjus@2022'

def solicitar_credenciais() -> str:
    usuario = input('Me diga seu usuário: ')
    senha = input('Me diga sua senha: ')
    return usuario,senha

def verificar_credenciais(usuario : str, senha : str) -> bool:
    if usuario == USUARIO_MESTRE and senha == SENHA_MESTRA:
        return True
    else:
        print('Usuário e/ou senha incorretos.')
        return False

def main():
    usuario,senha = solicitar_credenciais()
    conectado = verificar_credenciais(usuario, senha)
    if conectado:
        print('Conectado com sucesso ao nosso sistema!')
    else:
        print('Erro ao conectar ao nosso sistema, tente novamente.')

if __name__ == '__main__':
    main()