estoque = 50

print("1 - Entrada")
print("2 - Saída")
print("3 - Finalizar")

opcao = int(input("Escolha: "))

while opcao == 1 or opcao == 2:
    if opcao == 1:
        quantidade = int(input("Quantidade: "))
        estoque = estoque + quantidade
        print(f"Quantidade adicionada: {quantidade}")
        print(f"Quantidade em estoque: {estoque}")

        print("1 - Entrada")
        print("2 - Saída")
        print("3 - Finalizar")

        opcao = int(input("Escolha: "))

    elif opcao == 2:
        quantidade = int(input("Quantidade: "))
        if quantidade <= estoque:
            estoque = estoque - quantidade
            print(f"Quantidade retirada: {quantidade}")
            print(f"Total em estoque: {estoque}")

            print("1 - Entrada")
            print("2 - Saída")
            print("3 - Finalizar")

            opcao = int(input("Escolha: "))

        else:
            print("Estoque insuficiente!")

            print("1 - Entrada")
            print("2 - Saída")
            print("3 - Finalizar")

            opcao = int(input("Escolha: "))

if opcao == 3:
    print(f"Estoque: {estoque}")
    print("Movimentação encerrada!")

elif opcao < 1 or opcao > 3:
    print("Opção inválida.")
