from model.conexao import ConectaBanco

class ControllerLogin():

    def insere(self, usuario, senha, nome):
        banco = ConectaBanco()
        banco.insereUsuario(usuario, senha, nome)

    def verifica(self, *args):
        banco = ConectaBanco()
        resultado = banco.verificaUsuario(*args)
        return resultado

class Controllercrud():
    def creat(self, nomeC, gastoC, precoC):
        banco = ConectaBanco()
        banco.criar(nomeC, gastoC, precoC)

    def read(self, nomeR):
        banco = ConectaBanco()
        resultado = banco.ler(nomeR)
        return resultado

    def update(self, nomeU, gastoU, precoU):
        banco = ConectaBanco()
        resultado = banco.atualizar(nomeU, gastoU, precoU)
        return resultado

    def delete(self, nomeD):
        banco = ConectaBanco()
        resultado = banco.apagar(nomeD)
        return resultado