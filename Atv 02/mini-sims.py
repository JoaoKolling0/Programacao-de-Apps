class Personagem: # Classe que vai fazer as coisas sobre o personagem;
    def __init__(self, nome):
        #init é o construtor da classe;
        self.nome = nome
        self.energia = 100
        self.fonme = 100
        self.higiene = 100
        self.social = 100
        self.dinheiro = 160
        self.trabalho = None
        # Os atributos são o que vem após o self.
        
    # Métodos (Ações) abaixo
    def comer (self):
        if self.dinheiro < 10:
            return f"{self.nome} não tem dinheiro para comer"
        else:
            self.nome = min(100, self.fome + 20)
            self.dinheiro -= 8
            return f"{self.nome} se almentou"
        
    def dormir (self):
        if self.energia < 60:
            return f"{self.nome} está começando a se sentir cansado"
        else:
            self.nome = min(100, self.energia + 40)
            return f"{self.nome} dormiu um pouco"
    
    def banho (self):
        pass
    
    def trabalhar (self):
        pass
    
    def socializar (self):
        pass
        
if __name__ == "__main__":
    # Criar um objeto para o personagem
    obj1 = Personagem("Laura Caixão")
    
    print(obj1.nome)
    print(obj1.fome)
    
    obj2 = Personagem("Buddy")
    
    print(obj2.nome)
    obj2.fome -= 10
    print(obj2.fome)
    
    