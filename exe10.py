# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um
# deles;
# b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função
# Max.


def verificar_num(index):
    numero = False
    while 1:
        try:
            num = float(input(f'Digite o {index}° número: '))
            numero = True
        except:
            pass

        if numero:
            if num == int(num):
                break
        print('\nO valor digitado não é um número inteiro\n')
    return int(num)


# def Max(num): # Jeito prático
#     return max(num)

def Max(num): # Jeito certo
    num1, num2 = num
    maior = num1
    if num1 < num2:
        maior = num2
    return maior

def main():
    for i in range(4):
        num = []
        for j in range(1, 3):
            num.append(verificar_num(j))
        print(f'O maior número dentre ambos é {Max(num)}')



main()
