import os

def solicitar_idade():
    idade = int(input('Me diga sua idade por gentileza: '))
    return idade

def classificar_faixa_etaria(idade:int) -> str:
    faixa_etaria:str = ''
    if 0 < idade <= 12:
        faixa_etaria = 'Criança'
    elif 13 <= idade <= 18:
        faixa_etaria = 'Adolescente'
    else:
        faixa_etaria = 'Adulto'
    return faixa_etaria

def main():
    idade = solicitar_idade()
    faixa_etaria = classificar_faixa_etaria(idade)
    print(f'Você tem {idade} anos, e isso te coloca na faixa etaria de {faixa_etaria}.')

if __name__ == '__main__':
    main()