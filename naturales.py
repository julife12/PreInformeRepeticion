#escriba un algoritmo que imprima los numeros naturales contenidos entre dos numeros n-m
a=int(input("por favor digite el primer numero del rango: "))
b=int(input("por favor digite el ultimo numero del rago: "))
for i in range(a,b+1):
    if i>=0:
        print(i)