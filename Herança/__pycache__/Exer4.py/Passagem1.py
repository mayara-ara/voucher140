from Passagem import Passagem

class Passagem1 (Passagem):
    def escolher_assento(passagem):
        passagem["assento_1"] = int (input("digite o assento desejado: "))
        return passagem
    

    