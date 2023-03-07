# 7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro.


def verificar_num(texto):
    numero = False
    while 1:
        try:
            num = float(input(texto))
            numero = True
        except:
            pass
        try:
            num = int(num)
        except:
            pass

        if numero != True:
            print('\nO valor digitado não é um número\n')
        else:
            break
    return num

def fatorial(num):
    bank = num
    for i in range(num-1, 0, -1):
        bank *= i
    return f'O fatorial de {num} é {bank}'


def main():
    print(fatorial(verificar_num('Digite um número para calcular seu fatorial: ')))


main()
