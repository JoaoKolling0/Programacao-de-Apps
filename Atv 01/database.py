import sqlite3
import datetime

def criar_tabelas():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    
    cursor.execute('''create table if not exists alunos
                    (id integer primary key autoincrement, nome text)''')
    
    cursor.execute('''create table if not exists livros
                   (id integer primary key autoincrement, titulo text, autor text, ano text)''')
    
    cursor.execute('''create table if not exists emprestimos
                   (id integer primary key autoincrement, id_livro integer, id_aluno integer, 
                   data_emprestimo text, data_devolucao text, status text,
                   FOREIGN KEY(id_livro) REFERENCES livros(id),
                   FOREIGN KEY(id_aluno) REFERENCES alunos(id))''')
    
    conexao.commit()
     
def criar_aluno(nome):
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    
    cursor.execute('''INSERT INTO alunos (nome) VALUES (?)''', (nome,))
    
    conexao.commit()
    conexao.close()
    
def criar_livro(titulo, autor, ano):
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        
        cursor.execute('''INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)''', (titulo, autor, ano))
        
        conexao.commit()
        conexao.close()
        
def realizar_emprestimo(id_aluno, id_livro, data_devolucao):
    
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    
    data_hoje = datetime.datetime.now()
    
    cursor.execute('''INSERT INTO emprestimos (id_aluno, id_livro, data_emprestimo, data_devolucao, status)
                   VALUES (?, ?, ?, ?, ?)''', (id_aluno, id_livro, data_hoje, data_devolucao, "Emprestado"))
    
    conexao.commit()
    conexao.close()
    
def ver_emprestimos_aluno(id_aluno):
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    
    cursor.execute('''SELECT livros.titulo, livros.autor, emprestimos.data_devolucao
                   FROM emprestimos, livros
                   WHERE emprestimos.id_aluno = ? AND livros.id = emprestimos.id_livro''', (id_aluno,))
    
    emprestimos = cursor.fetchall()
    print(emprestimos)
    conexao.commit()
    conexao.close()
    return
    
def ver_emprestimos_atrasados():
    pass

if __name__ == '__main__':
    data_devolver = datetime.datetime(2025,5,25)
    realizar_emprestimo(1, 1, data_devolver)