from Filme import Filme
from Filme import Acao
from Filme import Drama


filme =Filme("duro de matar 2",199)
filme.setNome("Duro de cozinhar 3")

print(filme.getNome())
naufrago =Drama("NAUFRAGO",185,"TOM HANKS")

naufrago.play()

lista_explosivos = ["BOMBA","GRANADA","DINAMITE","BOMBA NUCLEAR"]
john = Acao("Jonh Wick",140,lista_explosivos)

john.play()

