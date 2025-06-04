class Veiculo: #Classe que vai englobar as coisas sobre os Veiculos.
    def __init__(self, modelo, preco, ano, quilometragem):
        self.modelo = modelo
        self.preco = preco
        self.ano = ano
        self.quilometragem = quilometragem
    
class Cliente:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

class Locacao:
    def __init__(self, cliente, carro, valor, forma_pagamento, data, quantidade_de_dias):
        self.cliente = cliente
        self.carro = carro
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.data = data
        self.quantidade_de_dias = quantidade_de_dias

if __name__ == "__main__":
    objeto_veiculo = Veiculo(modelo = "Saveiro -", preco = "400 Reais por dia -", ano = 2012, quilometragem = "- 1200 Km Rodados")
    print(objeto_veiculo.modelo, objeto_veiculo.preco, objeto_veiculo.ano, objeto_veiculo.quilometragem)

    objeto_veiculo2 = Veiculo(modelo = "Gol -", preco = "250 Reais por dia -", ano = 1996, quilometragem = "- 2400 Km Rodados")
    print(objeto_veiculo2.modelo, objeto_veiculo2.preco, objeto_veiculo2.ano, objeto_veiculo2.quilometragem)

    objeto_veiculo3 = Veiculo(modelo = "Fusca -", preco = "800 Reais por dia -", ano = 1970, quilometragem = "- 800 Km Rodados")
    print(objeto_veiculo3.modelo, objeto_veiculo3.preco, objeto_veiculo3.ano, objeto_veiculo3.quilometragem)

    objeto_veiculo4 = Veiculo(modelo = "Uno -", preco = "200 Reais por dia -", ano = 1990, quilometragem = "- 3200 Km Rodados")
    print(objeto_veiculo4.modelo, objeto_veiculo4.preco, objeto_veiculo4.ano, objeto_veiculo4.quilometragem)

    print("")

    objeto_cliente = Cliente(nome = "Ednaldo Pereira -", cpf = "Cpf: 669.355.740-64 -", endereco = "Amegakure -", telefone = "+99 (666) 40028922")
    print(objeto_cliente.nome, objeto_cliente.cpf, objeto_cliente.endereco, objeto_cliente.telefone)

    objeto_cliente2 = Cliente(nome = "Senku -", cpf = "Cpf: 669.355.666-64 -", endereco = "Arkhan -", telefone = "+99 (666) 900000000")
    print(objeto_cliente2.nome, objeto_cliente2.cpf, objeto_cliente2.endereco, objeto_cliente2.telefone)
    
