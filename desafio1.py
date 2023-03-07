def funcao():
    var  = int(input())
    divisores = []
    print(var)
    for i in range(1, int(var/2+2)):
        print(i)
        if var % i == 0:
            divisores.append(i)
    print(divisores)
    if sum(divisores) == var:
        print(f'O número {var} é perfeito')
    else:
        print(f'O número {var} não é perfeito')

funcao()
