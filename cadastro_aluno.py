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
        match plano:
            case 'mensal':
                return 30
            case 'trimestral':
                return 90
            case 'anual':
                return 365
        return None

class CadastrarAluno(ConectarBanco, Planos):

    def cadastrar(self, nome_aluno, plano, data_cadastro, data_vencimento):
        try:
            comando = ('insert into cadastro_aluno (nome_aluno, plano, data_cadastro, data_vencimento) '
                       'values (%s, %s, %s, %s)')
            self.cursor.execute(comando, (nome_aluno, plano, data_cadastro, data_vencimento))
            self.conexao.commit()
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
        match dias_planos:
            case 30:
                data_vencida = data_atual + timedelta (days = 30)
                return data_vencida
            case 90:
                data_vencida = data_atual + timedelta(days=90)
                return data_vencida
            case 365:
                data_vencida = data_atual + timedelta(days=365)
                return data_vencida

    def atualizar_plano(self, nome_aluno, novo_plano):
        try:
            dias = Planos.dias_planos(novo_plano)

            if dias is None:
                print("PLANO INVALIDO.")
                return

            data_atual = CadastrarAluno.data_cadastrado()
            nova_data_vencimento = data_atual + timedelta(days=dias)

            comando = 'update cadastro_aluno set plano = %s, data_vencimento = %s where nome_aluno = %s'
            self.cursor.execute(comando, (dias, nova_data_vencimento, nome_aluno,))
            self.conexao.commit()

            if self.cursor.rowcount == 0:
                print("ALUNO NÃO ENCONTRADO.")
            else:
                print("PLANO ATUALIZADO COM SUCESSO.!")

        except mysql.connector.Error as erro:
            print(f"Erro NO BANCO DE DADOS: {erro}")


    def remover_aluno(self, nome_aluno):
        try:
            comando = 'delete from cadastro_aluno where nome_aluno = %s'
            self.cursor.execute(comando, (nome_aluno,))
            self.conexao.commit()

            if self.cursor.rowcount == 0:
                print("ALUNO NAO ENCONTRADO.")
            else:
                print("ALUNO REMOVIDO COM SUCESSO!")

        except mysql.connector.Error as erro:
            print(f"Erro NO BANCO DE DADOS: {erro}")

    def verificar_vencimento(self, nome_aluno):
        try:
            comando = 'select * from cadastro_aluno where nome_aluno = %s'
            self.cursor.execute(comando, (nome_aluno,))
            resultado = self.cursor.fetchone()

            if resultado is None:
                print("ALUNO NÃO ENCONTRADO.")
                return
            data_vencimento = resultado[4]
            print(f"DATA DE VENCIMENTO: {data_vencimento}")

            if datetime.now().date() > data_vencimento.date():
                print("INSCRIÇÃO VENCIDA")
            else:
                print("INSCRIÇÃO ATIVA")

        except mysql.connector.Error as erro:
            print(f"Erro NO BANCO DE DADOS: {erro}")
















