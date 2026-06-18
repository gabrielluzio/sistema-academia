from cadastro_aluno import CadastrarAluno
from cadastro_aluno import Planos


def main():
    funcao = CadastrarAluno()
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
                print('VALOR INVALIDO')
                continue

        except ValueError:
            print('DIGITE APENAS NUMEROS.')
            continue

        match usuario:
            case 1:
                nome_aluno = str(input('NOME DO ALUNO: ')).strip()
                if not nome_aluno:
                    print("NOME INVALIDO.")
                    continue
                plano = str(input('PLANO DO ALUNO: '))

                dias = Planos.dias_planos(plano)
                data = CadastrarAluno.data_cadastrado()
                data_vencida = CadastrarAluno.data_vencimento(data, dias)
                funcao.cadastrar(nome_aluno, dias, data, data_vencida)

            case 2:
                  nome_aluno = str(input('NOME DO ALUNO: ')).strip()
                  if not nome_aluno:
                      print("NOME INVALIDO.")
                      continue
                  funcao.ListarAlunos(nome_aluno)

            case 3:
                nome_aluno = str(input('NOME DO ALUNO: ')).strip()
                if not nome_aluno:
                    print("NOME INVALIDO.")
                    continue
                plano = str(input('PLANO DO ALUNO: '))
                funcao.atualizar_plano(nome_aluno, plano)

            case 4:
                nome_aluno = str(input('NOME DO ALUNO: ')).strip()
                if not nome_aluno:
                    print("NOME INVALIDO.")
                    continue
                funcao.verificar_vencimento(nome_aluno)

            case 5:
                nome_aluno = str(input('NOME DO ALUNO: ')).strip()
                if not nome_aluno:
                    print("NOME INVALIDO.")
                    continue
                funcao.remover_aluno(nome_aluno)

            case 6:
                funcao.fechar_conexao()
                print("SISTEMA ENCERRADO.")
                break
if __name__ == '__main__':
    main()


