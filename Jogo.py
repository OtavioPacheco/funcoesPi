from Usuario import Usuario

class Jogo(Usuario):

    def __init__(self):
        super().__init__()
        self.jogos = []

    def cadastro(self, titulo, nome):
        jogo = {"titulo" : titulo, "nome" : nome}
        self.jogos.append(jogo)

    def mostraUsers(self, titulo):
        for jog in self.jogos:
            if jog["nome"] == titulo:
                return jog
        return None

    def getJogo(self):
        return self.jogos

    def setTitulo(self, titulo, nome):
        jogo = {"titulo" : titulo, "nome" : nome}
        self.jogos.append(jogo)