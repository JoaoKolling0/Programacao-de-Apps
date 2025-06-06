# O objetivo da Atv 04 é fazer um simulador de diretórios (diretórios +- = a "pastas");
class Arquivo:
    def __init__(self, nome, tipo, data, tamanho):
        
        self.nome = nome
        self.tipo = tipo
        self.data = data
        self.tamanho = tamanho
        
class Diretorio:
    def __init__(self, nome, lista_arquivo, lista_pasta):
        
        self.nome = nome
        self.lista_arquivo = lista_arquivo
        self.lista_pasta = lista_pasta
        
if __name__ == "__main__":
    pass