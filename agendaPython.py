def menu():
    opcao= input('''
     ==================================================
                 PROJETO AGENDA EM PYTHON
    ---------------------- MENU -----------------------
    [ 1 ] CADASTRAR CONTATO
    [ 2 ] LISTAR CONTATO
    [ 3 ] DELETAR CONTATO
    [ 4 ] BUSCAR CONTADO PELO NOME
    [ 5 ] SAIR   
    ====================================================
    ESCOLHA UMA DAS OPÇÕES:
     ''' )
    if opcao =="1":
        cadastroContato()
    elif opcao =="2":
        listarContato()
    elif opcao =="3":
        deletarContato()
    elif opcao =="4":
        buscarContatoNome()
    else:
        sair()

def cadastroContato():
    idContato = input("Escolha o ID do contato: ")
    nome = input("Escreva o nome do contato: ")
    telefone = input("Escreva o telefone de contato: ")
    email = input("Escreva o email do contato: ")
    try:
        agenda = open("agenda.txt","a")
        dados = f'{idContato};{nome};{telefone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!!')
    except:
        print("ERRO na gravação do contato")
def listarContato():
        agenda = open("agenda.txt","r")
        for contato in agenda:
         print(contato)
        agenda.close()

def deletarContato():
        nomeDeletado = input("Digite o nome a ser deletado: ")
        agenda = open("agenda.txt","r")
        aux = []
        aux2 =[]
        for i in agenda:
            aux.append(i)
        for i in range(0, len(aux)):
            aux2.append(aux[i])
            agenda = open("agenda.txt","w")
        for i in aux2:
            agenda.write(i)
            listarContato()
        print(f'Contato deletado com sucesso')

def buscarContatoNome():
    nome = input(f'digite o nome procurado: ')
    agenda = open("agenda.txt","r")
    for contato in agenda:
        if nome in contato.split(";")[1]:
         print(contato)
    agenda.close()

def sair():
    print(f'Sistema de agenda desligado')
    exit()

def main():

    menu()

main()
