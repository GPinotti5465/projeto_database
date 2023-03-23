import urllib.request


def filtnum(string):
    return int(''.join(filter(str.isdigit, string)))


def modulo11cpf(self):
    pjfinal = self

    if "." in pjfinal:
        cnpjqttdot = len(self.split('.'))
        cpj = 0
        fpj1 = pjfinal
        pjfinal = ""
        while (cnpjqttdot) > cpj:
            pjfinal = pjfinal + fpj1.split('.')[cpj]
            cpj+=1


    if "/" in pjfinal:
        cnpjqttbar = len(self.split('/'))
        cpj = 0
        fpj2 = pjfinal
        pjfinal = ""
        while (cnpjqttbar) > cpj:
            pjfinal = pjfinal + fpj2.split("/")[cpj]
            cpj+=1
    
    if "-" in pjfinal:
        cnpjqtthash = len(self.split('-'))
        cpj = 0
        fpj3 = pjfinal
        pjfinal = ""
        while (cnpjqtthash) > cpj:
            pjfinal = pjfinal + fpj3.split("-")[cpj]
            cpj+=1

    if "," in pjfinal:
        cnpjqttcomma = len(self.split(','))
        cpj = 0
        fpj4 = pjfinal
        pjfinal = ""
        while (cnpjqttcomma) > cpj:
            pjfinal = pjfinal + fpj4.split(",")[cpj]
            cpj+=1


    if pjfinal.isnumeric() == False:
        return 'INVÁLIDO'

    if len(pjfinal) !=11 :
        return 'INVÁLIDO'
    cpftemp1 = (
        (int(pjfinal[0]) * 1) + 
        (int(pjfinal[1]) * 2) + 
        (int(pjfinal[2]) * 3) + 
        (int(pjfinal[3]) * 4) + 
        (int(pjfinal[4]) * 5) + 
        (int(pjfinal[5]) * 6) +
        (int(pjfinal[6]) * 7) + 
        (int(pjfinal[7]) * 8) + 
        (int(pjfinal[8]) * 9)
    )
    if cpftemp1 % 11 == None or cpftemp1 % 11 == 10:
        cpftemp1mod = 0
    else:
        cpftemp1mod = cpftemp1 % 11 
    
    cpftemp2 = (
        (int(pjfinal[0]) * 0) + 
        (int(pjfinal[1]) * 1) + 
        (int(pjfinal[2]) * 2) + 
        (int(pjfinal[3]) * 3) + 
        (int(pjfinal[4]) * 4) + 
        (int(pjfinal[5]) * 5) +
        (int(pjfinal[6]) * 6) + 
        (int(pjfinal[7]) * 7) + 
        (int(pjfinal[8]) * 8) +
        (cpftemp1mod * 9)
    )
    if cpftemp2 % 11 == None or cpftemp2 % 11 == 10:
        cpftemp2mod = 0
    else:
        cpftemp2mod = cpftemp2 % 11 


    if str(cpftemp1mod) + str(cpftemp2mod) == pjfinal [9] + pjfinal[10]:
        return 'VÁLIDO'
    else:
        return 'INVÁLIDO'



#-------------------------CNPJ

def modulo11cnpj(self):
    pjfinal = self
    if "." in pjfinal:
        cnpjqttdot = len(self.split('.'))
        cpj = 0
        fpj1 = pjfinal
        pjfinal = ""
        while (cnpjqttdot) > cpj:
            pjfinal = pjfinal + fpj1.split('.')[cpj]
            cpj+=1


    if "/" in pjfinal:
        cnpjqttbar = len(self.split('/'))
        cpj = 0
        fpj2 = pjfinal
        pjfinal = ""
        while (cnpjqttbar) > cpj:
            pjfinal = pjfinal + fpj2.split("/")[cpj]
            cpj+=1
    
    if "-" in pjfinal:
        cnpjqtthash = len(self.split('-'))
        cpj = 0
        fpj3 = pjfinal
        pjfinal = ""
        while (cnpjqtthash) > cpj:
            pjfinal = pjfinal + fpj3.split("-")[cpj]
            cpj+=1

    if "," in pjfinal:
        cnpjqttcomma = len(self.split(','))
        cpj = 0
        fpj4 = pjfinal
        pjfinal = ""
        while (cnpjqttcomma) > cpj:
            pjfinal = pjfinal + fpj4.split(",")[cpj]
            cpj+=1


    if pjfinal.isnumeric() == False:
        return 'INVÁLIDO'


    if len(pjfinal) != 14:
        return 'INVÁLIDO'
    cnpjtemp1 = (
        (int(pjfinal[0]) * 6) + 
        (int(pjfinal[1]) * 7) + 
        (int(pjfinal[2]) * 8) + 
        (int(pjfinal[3]) * 9) + 
        (int(pjfinal[4]) * 2) + 
        (int(pjfinal[5]) * 3) +
        (int(pjfinal[6]) * 4) + 
        (int(pjfinal[7]) * 5) + 
        (int(pjfinal[8]) * 6) +
        (int(pjfinal[9]) * 7) + 
        (int(pjfinal[10]) * 8) +
        (int(pjfinal[11]) * 9)
    )
    if cnpjtemp1 % 11 == None or cnpjtemp1 % 11 == 10:
        cnpjtemp1mod = 0
    else:
        cnpjtemp1mod = cnpjtemp1 % 11
    
    cnpjtemp2 = (
        (int(pjfinal[0]) * 5) +
        (int(pjfinal[1]) * 6) + 
        (int(pjfinal[2]) * 7) + 
        (int(pjfinal[3]) * 8) + 
        (int(pjfinal[4]) * 9) + 
        (int(pjfinal[5]) * 2) + 
        (int(pjfinal[6]) * 3) +
        (int(pjfinal[7]) * 4) + 
        (int(pjfinal[8]) * 5) + 
        (int(pjfinal[9]) * 6) +
        (int(pjfinal[10]) * 7) + 
        (int(pjfinal[11]) * 8) +
        (cnpjtemp1mod * 9)
    )
    if cnpjtemp2 % 11 == None or cnpjtemp2 % 11 == 10:
        cnpjtemp2mod = 0
    else:
        cnpjtemp2mod = cnpjtemp2 % 11

    if str(cnpjtemp1mod) + str(cnpjtemp2mod) == pjfinal[12] + pjfinal[13]:
        return 'VÁLIDO'
    else:
        return 'INVÁLIDO'




#-----------------------------------------------------------CEP-----------------------


def cepsearch(self):

    cepfinal = self

    if "." in cepfinal:
        cnpjqttdot = len(self.split('.'))
        cpj = 0
        fpj1 = cepfinal
        cepfinal = ""
        while (cnpjqttdot) > cpj:
            cepfinal = cepfinal + fpj1.split('.')[cpj]
            cpj+=1


    if "/" in cepfinal:
        cnpjqttbar = len(self.split('/'))
        cpj = 0
        fpj2 = cepfinal
        cepfinal = ""
        while (cnpjqttbar) > cpj:
            cepfinal = cepfinal + fpj2.split("/")[cpj]
            cpj+=1
    
    if "-" in cepfinal:
        cnpjqtthash = len(self.split('-'))
        cpj = 0
        fpj3 = cepfinal
        cepfinal = ""
        while (cnpjqtthash) > cpj:
            cepfinal = cepfinal + fpj3.split("-")[cpj]
            cpj+=1

    if "," in cepfinal:
        cnpjqttcomma = len(self.split(','))
        cpj = 0
        fpj4 = cepfinal
        cepfinal = ""
        while (cnpjqttcomma) > cpj:
            cepfinal = cepfinal + fpj4.split(",")[cpj]
            cpj+=1


    if cepfinal.isnumeric() == False:
        return 'false'

    if len(cepfinal) !=8 :
        return 'false'

    try:
        with urllib.request.urlopen(f"https://viacep.com.br/ws/{cepfinal}/json") as f:
            tempcepsearch = f.read().decode('utf-8')
    except urllib.error.URLError as e:
        return 'false'
      #  print(e.reason)

    splitstr = tempcepsearch.split()

   #-----------VAR: cepInfo--------------------
   #------------RUA

    tempRua = ""
    tempCounterRua = 4
    verifier = False

    while verifier == False:
        whileTemp = splitstr[tempCounterRua]
        if whileTemp == '"complemento":':
            cepRua = tempRua.split('"')[1]
            verifier = True
        else:
            tempRua += whileTemp
            tempRua += " "
            tempCounterRua+=1



   #------------BAIRRO

    tempBairro = ""
    tempCounterBairro = tempCounterRua+3
    verifier = False

    while verifier == False:
        whileTemp = splitstr[tempCounterBairro]
        if whileTemp == '"localidade":':
            cepBairro = tempBairro.split('"')[1]
            verifier = True
        else:
            tempBairro += whileTemp
            tempBairro += " "
            tempCounterBairro+=1



   #----------CIDADE

    tempCidade = ""
    tempCounterCidade = tempCounterBairro+1
    verifier = False

    while verifier == False:
        whileTemp = splitstr[tempCounterCidade]
        if whileTemp == '"uf":':
            cepCidade = tempCidade.split('"')[1]
            verifier = True
        else:
            tempCidade += whileTemp
            tempCidade += " "
            tempCounterCidade+=1



   #---------ESTADO

    tempEstado = ""
    tempCounterEstado = tempCounterCidade+1
    verifier = False

    while verifier == False:
        whileTemp = splitstr[tempCounterEstado]
        if whileTemp == '"ibge":':
            cepEstado = tempEstado.split('"')[1]
            verifier = True
        else:
            tempEstado += whileTemp
            tempEstado += " "
            tempCounterEstado+=1



   #-------------IBGE

    tempIbge = ""
    tempCounterIbge = tempCounterEstado+1
    verifier = False

    while verifier == False:
        whileTemp = splitstr[tempCounterIbge]
        if whileTemp == '"gia":':
            cepIbge = tempIbge.split('"')[1]
            verifier = True
        else:
            tempIbge += whileTemp
            tempIbge += " "
            tempCounterIbge+=1



   #------------DDD

    tempDDD = ""
    tempCounterDDD = tempCounterIbge+3
    verifier = False

    while verifier == False:
        whileTemp = splitstr[tempCounterDDD]
        if whileTemp == '"siafi":':
            cepDDD = tempDDD.split('"')[1]
            verifier = True
        else:
            tempDDD += whileTemp
            tempDDD += " "
            tempCounterDDD+=1


#---------------RETURN

    cepreturn = f"""
    Estado: {cepEstado}
    Cidade: {cepCidade}  (DDD: {cepDDD})
    Bairro: {cepBairro}
    Rua: {cepRua}
    Código IBGE: {cepIbge}

    """

    return cepEstado, cepCidade, cepDDD, cepBairro, cepRua, cepIbge
    # cepEstado, cepCidade, cepDDD, cepBairro, cepRua, cepIbge = functions.cepsearch(VARIABLE/CEP)



