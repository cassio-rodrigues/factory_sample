from abc import ABCMeta, abstractmethod

class Secao(metaclass=ABCMeta):

    @abstractmethod
    def __repr__(self) -> str:
        pass

class SecaoPessoal(Secao):

    def __repr__(self) -> str:
        return "Seção Pessoal"
    

class SecaoAlbum(Secao):

    def __repr__(self) -> str:
        return "Seção Album"
    

class SecaoProjeto(Secao):

    def __repr__(self) -> str:
        return "Seção Projeto"
    

class SecaoPublicação(Secao):

    def __repr__(self) -> str:
        return "Seção Publicação"
    

class Perfil(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    
    def get_secoes(self):
        return self.secoes

    def add_secao(self, secao):
        return self.secoes.append(secao)


class LikedIn(Perfil):

    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoProjeto())
        self.add_secao(SecaoPublicação())


class FaceBook(Perfil):

    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoAlbum())



if __name__ == "__main__":
    rede_social = input("rede social para criar")

    perfil = eval(rede_social)()

    print(f"criando perfil no {type(perfil).__name__}")
    print(f"o perfil foi criado: {perfil.get_secoes()}")