# 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.


def verificar_num():
    numero = False
    while 1:
        try:
            num = float(input(f'Digite um número para saber quais são seus divisores: '))
            numero = True
        except:
            pass

        if numero:
            if num == int(num):
                break
        print('\nO valor digitado não é um número inteiro\n')
    return int(num)



def divisores(num):
    for i in range(1, int(num/2+2)):
        if num % i == 0:
            print(i)

def main():
    divisores(verificar_num())



main()

