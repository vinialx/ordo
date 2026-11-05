print("Insira os dados para criar seu usuário.")

login = input("Login: ")
senha = input("Senha: ")

print("\nUsuário criado. Insira os dados para realizar o login.")

login_inserido = input("Login: ")
senha_inserido = input("Senha: ")

print("\nResultado do login:")

if login == login_inserido and senha == senha_inserido:
    print("Bem-vindo!")
else:
    print("Acesso negado! Usuário ou senha incorretos.")
