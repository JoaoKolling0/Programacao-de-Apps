from personagem import Personagem, CartaDano, CartaCura, CartaRoubo, CartaStun, CartaAumento

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

