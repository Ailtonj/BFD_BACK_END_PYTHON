#Bibliotecas
import datetime

#atribuindo a hora atual
hora_atual = datetime.datetime.now()

#Entrada de dados
nome_usuario = input("Digite o seu nome: ")

#Imprimindo valores
print(f'Olá, {nome_usuario}! Agora são {hora_atual.strftime("%H:%M")} horas.')
