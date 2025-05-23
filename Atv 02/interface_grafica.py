import tkinter as tk
from mini_sims import Personagem

class SimsApp:
    # Construtor (linha 4).
    def __init__(self, root):
        # Criando o(a) Personagem (linha 8).
        self.personagem = Personagem("Laura Caixão")
        
        # Titulo da janela (linha 11).
        root.tittle('Mini Sims')