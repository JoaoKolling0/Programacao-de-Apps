class Personagem: # A classe que age sob o personagem
    def __init__(self, nome, status):
        self.nome = nome
        self.status = status
        self.vida_max = 100
        self.vida = 100
        self.pontos_ataque = 4
        self.pontos_defesa = 2
        self.mao_de_cartas = [] # Os colchetes (isso = []) é uma "lista";
        self.energia_max = 10
        self.energia = 10
        
    def falar_nome(self): # Atributo que age sob o nome do personagem(ou personagens);
        return f"Olá, meu nome é {self.nome}"
    
class Carta: # A classe que age sob as cartas;
    def __init__(self, nome, descricao, energia_gasta):
        self.nome = nome
        self.descricao = descricao
        self.energia_gasta = energia_gasta
        
    def usar(self): # O atributo que age para o comando de "usar" no "Main";
        pass
    
class CartaDano(Carta): # A classe onde age sob as cartas de dano;
    def __init__(self, nome, descricao, energia_gasta, ponto_dano):
        super().__init__(nome, descricao, energia_gasta)
        self.pontos_de_dano = ponto_dano
        
    def usar(self, oponente: Personagem): # O atributo que age sob a carta no "main";
        oponente.vida -= self.pontos_de_dano
        return f"O(a) oponente {oponente.nome} recebeu {self.pontos_de_dano} de dano"
    
class CartaCura(Carta): # A classe onde age sob as cartas de cura;
    def __init__(self, nome, descricao, energia_gasta, ponto_vida_curada):
        super().__init__(nome, descricao, energia_gasta)
        self.ponto_de_vida_curada = ponto_vida_curada
        
    def usar(self, personagem: Personagem):
        personagem.vida += self.ponto_de_vida_curada
        return f"{personagem.nome} teve {self.ponto_de_vida_curada} de vida restaurada"
    
class CartaRoubo(Carta): # A classe onde age sob as cartas de roubo;
    def __init__(self, nome, descricao, energia_gasta, roubar_carta):
        super().__init__(nome, descricao, energia_gasta)
        self.roubar_carta = roubar_carta
    
    
    def usar(self, oponente: Personagem):
        oponente.mao_de_cartas = self.roubar_carta
        return f"{oponente.nome} teve {self.roubar_carta} cartas roubadas"
    
class CartaStun(Carta): # A classe onde age sob as cartas de stun;
    def __init__(self, nome, descricao, energia_gasta, carta_de_stun):
        super().__init__(nome, descricao, energia_gasta)
        self.carta_de_stun = carta_de_stun
        
    def usar(self, oponente: Personagem):
        oponente.status = self.carta_de_stun
        return f"{oponente.nome} está {self.carta_de_stun}"
    
class CartaAumento(Carta): # A classe onde age sob as cartas de buff de atributos de personagem;
    def __init__(self, nome, descricao, energia_gasta, tipo: Personagem, pts_aumentado):
        super().__init__(nome, descricao, energia_gasta)
        self.tipo = tipo
        self.pts_aumentado = pts_aumentado
        
    def usar(self, personagem: Personagem):
        personagem.pontos_ataque += self.pts_aumentado
        return f"{personagem.nome} aumentou {self.pts_aumentado} de {self.tipo}"
    
class Partida: # A classe que age sob a Partida;
    def __init__(self, turno, jogador1, jogador2, jogador_atual):
        
        self.turno = turno
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogador_atual = jogador_atual
        
    def iniciar(self):
        pass
    
    def trocar_turno(self, verificar_jogador):
        self.verificar_jogador = verificar_jogador
    
    def trocar_jogador(self):
        pass
    
    def acabar(self):
        pass