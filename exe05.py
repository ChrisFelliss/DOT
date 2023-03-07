# 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
# que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
# - para homens : (72.7 * h) – 58
# - para mulheres : (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima).


def verificar_num(texto, conf):
    numero = False
    while 1:
        try:
            num = float(input(texto))
            numero = True
        except:
            pass

        if numero != True:
            print('\nO valor digitado não é um número\n')
        elif conf and not 1 <= num <= 2:
            print('Código incorreto')
        else:
            break
    return num

def altura(dados):
    if dados[1] == 1:
        peso_ideal = 62.1 * dados[0] - 44.7
    if dados[1] == 2:
        peso_ideal = 72.7 * dados[0] - 58
    return peso_ideal


def main():
    h = verificar_num('Digite sua altura:', False)
    sexo = verificar_num('\nDigite o seu sexo usando o seguinte código:\n1 - Feminino\n2 - Masculino', True)
    print(f'Seu peso ideal é {altura((h, sexo))}')


main()
