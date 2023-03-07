# 13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.

def verificar_num():
    numero = False
    while 1:
        try:
            num = float(input(f'Digite um número para saber qual o resultado da fórmula: '))
            numero = True
        except:
            pass

        if numero:
            if num == int(num):
                break
        print('\nO valor digitado não é um número inteiro\n')
    return int(num)


def divisoria(num):
    bank = 1
    for i in range(2, num+1):
        bank += 1/i
    return bank


def main():
    print(divisoria(verificar_num()))



main()

