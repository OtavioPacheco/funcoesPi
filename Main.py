from Usuario import Usuario
from Jogo import Jogo
def main():
    user1 = Usuario()
    jogo1 = Jogo()
    while True:
        print("=="*10 + "MENU" + "=="*10 )
        print("ESCOLHA UMA OPACAO:")
        print("1: LOGIN")
        print("2: CADASTRO DE USUARIO")
        print("3: MOSTRAR USUÁRIO")
        print("4: SAIR")
        print("5: CADASTRO DE JOGOS")
        print("6: MOSTRAR JOGOS")

        opcao = input("QUAL VOCE ESCOLHE : ")

        if opcao == '1':
            nome = input("digite seu nome : ")
            senha = input("digite uma senha : ")
            user1.login(nome, senha)

        if opcao == '2':
            nome = input("digite seu nome : ")
            senha = input("digite uma senha : ")
            user1.cadastro(nome, senha)

        if opcao == '3':
            nome = input("digite seu nome : ")
            print(user1.mostraUsers(nome))

        if opcao == '4':
            break

        if opcao == '5':
            titulo = input("digite o titulo do seu jogo : ")
            nome = input("digite o nome do criador : ")
            jogo1.cadastro(titulo, nome)

        if opcao == '6':
            nome = input("digite seu nome : ")
            print(jogo1.mostraUsers(nome))

if __name__ == "__main__":
    main()