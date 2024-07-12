class Livro:
    def __init__(self, nome: str, autor: str, editora: str, paginas: int):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def getPaginas(self):
        print(self.paginas)
        
    def setEditora(self, nomenovo):
        self.editora = nomenovo

livro = Livro('A bela e a fera', 'JOAO', 'ATICA', 300)
livro2 = Livro('Poesia concreta', 'Paulo Leminsk', 'Tesla', 199)
livro3 = Livro('Alberto caeiro', 'Fernando Pessoa', 'Brasil', 200)
livro4 = Livro('O Alquimista', 'Paulo Coelho', 'ok', 150)

livro4.getPaginas()
print(livro4.editora)

livro4.setEditora('123')
print(livro4.editora)
