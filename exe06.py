# 6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.


def verificar_num(texto):
    numero = False
    while 1:
        try:
            num = float(input(texto))
            numero = True
        except:
            pass

        if numero != True:
            print('\nO valor digitado não é um número\n')
        else:
            break
    return num

def poligono(dados):
    lados, medida = dados
    if lados == 3:
        figura = 'Triângulo'
        m_edida = medida * 3
    if lados == 4:
        figura = 'Quadrado'
        m_edida = medida ** 2
    if lados == 5:
        figura = 'Pentágono'
        m_edida = ''
    return m_edida, figura


def main():
    lados = verificar_num('Quantos lados tem o polígono regular? ')
    medida = verificar_num('Qual a medida do lado(cm)? ')
    valor, figura = poligono((lados, medida))
    print(figura.upper())
    print(valor)


main()
