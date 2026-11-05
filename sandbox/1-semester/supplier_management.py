nome = input("Nome do fornecedor: ")
contato = input("Contato: ")
endereco = input("Endereço: ")
cnpj = input("CNPJ: ")

print(f"Fornecedor: {nome}")
print(f"Contato: {contato}")
print(f"Endereço: {endereco}")
print(f"CNPJ: {cnpj}")

opcao = input("Deseja corrigir o cadastro?")

while opcao == "sim":
    nome = input("Nome do fornecedor: ")
    contato = input("Contato: ")
    endereco = input("Endereço: ")
    cnpj = input("CNPJ: ")

    print(f"Fornecedor: {nome}")
    print(f"Contato: {contato}")
    print(f"Endereço: {endereco}")
    print(f"CNPJ: {cnpj}")

    opcao = input("Deseja corrigir o cadastro?")

if opcao == "nao":
    print("Fornecedor cadastrado!")
