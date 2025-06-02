import tkinter as tk
from tkinter import messagebox
from mini_sims import Personagem, Trabalho

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
        
        self.btn_procurar_emprego = tk.Button(root, text="procurar emprego", command=self.acao_botao_procurar_emprego)
        self.btn_procurar_emprego.pack(pady= 5)
        
# Método que atualiza os status dos personagens
    def atualizar_status(self):
        self.label_status.config(text=self.personagem.mostrar_status())
        
# Método que define a ação que vai acontecer quando apertar o botão comer
    def acao_botao_comer(self):
        mensagem = self.personagem.comer()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()
        
    def acao_botao_procurar_emprego(self):
        self.trabalhos = self.criar_trabalhos()
        for trabalho in self.trabalhos:
            mensagem = trabalho.informacoes()
            resposta = messagebox.askquestion("Oferta de emprego", message=mensagem)
            if resposta == "yes":
                mensagem_sucesso = f"Parabéns, você foi contratado na carreira de {trabalho.carreira}."
                messagebox.showinfo("Oferta de emprego", mensagem_sucesso)
                self.personagem.ser_contratado(trabalho)
                return
        messagebox.showerror("Oferta de emprego", "não há mais empregos disponiveis")
        return
    
    def criar_trabalhos(self):
         # Criar um objeto para o trabalho
        carreira = "Artista Pop"
        cargos = ["Cantor de Rua", "Artista idependente", "Pop star"]
        salarios = [100, 1000, 20000]
        higiene = 30
        energia = 50
        social = 20

        objeto_trabalho_artista = Trabalho(carreira, cargos, salarios, higiene, energia, social)
        
        carreira = "Escritor"
        cargos = ["Escritor de Poemas ruins", "Escritor Amador", "Escritor", "Escritor de Best Seller"]
        salarios = [60, 120, 640, 1000]
        higiene = 30
        energia = 20
        social = 10
        
        objeto_trabalho_escritor = Trabalho(carreira, cargos, salarios, higiene, energia, social)
        
        lista_de_trabalho = [objeto_trabalho_artista, objeto_trabalho_escritor]
        
        return lista_de_trabalho
            
# Rodar o App
if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp(root)
    root.mainloop()