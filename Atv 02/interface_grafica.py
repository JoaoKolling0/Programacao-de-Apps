import tkinter as tk
from mini_sims import Personagem

class SimsApp:
    # Construtor
    def __init__(self, root):
        # Criando o(a) Personagem
        self.personagem = Personagem("Laura Caixão")
        
        # Titulo da janela
        root.title("Mini Sims")
        # Tamanho da Janela
        root.geometry("500x500")
        
        self.label_status = tk.Label(root, text=self.personagem.mostrar_status(),
                                    font=("Arial", 18), pady=10)
        self.label_status.pack()
        
        self.btn_comer = tk.Button(root, text="🍴 Comer", command=self.acao_botao_comer)
        self.btn_comer.pack(pady= 5)
        
        self.label_mensagem = tk.Label(root, text="", font=("Arial", 10 ))
        self.label_mensagem.pack()
        
# Método que atualiza os status dos personagens
    def atualizar_status(self):
        self.label_status.config(text=self.personagem.mostrar_status())
        
# Método que define a ação que vai acontecer quando apertar o botão comer
    def acao_botao_comer(self):
        mensagem = self.personagem.comer()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()
        
# Rodar o App
if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp(root)
    root.mainloop()