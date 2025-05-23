class Personagem: #classe que vai fazer as coisas sobre o personagem;
    def __init__(self, nome):
        #init é o construtor da classe;
        self.nome = nome
        self.energia = 100
        self.fonme = 100
        self.higiene = 100
        self.dinheiro = 160
        self.trabalho = None
        
if __name__ == "__main__":
    # Criar um objeto para o personagem
    obj1 = Personagem("Laura Caixão")
    