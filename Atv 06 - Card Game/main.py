from personagem import Personagem, Carta, CartaDano

objeto_personagem1 = Personagem("Kolling")
mensagem = objeto_personagem1.falar_nome()
print(mensagem)

objeto_personagem2 = Personagem("Misty")
mensagem = objeto_personagem2.falar_nome()

print("")

objeto_cartadano1 = CartaDano(nome = "Air Slash", descricao = "Lança um corte feito de vento na direção do oponente", energia_gasta = 2, ponto_dano = 8)
mensagem = objeto_cartadano1.usar(objeto_personagem2)
print(mensagem)
