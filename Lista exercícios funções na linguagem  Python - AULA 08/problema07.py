# # Problema 07
# 7. Problema - Ficha de Cadastro 
# Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
# uma função cadastrar_usuario que aceite nome e email como argumentos 
# obrigatórios e qualquer outra informação como kwargs. Imprima todos os 
# dados recebidos. 
# Exemplo de uso: cadastrar_usuario(nome="Ana", email="ana@email.com", 
# idade=30, cidade="Salvador")

def cadastrar_usuario(nome,email,**outros_dados_usuario):
    print(f"Nome: {nome}\nEmail: {email}")

    for chave, valor in outros_dados_usuario.items():
        print(f"{chave}: {valor}")

cadastrar_usuario(nome="Ana", email="ana@email.com", idade=30, cidade="Salvador")
