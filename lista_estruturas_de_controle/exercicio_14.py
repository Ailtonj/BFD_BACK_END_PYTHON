# Exercicio 14
SENHA = "python123"
while True:
    senha_usuario = input("Informe a senha correta: ")
    if senha_usuario == SENHA:
        print("Senha correta.")
        break
    print("Senha incorreta, tente novamente")