# Exercicio 8
semaforo = input(
    "Informe uma cor do semáforo  (""verde"", ""amarelo"" ou ""vermelho""):\n ")

match semaforo:
    case "verde":
        print("motorista pode passar")
    case "amarelo":
        print("motorista pode passar, mas com atenção")
    case "vermelho":
        print("motorista não pode passar")
    case _:
        print("semaforo inválido")
