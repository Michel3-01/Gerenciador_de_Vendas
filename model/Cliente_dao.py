# Padrão DAO (Data Access Object).
# Centraliza o acesso aos dados dos objetos cliente.

Lista_Cliente = []

# Adicionar novo Cliente.
def Add(novo_cliente):
    Lista_Cliente.append(novo_cliente)
# Editar Cliente.
def Edit():
    pass
# Excluir Cliente.
def Delete():
    pass
#Lista todos os clientes.
def listAll():
    for c in Lista_Cliente:
        c.imprimir()