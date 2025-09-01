# problema 2
# 2. Problema - Cadastro de Alunos  
# Crie um arquivo .py. Escreva um código que vai armazenar a sequência 
# 'Bruno', 'Ana', 'Carlos', 'Denise', 'Felipe' de alunos em uma estrutura de dados 
# do tipo lista chamada alunos. Pense no seguinte cenário, você precisa 
# modificar essa lista, mostrando os nomes dos alunos em ordem decrescente 
# e você deve acessar a posição dos alunos(as) Felipe e Ana e mostrar na tela 
# o nome desses alunos. 
alunos = ['Bruno', 'Ana', 'Carlos', 'Denise', 'Felipe']
alunos.sort(reverse=True)
i = alunos.index("Felipe")
j = alunos.index("Ana")
print(alunos)
print(alunos[i])
print(alunos[j])
