# Listas
#Grupo: Felipe Loche, Matias Daniel, Jael Pinheiro e João Salvador

analise = []
horasRealizadas = []
pendencias = []
matriculas = []
solicitacoes = []
codigosDeHorasComplementares = [1, 10, 322, 324, 345, 456]
horasTotaisPorCodigo = []
listaDeAlunos = []
listaAnaliseAluno = []


#############################################################

# Adicionar
def adicionarAluno():
    # Inputs para ler os valores!
    numMatricula = input("Digite sua matrícula: ") # Recebe a matricula do aluno

    if numMatricula == "":
        print("Por favor digite uma matrícula valida")
        return

    codigo = int(input("Digite o código das horas complementares: ")) # Recebe o código das horas

    if codigo == '':
        print("Por favor digite um código válido")
        return
    else:
        codigo = int(codigo)

    codigoHoras = { # Dicionario que recebe CODIGO = HORAS 
        1:2,
        10: 3,
        322: 5,
        324: 20,
        345: 50,
        456: 20
    }


    if codigo in codigoHoras: # Itera sobre o dicionario
        horas = codigoHoras[codigo]
    else:
        print("Por favor, digite um dos códigos acima!")
        return

    existeMatricula = False # Se a matrícula não existe
    for aluno in listaDeAlunos: # Aluno itera sobre a lista de Alunos 
        if aluno['Matrícula'] == numMatricula: # Se matricula == input número da matrícula ele adiciona os valores em uma lista
            existeMatricula = True # Se matricula existe já ele adiciona as horas e soma com as que já existe
            aluno['Horas'] += horas
            break # Fim do programa

    #Se aluno não for false ele adiciona os valores as dicionario.
    if not existeMatricula:
        matriculaFormatada = numMatricula.zfill(5) if len(numMatricula) < 5 else numMatricula
        aluno = {
            'Matrícula': matriculaFormatada,
            'Horas': horas
        }
        listaDeAlunos.append(aluno)

    # Adição de valores às filas e correção da formatação dos números 001 e 010.
    if codigo in codigosDeHorasComplementares:
        matriculas.append(numMatricula)
        alunoRequisicao = {
            'Matrícula': numMatricula,
            'Código': codigo
        }
        for cod in pendencias: # Iteração de lista 
            for mNum in matriculas: # Iteração de lista
                if cod == 1 or cod == 10:
                    print(mNum, "-", ("%03d" % (cod,))) 
                else:
                    print(mNum, "-", cod)
        analise.append(alunoRequisicao) 
    else:
        listaDeAlunos.pop()
        print("Código Inválido")


# Visualizar o total de analises na fila.
def totalAnalises(): 
    if len(analise) != 0:
        for iCodigo in range(len(analise) - 1, -1, -1):
            aluno = analise[iCodigo]  
            print(f"Os seguintes documentos estão na fila para análise {iCodigo + 1}: Matrícula do Aluno: {aluno['Matrícula']},", " Código de horas: " ,aluno['Código'])
            #print("Os seguintes documentos estão na fila para análise: Matrícula do Aluno: ", aluno['Matrícula'], ", Código de horas: " ,aluno['Código'])   
    else:
        print("Não temos solicitações para análise!")


# O número total de analises na fila.
def qtd_analisar(): # Quantidade de Solitações 
    if analise != 0:
        print("Os seguintes documentos estão na fila para analise: ", len(analise))
    else:
        print("Não temos solicitação para análise!")


#Rejeitar alguma analise por falta de documento
listTotalPendencias = []
def rejeitarAnalise():
    if len(analise) != 0: # Verificar se a fila esta Vazia!
        rejeitado = analise.pop(0)

        countPendencias = 0
        countPendencias+=1

        listTotalPendencias.append(countPendencias)
        pendencias.append(rejeitado['Código']) # Adiciona o código que o aluno digitou referente as Horas.
        listaDeAlunos.pop(0)
        for pend in pendencias:
            print("A solicitação ", pend, " não possui todos os documentos necessários, avise o aluno e solicite os documentos corretos ao mesmo")
    else:
        print("Não há solicitações para validar!")


# Valida as horas do aluno por matricula
def validarHoras():
    if len(analise) != 0: # Verificar se a fila esta Vazia! Dica do mano Michel.

        validado = analise.pop(0)
        horasRealizadas.append(validado)

        for iHoras in range(len(listaDeAlunos) - 1, -1, -1): # Itera sobre o indice da lista assim retornando a ultima posição da pilha;
            
            horasAluno = listaDeAlunos[iHoras]

            if horasAluno['Matrícula'] == validado['Matrícula']: ## Se horasAluno['Matricula'] for igual a validado[Matricula] ele printa as informações do Aluno.
                dadosFormatados = f"A solicitação da matrícula: {horasAluno['Matrícula']}, com total de horas: {horasAluno['Horas']}, foi validada."
                listaDeAlunos.pop(0)
                print(dadosFormatados)
                break
    else:
        print("Não há horas para validar!")


# Relatorio geral das informações
def relatorio():
    qtd_ana = len(analise)
    qtd_pnd = len(listTotalPendencias)
    qtd_hor = len(horasRealizadas)
    qtd_total = len(solicitacoes)
    print("O total de solicitações em análise são: ", qtd_ana)
    print("O total de solicitações com pendências são: ", qtd_pnd)
    print("O total de solicitações que forma validadas: ", qtd_hor)
    print("O total de solicitações analisadas no semestre foram:", qtd_total)
    print("O total por alunos de hora é:", listaDeAlunos)


# Função que informa erro caso o Usuário digite errado.
def invalido():
    print("Informe um número entre 1 e 7")


divisoria = "-" * 30

# Menu que printa na tela as informações.
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
        456 Participação em minicurso 20hs

        \n Exemplo da solicitação:
        Matrícula+código
        00987-324''')


operacao = 0

while operacao != 7:
    menu()
    operacao = int(input("\nInforme a opção desejada: "))
    if operacao == 1:
        qtd_analisar()
    elif operacao == 2:
        validarHoras()
    elif operacao == 3:
        adicionarAluno()
    elif operacao == 4:
        totalAnalises()
    elif operacao == 5:
        rejeitarAnalise()
    elif operacao == 6:
        relatorio()
    elif operacao >= 8 or operacao <= 0:
        invalido()
    else:
        print("Programa encerrado.")
        break
