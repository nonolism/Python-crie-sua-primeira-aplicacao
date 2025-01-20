import os

restaurantes:list[dict] =   [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                            {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                            {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    '''Exibe o nome do sistema'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Exibe as opções para o usuário'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    '''Redireciona o usuário ao menu principal após digitar uma tecla'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def exibir_subtitulo(texto:str):
    '''Limpa a tela do sistema e exibe um subtitulo
    
    Input:
    - texto(str): texto que será mostrado como subtítulo
    
    Output:
    - subtítulo estilizado'''
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(f'{texto}')
    print(linha)
    print('\n')

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Input:
    - Nome do restaurante (string)
    - Categoria (string)
    
    Output:
    - Adiciona um novo restaurantes a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Lista os restaurantes cadastrados no sistema
    
    
    Output:
    
    - Uma lista dos restaurantes cadastrados, informando:
        - nome
        - categoria 
        - estado
    '''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """
    Busca pelo nome de um restaurante em uma lista e altera seu estado.

    Parâmetros:
    - nome_restaurante (str): Nome do restaurante a ser localizado.

    Retorno:
    - Sucesso: Altera o estado do restaurante (exemplo: ativo <-> inativo).
    - Erro: Retorna uma mensagem informando que o restaurante não foi encontrado.
    """
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaunte_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaunte_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaunte_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal()

def finalizar_app():
    '''Encerra o programa'''
    exibir_subtitulo('Finalizando app')

def opcao_invalida():
    '''Informa ao usuário que a opção selecionada é invalida e o redireciona ao menu principal'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Recebe o input do usuário que vai o redirecionar pra uma das opções disponíveis
    
    Input:
    - opcao_escolhida(int): Opção escolhida pelo usuário
    
    Output:
    - Sucesso: Redireciona o usuário pra uma das opções disponíveis
    - Erro: Redireciona o usuário para o metodo opcao_invalida'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal do sistema, onde o codigo é iniciado.
    
    Orquestra toda a estrutura de como os outros metodos serão chamados.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()