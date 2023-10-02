#Sem-08-T2-Q1 Somar um valor diferente para números pares ou ímpares

x= int(input())

if x %2 == 0:
    par= x + 5
    print(par)
elif x %2 != 0:
    impar= x + 8
    print(impar)