# 9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
# no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.


def verificar_num(index):
    numero = False
    while 1:
        try:
            num = float(input(f'Digite o {index}° número: '))
            numero = True
        except:
            pass

        if not numero:
            print('\nO valor digitado não é um número\n')
        else:
            break
    return num


# def Sum(num): # Jeito prático
#     return sum(num)

def Sum(num): # Jeito certo
    num1, num2 = num
    return num1 + num2

def main():
    num = []
    for j in range(1, 3):
        num.append(verificar_num(j))
    print(f'A soma dos números é {Sum(num)}')



main()

