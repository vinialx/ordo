nome = input("Nome do usuário: ")
login = input("Login: ")
senha = input("Senha: ")

print("\nDados para conferência:")
print(f"Nome: {nome}")
print(f"Login: {login}")

opcao = input("\nDeseja corrigir o cadastro? ").lower().replace("ã", "a")

while opcao == "sim":
    nome = input("Nome do usuário: ")
    login = input("Login: ")
    senha = input("Senha: ")

    print("\nDados para conferência:")
    print(f"Nome: {nome}")
    print(f"Login: {login}")

    opcao = input("\nDeseja corrigir o cadastro? ").lower().replace("ã", "a")
    print("\nUsuário atualizado!")

if opcao == "nao":
    print("\nUsuário cadastrado!")
