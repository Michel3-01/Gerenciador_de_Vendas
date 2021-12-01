# Descrição: Classe Cliente.
# Contém os atributos dos Clientes.


class Cliente():
    def _init_(self,id,nome,endereco,telefone):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
    # Função da minha classe
    def imprimir(self):
        print(self.id, self.nome, self.endereco, self.telefone)


