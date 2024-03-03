from abc import ABCMeta, abstractclassmethod

class Animal(metaclass=ABCMeta):

    @abstractclassmethod
    def falar(self):
        pass


class Cachorro(Animal):

    def falar(self):
        print("late")


class Gato(Animal):

    def falar(self):
        print("mia")


#factory
class Fabrica:

    def criar_animal(self, tipo):
        return eval(tipo)().falar()



if __name__ == "__main__":
    fab = Fabrica()
    animal = input("insira o animal e descubra o som")
    fab.criar_animal(animal)
