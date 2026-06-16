from cadastro_aluno import Cadastrar_Aluno
from cadastro_aluno import Planos


def main():
    funcao = Cadastrar_Aluno()
    funcao.conectar()

    while True:
        print('''
        1 --> CADASTRAR ALUNO
        2 --> EXIBIR ALUNO
        3 --> ATUALIZAR PLANO
        4 --> DATA DE VENCIMENTO
        5 --> REMOVER ALUNO
        6--> SAIR ''')
        try:
            usuario = int(input('ESCOLHA UMA OPÇÃO: '))
            if usuario < 1 or usuario > 6:
                print('valor invalido')
                continue

        except ValueError:
            print('Digite apenas números.')
            continue

        if usuario == 1:
            nome_aluno = str(input('NOME DO ALUNO: ')).strip()
            if not nome_aluno:
                print("Nome inválido.")
                continue
            plano = str(input('PLANO DO ALUNO: '))

            dias = Planos.dias_planos(plano)
            data = Cadastrar_Aluno.data_cadastrado()
            data_vencida = Cadastrar_Aluno.data_vencimento(data, dias)
            funcao.cadastrar(nome_aluno, dias, data, data_vencida)


        elif usuario == 2:
              nome_aluno = str(input('NOME DO ALUNO: ')).strip()
              if not nome_aluno:
                  print("Nome inválido.")
                  continue
              funcao.ListarAlunos(nome_aluno)

        elif usuario == 3:
            nome_aluno = str(input('NOME DO ALUNO: ')).strip()
            if not nome_aluno:
                print("Nome inválido.")
                continue
            plano = str(input('PLANO DO ALUNO: '))
            funcao.atualizar_plano(nome_aluno, plano)

        elif usuario == 4:
            nome_aluno = str(input('NOME DO ALUNO: ')).strip()
            if not nome_aluno:
                print("Nome inválido.")
                continue
            funcao.verificar_vencimento(nome_aluno)

        elif usuario == 5:
            nome_aluno = str(input('NOME DO ALUNO: ')).strip()
            if not nome_aluno:
                print("Nome inválido.")
                continue
            funcao.remover_aluno(nome_aluno)

        elif usuario == 6:
            funcao.fechar_conexao()
            print("Sistema encerrado.")
            break
if __name__ == '__main__':
    main()


