print("exercício 13")

base = int(input("Digite a base: "))
expoente = int(input("Digite expoente: "))
resul = 1

for i in range(expoente):
    resul = base * base
    resul = base * resul

print(resul)