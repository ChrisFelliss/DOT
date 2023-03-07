# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def verificar_sn():
    string = True
    while 1:
        sn = input('Deseja continuar? [S/N]\n'), None
        try:
            if sn == None:
                string = False
            else:
                sn = sn[0]
            sn == float(sn)
            string = False
        except:
            pass
        if string and sn[:1].upper() == 'S':
            sn = True
            break
        elif string and sn[:1].upper() == 'N':
            sn = False
            break
        print('Comando inválido\nDigite S ou N\n')
    return sn


def verificar_num():
    numero = False
    while 1:
        try:
            num = float(input('Digite um número para saber seu cubo: '))
            numero = True
        except:
            pass

        if not numero:
            print('\nO valor digitado não é um número\n')
        else:
            break
    return num


def cubo(num):
    return f'\nO cubo de {num} é igual a {num ** 3}\n'


def main():
    print(cubo(verificar_num()))
    while 1:
        if verificar_sn():
            print(cubo(verificar_num()))
        else:
            break


main()

