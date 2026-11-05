nome = input("Nome do cliente: ")
contato = input("Contato: ")
endereco = input("Endereço: ")

print("\nDados para conferência:")
print(f"Nome: {nome}")
print(f"Contato: {contato}")
print(f"Endereço: {endereco}")

opcao = input("\nDeseja corrigir o cadastro? ").lower().replace("ã", "a")

while opcao == "sim":
    nome = input("Nome do cliente: ")
    contato = input("Contato: ")
    endereco = input("Endereço: ")

    print("\nDados para conferência:")
    print(f"Nome: {nome}")
    print(f"Contato: {contato}")
    print(f"Endereço: {endereco}")

    opcao = input("\nDeseja corrigir o cadastro? ").lower().replace("ã", "a")
    print("\nCadastro atualizado")

if opcao == "nao":
    print("\nCliente cadastrado!")
