# 1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.

def verificar_num():
    numero = False
    while 1:
        try:
            num = float(input('Digite um número inteiro '))
            numero = True
        except:
            pass

        if numero == True:
            if num == int(num):
                break
        print('O valor digitado não é um número inteiro')
    return num

def im_par(num):
    if num % 2 ==0:
        return 'Par'
    else:
        return 'Impar'

def main():
    print(im_par(verificar_num()))

main()
