frase = 'uma frase de teste com varias palavras repetidas só que não só algumas, tipo uma'
dicionario = {}
palavras = frase.split()
for palavra in palavras:
    if palavra not in dicionario:
        dicionario[f'{palavra}'] = 1
    else:
        dicionario[f'{palavra}'] += 1

for chave, valor in dicionario.items():
    print(f'A palavra "{chave}" aparece {valor} vezes')