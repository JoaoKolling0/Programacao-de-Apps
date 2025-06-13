from personagem import Personagem, Carta, CartaDano, CartaCura, CartaRoubo

objeto_personagem1 = Personagem("Kolling")
mensagem = objeto_personagem1.falar_nome()
print(mensagem)

objeto_personagem2 = Personagem("Misty")
mensagem = objeto_personagem2.falar_nome()

print("")

objeto_cartadano1 = CartaDano(nome = "Air Slash", descricao = "Lança um corte feito de vento na direção do oponente", energia_gasta = 2, ponto_dano = 8)
mensagem = objeto_cartadano1.usar(objeto_personagem2)
print(mensagem)

print("")

objeto_cartacura1 = CartaCura(nome = "Poção de Cura pequena", descricao = "Poção de cura que restaura uma pequena porção de vida", energia_gasta = 2, ponto_vida_curada = 8)
mensagem = objeto_cartacura1.usar(objeto_personagem1)
print(mensagem)

print("")

objeto_cartarouba1 = CartaRoubo(nome = "Roubar 01 carta", descricao = "rouba 1 carta do(a) oponente", energia_gasta = 4, roubar_carta = 1)
mensagem = objeto_cartarouba1.usar(objeto_personagem1)
print(mensagem)

print("")
