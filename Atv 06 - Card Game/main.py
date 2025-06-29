from personagem import Personagem, Carta, CartaDano, CartaCura, CartaRoubo, CartaStun, CartaAumento
# Esse Main não será usado para o Jogo (o Jogo.py é onde está o jogo agora);
print("")
# O "objeto_personagem" é o jeito que usei para printar na main o personagem "principal", eu ainda tenho que fazer uma interfaçe;
objeto_personagem1 = Personagem(nome = "Kolling", status = "bem")
mensagem = objeto_personagem1.falar_nome()
print(mensagem)

print("")
# O "objeto_personagem02" é o jeito que usei para printar na main um 2° player, eu ainda tenho que fazer uma interfaçe;
objeto_personagem2 = Personagem(nome = "Misty", status = "bem")
mensagem = objeto_personagem2.falar_nome()
print(mensagem)

print("")
# O "objeto_cartadano" é o jeito que usei para printar na main cartas de ataque, eu ainda tenho que fazer uma interfaçe;
objeto_cartadano1 = CartaDano(nome = "Air Slash", descricao = "Lança um corte feito de vento na direção do oponente", energia_gasta = 2, ponto_dano = 8)
mensagem = objeto_cartadano1.usar(objeto_personagem1)
print(f"{objeto_personagem2.nome} usou {objeto_cartadano1.nome} em {objeto_personagem1.nome}")
print(mensagem)

print("")

objeto_cartadano2 = CartaDano(nome = "Pulso de Sangue", descricao = "Lança uma especie de feixe feito de sangue", energia_gasta = 6, ponto_dano = 32)
mensagem = objeto_cartadano2.usar(objeto_personagem2)
print(f"{objeto_personagem1.nome} usou {objeto_cartadano2.nome} em {objeto_personagem2.nome}")
print(mensagem)

print("")

objeto_cartadano3 = CartaDano(nome = "Espada Relâmpago", descricao = "O personagem carrega a espada com Raios e teleporta atras do adversário fazendo um corte com a espada", energia_gasta = 4, ponto_dano = 16)
mensagem = objeto_cartadano3.usar(objeto_personagem2)
print(f"{objeto_personagem1.nome} Usou {objeto_cartadano3.nome} em {objeto_personagem2.nome}")
print(mensagem)

print("")

objeto_cartadano4 = CartaDano(nome = "Corte Corrompido", descricao = "O personagem sacrifica sua honra por um momento para atacar o adversário com sua espada agora corrompida", energia_gasta = 2, ponto_dano = 8)
mensagem = objeto_cartadano4.usar(objeto_personagem1)
print(f"{objeto_personagem2.nome} usou {objeto_cartadano4.nome} em {objeto_personagem1.nome}")
print(mensagem)

print("")

# O "objeto_cartacura" é o jeito que usei para printar na main cartas de cura em geral, eu ainda tenho que fazer uma interfaçe;
objeto_cartacura1 = CartaCura(nome = "Poção de Cura pequena", descricao = "Poção de cura que restaura uma pequena porção de vida", energia_gasta = 2, ponto_vida_curada = 8)
mensagem = objeto_cartacura1.usar(objeto_personagem1)
print(f"{objeto_personagem1.nome} usou {objeto_cartacura1.nome}")
print(mensagem)

print("")

objeto_cartacura2 = CartaCura(nome = "Poção de Cura Grande", descricao = "Poção de cura que restaura uma grande porção de vida", energia_gasta = 4, ponto_vida_curada = 24)
mensagem = objeto_cartacura2.usar(objeto_personagem2)
print(f"{objeto_personagem2.nome} usou {objeto_cartacura2.nome}")
print(mensagem)

print("")
# O "objeto_cartarouba" é o jeito que usei para printar na main uma carta usada para roubar uma das cartas do inimigo, eu ainda tenho que fazer uma interfaçe;
objeto_cartarouba1 = CartaRoubo(nome = "Roubar uma carta", descricao = "rouba 1 carta do(a) oponente", energia_gasta = 4, roubar_carta = 1)
mensagem = objeto_cartarouba1.usar(objeto_personagem1)
print(f"{objeto_personagem2.nome} usou {objeto_cartarouba1.nome} em {objeto_personagem1.nome}")
print(mensagem)

print("")
# O "objeto_cartastun" é o jeito que usei para printar na main uma carta para dar stun, eu ainda tenho que fazer uma interfaçe;
objeto_cartastun1 = CartaStun(nome = "Carta de Atordoamento", descricao = "Deixa o oponente atordoado", energia_gasta = 4, carta_de_stun = "Atordoado(a)")
mensagem = objeto_cartastun1.usar(objeto_personagem2)
print(f"{objeto_personagem1.nome} usou {objeto_cartastun1.nome} em {objeto_personagem2.nome}")
print(mensagem)

print("")
# O "objeto_cartaaumento" é o jeito que usei para printar na main uma carta de buff, eu ainda tenho que fazer uma interfaçe;
objeto_cartaaumentoataque1 = CartaAumento(nome = "Carta de Aumento de Ataque", descricao = "aumenta o ataque", energia_gasta = 1, tipo = "Ataque", pts_aumentado = 1)
mensagem = objeto_cartaaumentoataque1.usar(objeto_personagem1)
print(f"{objeto_personagem1.nome} usou {objeto_cartaaumentoataque1.nome}")
print(mensagem)

print("")

objeto_cartaaumentodefesa1 = CartaAumento(nome = "Carta de Aumento de Defesa", descricao = "Aumenta a Defesa", energia_gasta = 1, tipo = "Defesa", pts_aumentado = 1)
mensagem = objeto_cartaaumentodefesa1.usar(objeto_personagem2)
print(f"{objeto_personagem2.nome} usou {objeto_cartaaumentodefesa1.nome}")
print(mensagem)

print("")

