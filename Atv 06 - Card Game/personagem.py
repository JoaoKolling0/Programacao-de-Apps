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
    
class Cartas:
    def __init__(self, cartas,ver_lista_cartas, comprar_carta):
        self.cartas = cartas 
        self.ver_lista_cartas = ver_lista_cartas
        self.comprar_carta = comprar_carta