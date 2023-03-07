# 4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
# notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
# foi aprovado (considere 6.0 a média mínima para aprovação).


def verificar_num():
    numero = False
    notas = []
    for i in range(1, 3):
        while 1:
            try:
                nota = float(input(f'Digite a {i}º nota: '))
                numero = True
            except:
                pass

            if numero != True:
                print('O valor digitado não é um número ')
            else:
                notas.append(nota)
                break
    return notas

def media_nota(notas):
    media = sum(notas)/2
    return media


def main():
    notas= verificar_num()
    media = media_nota(notas)
    if media >= 6:
        print('PARABÉNS! Você foi aprovado!')
    print(media)

main()
