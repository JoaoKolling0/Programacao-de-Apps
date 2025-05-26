class Personagem: # Classe que vai fazer as coisas sobre o personagem.
    def __init__(self, nome):
        #init é o construtor da classe
        self.nome = nome
        self.energia = 100
        self.fome = 100
        self.higiene = 100
        self.social = 100
        self.dinheiro = 160
        self.trabalho = None
        # Os atributos são o que vem após o self
        
    # Métodos (Ações) abaixo
    def comer (self):
        if self.dinheiro < 10:
            return f"{self.nome} não tem dinheiro para comer"
            # para não ter que usar o "print" o professor disse para usar o comando acima
        else:
            self.fome = min(100, self.fome + 20)
            self.dinheiro -= 10
            return f"{self.nome} se almentou"
        
    def dormir (self):
        if (self.energia == 100):
            return f"{self.nome} está como Coruja e não precisa dormir"
        
        else:
            self.energia = 100
            self.fome -= 40
            return f"{self.nome} dormiu finalmente e está mais descansado"
        
    def banho (self):
        if (self.higiene == 100):
            return f"{self.nome} perde tudo mas não fica sujo(a), então não precisa de um banho"
        
        else:
            self.higiene = 100
            self.energia += 20
            return f"{self.nome} o gambá finalmente tomou banho"
    
    def trabalhar (self):
        if (self.energia < 20):
            return f"{self.nome} só falta enterrar de tão cansado(a), não pode trabalhar agora"
        
        self.energia -= 20
        self.higiene -= 10
        self.social += 10
        return f"{self.nome} trabalhou como uma mula, mas pelo menos terminou o dia de trabalho"
    
    def socializar (self):
        if (self.social == 100):
            return f"{self.nome} é amigo(a) até do diabo de tão sociavel"
        
        else:
            self.social == 100
            
    def mostrar_status(self):
        return f'''
        👩 {self.nome}
        😴 Energia: {self.energia}
        🛀 Higiene: {self.higiene}
        💬 Social: {self.social}
        📋 Trabalho: {self.trabalho}
        💰 Dinheiro: {self.dinheiro}
    '''
    
class Trabalho:
    def __init__(self, carreira, cargos, salarios, higiene, energia):
        # Atributos
        self.carreira = carreira
        self.cargos = cargos # Lista de cargos possíveis
        self.salarios = salarios # Lista de salarios
        self.higiene_utilizada = higiene
        self.energia_gasta = energia
        
    # Métodos
        
if __name__ == "__main__":
    # Criar um objeto para o personagem
    obj1 = Personagem("Laura Caixão")
    
    print(obj1.nome)
    print(obj1.fome)
    
    obj2 = Personagem("Buddy")
    
    print(obj2.nome)
    obj2.fome -= 10
    print(obj2.fome)