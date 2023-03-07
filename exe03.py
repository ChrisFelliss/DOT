# 3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar
# o valor correspondente em graus Celsius.
# Fórmula: C = ((F-32)/9)*5


def verificar_num():
    numero = False
    while 1:
        try:
            temp = float(input('Digite a temperatura(Fº): '))
            numero = True
        except:
            pass

        if numero != True:
            print('O valor digitado não é um número ')
        else:
            break
    return temp

def celcius(temp):
    c = ((temp - 32)/9)*5
    return c


def main():
    temp = verificar_num()
    print(f'{celcius(temp):.1f}')

main()
