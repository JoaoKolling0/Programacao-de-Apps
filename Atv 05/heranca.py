class Animal:
    def __init__(self, nome_cientifico):
        self.nome_cientifico = nome_cientifico
        
    def falar(self):
        print("Sou um animal genérico")
        
class Cachorro(Animal): # O "Animal" entre parenteses diz que "Cachorro" herda da classe "Animal";
    
    def __init__(self, nome_cientifico, racao_favorita):
        self.nome_cientifico = nome_cientifico
        self.racao_favorita =  racao_favorita
        
if __name__ == "__main__":
    objeto_cachorro = Cachorro("Canis lupus familiaris", )