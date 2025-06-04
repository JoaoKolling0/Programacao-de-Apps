class Veiculo: #Classe que vai englobar as coisas sobre os Veiculos.
    def __init__(self, modelo, preco, ano, quilometragem):
        self.modelo = modelo
        self.preco = preco
        self.ano = ano
        self.quilometragem = quilometragem
    


if __name__ == "__main__":
    objeto_veiculo = Veiculo(modelo = "Saveiro -", preco = "400 Reais por dia -", ano = 2012, quilometragem = "- 1200 Km Rodados")
    print(objeto_veiculo.modelo, objeto_veiculo.preco, objeto_veiculo.ano, objeto_veiculo.quilometragem)

    objeto_veiculo2 = Veiculo(modelo = "Gol -", preco = "250 Reais por dia -", ano = 1996, quilometragem = "- 2400 Km Rodados")
    print(objeto_veiculo2.modelo, objeto_veiculo2.preco, objeto_veiculo2.ano, objeto_veiculo2.quilometragem)

    objeto_veiculo3 = Veiculo(modelo = "Fusca -", preco = "800 Reais por dia -", ano = 1970, quilometragem = "- 800 Km Rodados")
    print(objeto_veiculo3.modelo, objeto_veiculo3.preco, objeto_veiculo3.ano, objeto_veiculo3.quilometragem)

    objeto_veiculo4 = Veiculo(modelo = "Uno -", preco = "200 Reais por dia -", ano = 1990, quilometragem = "- 3200 Km Rodados")
    print(objeto_veiculo4.modelo, objeto_veiculo4.preco, objeto_veiculo4.ano, objeto_veiculo4.quilometragem)
    