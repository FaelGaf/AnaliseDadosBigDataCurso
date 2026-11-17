# Atividade 1:

'''O objetivo desta atividade é '''
print("========== Faça seu login para acessar sua conta ==========" )
print()
login_certo = "pablo@escobar"
senha_certa = "1002003"

for i in range(1, 4):

    login = input("Insira seu usuário: ")
    senha = input("Insira sua senha: ")

    if login == login_certo and senha == senha_certa:
        print("Login realizado com sucesso!")
        break
    else:
        print("Login ou senha incorretos.")

if i == 3 and (login != login_certo or senha != senha_certa):
    print("Acesso bloqueado. Por favor, tente novamente.")