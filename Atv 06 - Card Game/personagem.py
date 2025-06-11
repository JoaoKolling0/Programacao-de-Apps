class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida_max = 100
        self.vida = 100
        
    def falar_nome(self):
        return f"Olá, meu nome é {self.nome}"
    