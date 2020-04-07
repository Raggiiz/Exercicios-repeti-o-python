print("Exercício1")

while True:
    nota = float(input("Digite uma nota: "))
    if nota > 10 or nota < 0:
        print("Nota inválida, digite novamente")
        continue
    else:
        break