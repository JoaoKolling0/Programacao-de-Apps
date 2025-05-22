import sqlite3

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
    
if __name__ == '__main__':
    criar_tabelas()