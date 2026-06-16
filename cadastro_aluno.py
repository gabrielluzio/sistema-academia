import mysql.connector
from datetime import datetime, timedelta


class ConectarBanco:
    def __init__(self):
        self.conexao = None
        self.cursor = None


    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "SENHA",
                database = "academia"
            )
            self.cursor = self.conexao.cursor()
            print('BANCO CONECTADO')
        except mysql.connector.Error as erro:
            print('ERRO AO CONECTAR BANCO DE DADOS  ')
            print(erro)
            exit()

    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()

class Planos:
    @staticmethod
    def dias_planos(plano):
        if plano == 'mensal':
            return 30
        elif plano == 'trimestral':
            return 90
        elif plano == 'anual':
            return 365
        return None

class Cadastrar_Aluno(ConectarBanco, Planos):

    def cadastrar(self, nome_aluno, plano, data_cadastro, data_vencimento):
        try:
            comando = ('insert into cadastro_aluno (nome_aluno, plano, data_cadastro, data_vencimento) '
                       'values (%s, %s, %s, %s)')
            self.cursor.execute(comando, (nome_aluno, plano, data_cadastro, data_vencimento))
            self.conexao.commit()
            print('commit feito')
            print('ALUNO CADASTRADO. ')

        except mysql.connector.IntegrityError:
            print('Erro: ALUNO JA CADASTRADO!')

    def ListarAlunos(self,nome_aluno):
        comando = f'select * from cadastro_aluno where nome_aluno = %s'
        self.cursor.execute(comando,(nome_aluno,))
        resultado = self.cursor.fetchall()
        for aluno in resultado:
            print(aluno)

    @staticmethod
    def data_cadastrado():
        data_atual = datetime.now()
        return data_atual

    @staticmethod
    def data_vencimento(data_atual, dias_planos):
        if dias_planos == 30:
            data_vencida = data_atual + timedelta (days = 30)
            return data_vencida
        elif dias_planos == 90:
            data_vencida = data_atual + timedelta(days=90)
            return data_vencida
        elif dias_planos == 365:
            data_vencida = data_atual + timedelta(days=365)
            return data_vencida

    def atualizar_plano(self, nome_aluno, novo_plano):
        try:
            dias = Planos.dias_planos(novo_plano)

            if dias is None:
                print("Plano inválido.")
                return

            data_atual = Cadastrar_Aluno.data_cadastrado()
            nova_data_vencimento = data_atual + timedelta(days=dias)

            comando = 'update cadastro_aluno set plano = %s, data_vencimento = %s where nome_aluno = %s'
            self.cursor.execute(comando, (dias, nova_data_vencimento, nome_aluno,))
            self.conexao.commit()

            if self.cursor.rowcount == 0:
                print("Aluno não encontrado.")
            else:
                print("Plano atualizado com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro no banco de dados: {erro}")


    def remover_aluno(self, nome_aluno):
        try:
            comando = 'delete from cadastro_aluno where nome_aluno = %s'
            self.cursor.execute(comando, (nome_aluno,))
            self.conexao.commit()

            if self.cursor.rowcount == 0:
                print("Aluno não encontrado.")
            else:
                print("aluno removido com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro no banco: {erro}")

    def verificar_vencimento(self, nome_aluno):
        try:
            comando = 'select * from cadastro_aluno where nome_aluno = %s'
            self.cursor.execute(comando, (nome_aluno,))
            resultado = self.cursor.fetchone()

            if resultado is None:
                print("Aluno não encontrado.")
                return
            data_vencimento = resultado[4]
            print(f"Data de vencimento: {data_vencimento}")

            if datetime.now().date() > data_vencimento:
                print("INSCRIÇÃO VENCIDA")
            else:
                print("INSCRIÇÃO ATIVA")

        except mysql.connector.Error as erro:
            print(f"Erro no banco: {erro}")
















