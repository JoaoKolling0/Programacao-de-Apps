class Veiculo: #Classe que vai englobar as coisas sobre os Veiculos.
    def __init__(self, modelo, preco, ano, quilometragem):
        self.modelo = modelo
        self.preco = preco
        self.ano = ano
        self.quilometragem = quilometragem
    


if __name__ == "__main__":
    objeto_veiculo = Veiculo(modelo = "Saveiro", preco = 400, ano = 2012, quilometragem = 1200)
    print(objeto_veiculo.modelo, objeto_veiculo.preco, objeto_veiculo.ano, objeto_veiculo.quilometragem) 