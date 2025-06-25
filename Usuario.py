class Usuario:

    def __init__(self):
        self.user = [{"nome" : '', "senha" : ''}]

    def mostraUsers (self, nome):
        for use in self.user:
            if use["nome"] == nome:
                return use
        return None

    def cadastro(self, nome, senha):
        user = {"nome" : nome , "senha" : senha}
        for us in self.user:
            if us["nome"] != nome:
                self.user.append(user)
            else:
                print(f"Ja existe usuario com esse nome")
    def login (self, nome, senha):
        for us in self.user:
            if us["nome"] == nome and us["senha"] == senha:
                print(f"Login bem-sucedido! Bem-vindo, {nome}.")
                return True
        print("Nome ou senha incorretos.")
        return False

    def getUser(self):
        return self.user

    def setUser(self, nome, senha):
        user = {"nome":nome, "senha":senha}
        self.user = user


