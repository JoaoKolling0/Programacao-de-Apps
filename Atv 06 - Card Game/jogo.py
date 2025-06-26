from personagem import Personagem, Carta, CartaDano, CartaCura, CartaRoubo, CartaStun, CartaAumento
import random

nome = input("Digite seu nome: ")

objeto_personagem1 = Personagem(nome = nome, status = "bem")
mensagem = objeto_personagem1.falar_nome()
print(mensagem)

print("")

nome = input("Nome do Adversário: ")

objeto_personagem2 = Personagem(nome = nome, status = "bem")
mensagem = objeto_personagem2.falar_nome()
print(mensagem)

print("")

# Criar baralho com as cartas existentes;
baralho = [] # Lista é feita usando colchetes (lista é feita com colchetes, exemplo: Cartas "[]");

objeto_cartadano1 = CartaDano(nome = "Air Slash", descricao = "Lança um corte feito de vento na direção do oponente", energia_gasta = 2, ponto_dano = 8)
baralho.append(objeto_cartadano1) # O .append coloca o Objeto na lista;

objeto_cartadano2 = CartaDano(nome = "Pulso de Sangue", descricao = "Lança uma especie de feixe feito de sangue", energia_gasta = 6, ponto_dano = 24)
baralho.append(objeto_cartadano2)

objeto_cartadano3 = CartaDano(nome = "Espada Relâmpago", descricao = "O personagem carrega a espada com Raios e teleporta atras do adversário fazendo um corte com a espada", energia_gasta = 4, ponto_dano = 16)
baralho.append(objeto_cartadano3)

objeto_cartadano4 = CartaDano(nome = "Corte Corrompido", descricao = "O personagem sacrifica sua honra por um momento para atacar o adversário com sua espada agora corrompida", energia_gasta = 2, ponto_dano = 8)
baralho.append(objeto_cartadano4)

objeto_cartacura1 = CartaCura(nome = "Poção de Cura pequena", descricao = "Poção de cura que restaura uma pequena porção de vida", energia_gasta = 2, ponto_vida_curada = 8)
baralho.append(objeto_cartacura1)

objeto_cartacura2 = CartaCura(nome = "Poção de Cura Grande", descricao = "Poção de cura que restaura uma grande porção de vida", energia_gasta = 4, ponto_vida_curada = 24)
baralho.append(objeto_cartacura2)

objeto_cartarouba1 = CartaRoubo(nome = "Roubar uma carta", descricao = "rouba 1 carta do(a) oponente", energia_gasta = 4, roubar_carta = 1)
baralho.append(objeto_cartarouba1)

objeto_cartastun1 = CartaStun(nome = "Carta de Atordoamento", descricao = "Deixa o oponente atordoado", energia_gasta = 4, carta_de_stun = "Atordoado(a)")
baralho.append(objeto_cartastun1)

objeto_cartaaumentoataque1 = CartaAumento(nome = "Carta de Aumento de Ataque", descricao = "aumenta o ataque", energia_gasta = 1, tipo = "Ataque", pts_aumentado = 1)
baralho.append(objeto_cartaaumentoataque1)

objeto_cartaaumentodefesa1 = CartaAumento(nome = "Carta de Aumento de Defesa", descricao = "Aumenta a Defesa", energia_gasta = 1, tipo = "Defesa", pts_aumentado = 1)
baralho.append(objeto_cartaaumentodefesa1)

print("")

# Random vai pegar da lista (baralho) e de forma aletória escolher um certo numeros de cartas;
objeto_personagem1.mao_de_cartas.extend(random.choices(baralho, k = 4))
objeto_personagem2.mao_de_cartas.extend(random.choices(baralho, k = 4))

print("Suas cartas são: ")
for carta in objeto_personagem1.falar_cartas():
    print(carta.nome)

jogador_atual = objeto_personagem1
jogador_atual.falar_nome

jogador_oponente = objeto_personagem2
print("")

# A partida continua enquanto a vida estiver maior que 0;    
while objeto_personagem1.vida > 0 and objeto_personagem2.vida > 0:
    
    print("")
    print (f"É a vez de {jogador_atual.nome}")
    
    print(f"Vida de {jogador_atual.nome}: {jogador_atual.vida}")
    print(f"Energia de {jogador_atual.nome}: {jogador_atual.energia}")
    
    print("")
    
    

    acao = input(''' Escolha sua ação:
                        
                        1 - Ver Cartas
                        2 - Usar Carta
                        3 - Comprar Carta
                        0 - Fazer Nada
                        
                        ''')
    
    if acao == "1":
        for carta in objeto_personagem1.falar_cartas():
            print(carta.nome)
            
    elif acao == "2":
        print("Escolha uma carta para usar: ")
        for indice,carta in enumerate(objeto_personagem1.mao_de_cartas):
            print (f"{indice + 1} {carta.nome}")
        
        carta_escolhida = input()
        carta_escolhida = int(carta_escolhida)
        carta = jogador_atual.mao_de_cartas.pop(carta_escolhida - 1)
        print("")
        print("A carta escolhida foi: ")
        print(carta.nome)
        if (isinstance(carta, CartaDano)):
            carta.usar(oponente = jogador_oponente)
        elif (isinstance(carta, CartaCura)):
            carta.usar(personagem = jogador_atual)
        elif (isinstance(carta, CartaRoubo)):
            carta.usar(oponente = jogador_oponente)
        elif (isinstance(carta, CartaStun)):
            carta.usar(oponente = jogador_oponente)
        elif (isinstance(carta, CartaAumento)):
            carta.usar(personagem = jogador_atual)    
    elif acao == "0":
        break
    