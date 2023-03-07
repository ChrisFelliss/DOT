# 2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
# do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
# Área = PI * r2; Perímetro = PI * 2 * r;

from math import pi

def verificar_num():
    numero = False
    while 1:
        try:
            raio = float(input('Digite o valor do raio da circunferncia '))
            numero = True
        except:
            pass

        if numero != True:
            print('O valor digitado não é um número ')
        else:
            break
    return raio

def area(raio):
    a = pi * raio ** 2
    return a


def perimetro(raio):
    p = 2 * pi * raio
    return p

def main():
    raio = verificar_num()
    print(f'{area(raio):.2f}')
    print(f'{perimetro(raio):.2f}')

main()
