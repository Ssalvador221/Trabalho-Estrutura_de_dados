
#Listas
analise = []
horasRealizadas = []
pendencias = []
matriculas = []
solicitacoes = []
codigosDeHorasComplementares = [1,10,322,324,345,456]
#########################################################


#Contadores
contAnalise = 0
contSolicitacoes = 0


#Adicionar
def adicionar():
    #Inputs para ler os valores!
    numMatricula = int(input("Digite sua matrícula: "))
    codigo = int(input("Digite o código das horas complementares: "))
    
    #Adição de valores as filas e correção da formatação dos numeros 001 e 010.
    while True:
        if(codigo != codigosDeHorasComplementares):
            matriculas.append(numMatricula)
            pendencias.append(codigo)
            for cod in pendencias:
                for mNum in matriculas:
                    if(cod == 1 or cod == 10):
                        print(mNum, "-", ("%03d" % (cod,)))
                    else:
                        print(mNum, "-", cod)      

            #Contadores
            contAnalise = 0
            contSolicitacoes = 0
            #Contadores aqui adicionam 1 sempre que passa por aqui
            contAnalise += 1
            contSolicitacoes += 1  
            
            analise.append(contAnalise)
            solicitacoes.append(contSolicitacoes)
            
            break     
        else:
            print("Codigo Invalid")
            break

#Analisar
def analisar():
    if analise != 0:
        print("Os seguintes documentos estão na fila para analise: ", len(analise))
    else:
        print("Não temos solicitação para análise!")

#Rejeitar
def rejeitar():
    rejeitado=analise.pop(0)
    pendencias.append(rejeitado)
    print("A solicitação ", pendencias[-1], " não possui todos os documentos necessários, avise o aluno e solicite os documentos corretos ao mesmo")

#Relatorio   
def relatorio():
    qtd_ana = len(analise)
    qtd_pnd = len(solicitacoes)
    qtd_hor = len(horasRealizadas)
    qtd_total = len(solicitacoes)
    print("O total de solicitações em análise são: ", qtd_ana)
    print("O total de solicitações com pendências são: ", qtd_pnd)
    print("O total de solicitações que forma validadas: ", qtd_hor)
    print("O total de solicitações analisadas no semestre foram:", qtd_total)





# Menu!
def invalido():
    print("Informe um número entre 1 e 5")

divisoria = "-" * 30
    
def menu():
    print(divisoria + '''\n Menu de opções:
        [1] Quantidade de solicitações aguardando análise
        [2] Validação de solicitações
        [3] Adicionar solicitação
        [4] Solicitações aguardando análise
        [5] Adicionar à fila de pendências
        [6] Relatório de solicitações
        [7] Sair do programa''')
    print(divisoria + '''\n Códigos:
        001 Monitoria de Ensino 2hs
        010 Participação em Seminário 3hs
        322 Postagem de artigo 5hs
        324 Produção de software 20hs
        345 Patente de produto 50hs
        456 Participação em mimicurso 20hs

        \n Exemplo da solicitação:
        Matrícula+código
        00987-324''')
    
operacao=0

while operacao !=7:
    menu()
    operacao=int(input("\nInforme a opção desejada: "))
    if operacao == 1:
        print()
    elif operacao == 2:
        print()
    elif operacao == 3:
        adicionar()
    elif operacao == 4:
        analisar()
    elif operacao == 5:
        rejeitar()
    elif operacao == 6:
        relatorio()
    elif operacao >= 8 or operacao <= 0:
        invalido()
    else:
        print("Fim")
        break













    
    
