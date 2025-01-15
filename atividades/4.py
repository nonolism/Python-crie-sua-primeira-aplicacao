def solicitar_coordenadas() -> str:
    coordenadas = input('Me diga as cordenadas (x,y) de um ponto: ')
    return coordenadas

def separar_eixos(coordenadas: str) -> int:
    eixo_horizontal,eixo_vertical = coordenadas.split(',')
    eixo_horizontal = int(eixo_horizontal)
    eixo_vertical = int(eixo_vertical)
    return eixo_horizontal, eixo_vertical

def definir_quadrante(x:str, y:str) -> str:
    quadrante = ''
    if x>0 and y>0:
        quadrante = 'Primeiro'
    elif x<0 and y>0:
        quadrante = 'Segundo'
    elif x<0 and y<0:
        quadrante = 'Terceiro'
    elif x>0 and y<0:
        quadrante = 'Quarto'
    else:
        quadrante = 'Ponto de Origem'
    return quadrante

def main():
    coordenadas = solicitar_coordenadas()
    x,y = separar_eixos(coordenadas)
    quadrante = definir_quadrante(x,y)
    print(f'O ponto com as cordenadas X: {x}, e Y: {y}, se encontra no quadrante: {quadrante}')

if __name__ == '__main__':
    main()