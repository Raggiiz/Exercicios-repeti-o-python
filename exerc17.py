print ("exercício 17")

numero = int(input("Digite um número: "))
count1 = 0
count = 1
while count1 < numero:
    fatorial = numero * (numero - count)
    count = count - 1
    count1 = count + 1

print(fatorial)