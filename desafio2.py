def funcao():
    num = int(input())
    for j in range(2, num+1):

        var = j
        divisores = []
        for i in range(1, int(var/2+2)):
            if var % i == 0:
                divisores.append(i)
        if sum(divisores) == var:
            print(f'O número {var} é perfeito')
        if var % 1000 == 0:
            print (var)
funcao()
