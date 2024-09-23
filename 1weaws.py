import os

def titulo():
    print('▀▄▀▄▀▄1001 🄴🅂🅃🄰🄱🄴🄻🄴🄲🄸🄼🄴🄽🅃🄾🅂▀▄▀▄▀▄ \n')
def opcoes():
    print('1. cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')\

estabelecimentos = [{'nome':'stf', 'paga_imposto':False , 'carga_horaria' : "40"},
                    {'nome':'LOUCCUROLANDIA', 'paga_imposto': True , 'carga_horaria' : "80"}]

def encerrar ():
    print('Encerrando')

def voltar_ao_menu():
    input("\n  digite qualisquer tercla para retornar ao menu principal  :")
    principal()
    
def opcao_invalida():
    print("opcao invalida!!\n")
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar():
    exibir_subtitulo('Cadasto de novos estabelecimentos')
    nome_do_estabelecimento = input('digite o nome do estabelecimento : ')
    carga_do_estabelecimento = input(f'digite a caraga horaria do estabelecimento {nome_do_estabelecimento} : ')
    dados_estabelecimento = {'nome' : nome_do_estabelecimento, 'carga_horaria' : carga_do_estabelecimento, 'paga_imposto': False }
    estabelecimentos.append(dados_estabelecimento)
    print(f' O estabelecimento{nome_do_estabelecimento} foi cadastrado com sucesso  ')
    
    
    voltar_ao_menu()

def listagem():
    
    exibir_subtitulo('lista de estabelecimentos')
    
    for estabelecimento in estabelecimentos :
        nome_do_estabelecimento = estabelecimento['nome'] 
        carga_horaria_do_estabelecimento = estabelecimento['carga_horaria']
        estabelecimento_paga_imposto = estabelecimento ['paga_imposto']
        print(f'- {nome_do_estabelecimento} | {carga_horaria_do_estabelecimento} | {estabelecimento_paga_imposto}')
    voltar_ao_menu()

def ativar_imposto():
    exibir_subtitulo('ativar imposto')
    nome_do_estabelecimento = input('digite o nome do estabelecimentoque voce deseja ativar o imposto : ')
    estabelecimento_encontrado = False
    
    for estabelecimeto in estabelecimentos :
        if nome_do_estabelecimento == estabelecimeto['nome']:
            estabelecimento_encontrado = True
            estabelecimeto['paga_imposto']= not estabelecimeto['paga_imposto']
            msg = f'o imposto no estabelecimento {nome_do_estabelecimento} restaurante foi ativado' 
            if estabelecimeto['paga_imposto'] : f'Imposto no estabelecimento {nome_do_estabelecimento} foi desativado com sucesso'
            print(msg)
    if not estabelecimento_encontrado:
        print('estabelecimento não encontrado')
    voltar_ao_menu()

def pagina_escolhas1():
    
    opcao_escolida= int(input('escolha uma opcao : '))

    print (f'voce escolheu a opcao {opcao_escolida} !!!')

    if opcao_escolida == 1 :
        cadastrar()
    elif opcao_escolida == 2:
        listagem()
    elif opcao_escolida == 3:
        ativar_imposto
    elif opcao_escolida == 4:
        encerrar()
    else :
        opcao_invalida()
        

def principal():
    os.system('cls')
    titulo()
    opcoes()
    pagina_escolhas1()

if __name__ == '__main__':
    principal()
    

