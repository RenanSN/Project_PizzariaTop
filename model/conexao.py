import MySQLdb  # Importa a biblioteca do MySQL


class ConectaBanco:  # Define a classe
    def __init__(self):  # init é o metodo inicializador da classe

        self.con = ""  # Cria a variavel de conexão vazia
        self.nome = ""

    def conecta(self):  # Método para conectar no banco
        host = "localhost"  # Nome utilizado no host no Workbenck
        user = "root"  # Nome do usuario que criamos no Workbenck
        password = ""  # Senha que colocamos para o usuario
        db = "pizzariatop"  # Nome do banco de dados
        port = 3306  # Porta configurada para o server MySQL
        self.con = MySQLdb.connect(host, user, password, db, port)  # Na variavel con cria nossa conexão

    def insereUsuario(self, usuario, senha): #Método que faz a criação do usuário no banco de dados, inserindo o nome, senha e login
        self.conecta()
        cur = self.con.cursor()

        query = ('insert into tbl_usuarios (login_usuario, senha_usuario)values ("{}", "{}");'.format(usuario, senha))
        #Query que faz a inserção da login, senha e nome

        cur.execute(query)

        self.con.commit()
        self.con.close()



        # if cur.rowcount > 0:
        #     result = True
        # else:
        #     result = False

        # return result

    def verificaUsuario(self, *args): #Função que verifica se o usuário existe no banco. No código também existe outra função chamada verificaUsuario, esta recebe como parametro o usuario e a senha para fazer a verificação
        self.conecta()
        cur = self.con.cursor()

        if len(args) == 2:
            query = ("select login_usuario, senha_usuario from tbl_usuarios where login_usuario = '{}' and senha_usuario = '{}';".format(args[0], args[1]))
            #Query que seleciona o usuario e a senha de acordo com os valores passados pela view
            cur.execute(query)
            resultado = cur.fetchall() #Guarda o resultado do select realizado acima
            if len(resultado) > 0: #Verifica se a quantidade de linhas do select realizado é maior que 0, se for significa que o usuario já existe, se não for significa que o usuario ainda não existe
                return True
            else:
                return False
        elif len(args) == 1:
            self.conecta()
            cur = self.con.cursor()
            query = (
                "select login_usuario, senha_usuario from tbl_usuarios where login_usuario = '{}';".format(
                    args[0]))
            cur.execute(query)
            resultado = cur.fetchall()

            if len(resultado) > 0:
                return True
            else:
                return False

    def criar(self, nomeC, gastoC, precoC):
        self.conecta()
        cur = self.con.cursor()
        queryC = ('insert into tbl_produtos (nome_produto, gasto_produto, venda_produto)values ("{}", "{}", "{}");'.format(nomeC, gastoC, precoC))
        cur.execute(queryC)
        self.con.commit()
        self.con.close()

    def ler(self, nomeR):
        self.conecta()
        cur = self.con.cursor()
        queryR = ('select * from tbl_produtos where nome_produto = "{}" ;'.format(nomeR))
        self.nome = nomeR
        cur.execute(queryR)
        resultado = cur.fetchall()
        if len(resultado) > 0:
            return True
        else:
            return False
        self.con.close()

    def atualizar(self, nomeU, gastoU, precoU):
        self.conecta()
        cur = self.con.cursor()
        #query = f'select cod_produto from tbl_produtos where nome_produto = "{self.nome}"'
        #cur.execute(query)
        queryU = ('update tbl_produto set nomeU = "{}", gastoU = {}, precoU = {} where ')
        cur.execute(queryU)
        self.con.close()

    def apagar(self, nomeD):
        self.conecta()
        cur = self.con.cursor()
        queryD = ('delete from tbl_produtos where nome_produto = "{}"'.format(nomeD))
        cur.execute(queryD)
        self.con.commit()
        self.con.close()