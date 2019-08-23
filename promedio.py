cant=int(input("cuantos numeros va a digitar: "))
suma=0
for i in range(1, cant+1):
    num=int(input("digite un numero: "))
    suma=suma+num


promedio= suma/cant
print("el promedio es: ", promedio)