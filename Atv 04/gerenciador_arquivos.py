# O objetivo da Atv 04 é fazer um simulador de diretórios (diretórios +- = a "pastas");
class Arquivo:
    def __init__(self, nome, tipo, data, tamanho):
        
        self.nome = nome
        self.tipo = tipo
        self.data = data
        self.tamanho = tamanho
        
class Diretorio:
    def __init__(self, nome):
        
        self.nome = nome
        self.lista_arquivo = [] #Colchetes usados para criar uma lista.
        self.lista_pasta = [] #Colchetes usados para criar uma lista.
        
    def add_arquivo(self, objeto_arquivo):
        self.lista_arquivo.append(objeto_arquivo)
        
    def add_pasta(self, objeto_pasta):
        self.lista_pasta.append(objeto_pasta)
        
    def listar_conteudo(self):
        print("Arquivos -", self.nome)
        for arquivo in self.lista_arquivo:
            print(arquivo.nome)
        
           
    
if __name__ == "__main__":
    
    print("")
    
    objeto_arquivo01 = Arquivo(nome = "- ACDC - Back in Black -", tipo = "mp3 -", data = "06/062/025 -", tamanho = "6mb -")
    print(objeto_arquivo01.nome, objeto_arquivo01.tipo, objeto_arquivo01.data, objeto_arquivo01.tamanho)
    
    print("")
    
    objeto_arquivo02 = Arquivo(nome = "- SURVIVOR - Eye Of The Tiger -", tipo = "mp3 -", data = "06/06/2025 -", tamanho = "6mb -")
    print(objeto_arquivo02.nome, objeto_arquivo02.tipo, objeto_arquivo02.data, objeto_arquivo02.tamanho)
    
    print("")
    
    objeto_pasta01 = Diretorio(nome = "Músicas")
    objeto_pasta01.add_arquivo(objeto_arquivo01)
    objeto_pasta01.add_arquivo(objeto_arquivo02)
    
    objeto_pasta01.listar_conteudo()
    
    