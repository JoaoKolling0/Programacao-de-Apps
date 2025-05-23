import tkinter as tk
from mini_sims import Personagem

class SimsApp:
    # Construtor (linha 4).
    def __init__(self, root):
        # Criando o(a) Personagem (linha 8).
        self.personagem = Personagem("Laura Caixão")
        
        # Titulo da janela (linha 11).
        root.title("Mini Sims")
        # Tamanho da Janela
        root.geometry("500x500")
        
        self.label_status = tk.Label(root, text=self.personagem.mostrar_status(),
                                    font=("Arial", 18), pady=10)
        self.label_status.pack()
        
# Rodar o App
if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp(root)
    root.mainloop()