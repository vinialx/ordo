nome = input("Nome do fornecedor: ")
contato = input("Contato: ")
endereco = input("Endereço: ")
cnpj = input("CNPJ: ")

print("\nDados para conferência:")
print(f"Fornecedor: {nome}")
print(f"Contato: {contato}")
print(f"Endereço: {endereco}")
print(f"CNPJ: {cnpj}")

opcao = input("\nDeseja corrigir o cadastro? ").lower().replace("ã", "a")

while opcao == "sim":
    nome = input("Nome do fornecedor: ")
    contato = input("Contato: ")
    endereco = input("Endereço: ")
    cnpj = input("CNPJ: ")

    print("\nDados para conferência:")
    print(f"Fornecedor: {nome}")
    print(f"Contato: {contato}")
    print(f"Endereço: {endereco}")
    print(f"CNPJ: {cnpj}")

    opcao = input("\nDeseja corrigir o cadastro? ").lower().replace("ã", "a")

if opcao == "nao":
    print("\nFornecedor cadastrado!")
