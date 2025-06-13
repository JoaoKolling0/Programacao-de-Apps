class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida_max = 100
        self.vida = 100
        self.pontos_ataque = 8
        self.pontos_defesa = 2
        self.mao_de_cartas = []
        self.energia_max = 10
        self.energia = 10
        
    def falar_nome(self):
        return f"Olá, meu nome é {self.nome}"
    
class Carta:
    def __init__(self, nome, descricao, energia_gasta):
        self.nome = nome
        self.descricao = descricao
        self.energia_gasta = energia_gasta
        
    def usar(self):
        pass
    
class CartaDano(Carta):
    def __init__(self, nome, descricao, energia_gasta, ponto_dano):
        super().__init__(nome, descricao, energia_gasta)
        self.pontos_de_dano = ponto_dano
        
    def usar(self, oponente: Personagem):
        oponente.vida -= self.pontos_de_dano
        return f"O(a) oponente {oponente.nome} recebeu {self.pontos_de_dano} de dano"
    
        
        