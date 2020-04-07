print("exercício 2")

senha = ""
nome = ""

while senha == nome:
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    if senha == nome:
        print("A senha não pode ser igual o nome")

print(f"Seu nome é {nome} e sua senha é {senha}")
