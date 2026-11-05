nome = input("Nome do cliente: ")
contato = input("Contato: ")
endereco = input("Endereço: ")

print(f"Nome: {nome}")
print(f"Contato: {contato}")
print(f"Endereço: {endereco}")

opcao = input("Deseja corrigir o cadastro?")

while opcao == "sim":
    nome = input("Nome do cliente: ")
    contato = input("Contato: ")
    endereco = input("Endereço: ")

    print(f"Nome: {nome}")
    print(f"Contato: {contato}")
    print(f"Endereço: {endereco}")

    opcao = input("Deseja corrigir o cadastro?")
    print("Cadastro atualizado")

if opcao == "nao":
    print("Cliente cadastrado!")
