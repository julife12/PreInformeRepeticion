cant=int(input("cuantos numeros va a digitar: "))
for i in range(1, cant):
    if i%2==0:
        print(-i)
    else:
        print(i)