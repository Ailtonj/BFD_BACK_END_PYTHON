# Exercicio 7
status_pedido = input(
    "Informe o status do pedido (como 'recebido', 'em_preparação', 'em_entrega' ou 'entregue'):\n")

match status_pedido:
    case "recebido":
        print("Pedido recebido, logo será preparado e depois sairá para a entrega")
    case "em_preparação":
        print("Pedido em preparação, logo sairá para a entrega")
    case "em_entrega":
        print("Pedido ja saiu para a entrega, deve chegar em breve")
    case "entregue":
        print("Pedido ja foi entregue, Obrigado")
    case _:
        print("Status não identificado")
