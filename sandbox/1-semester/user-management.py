nome = input("Nome do usuário: ")
login = input("Login: ")
senha = input("Senha: ")

print(f"Nome: {nome}")
print(f"Login: {login}")

opcao = input("Deseja corrigir o cadastro?")

while opcao == "sim":
    nome = input("Nome do usuário: ")
    login = input("Login: ")
    senha = input("Senha: ")

    print(f"Nome: {nome}")
    print(f"Login: {login}")

    opcao = input("Deseja corrigir o cadastro?")
    print("Usuário atualizado!")

if opcao == "nao":
    print("Usuário cadastrado!")
