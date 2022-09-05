from asyncore import read
import json
import pymongo
import time
import json


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["local"]
mycol = mydb["RANU"]

list = []
dic = {}
fatores = []

file = open("Datawarehouse_Final.csv","r",encoding='utf-8')
line = file.readline()
cnt = 1
#print(line)
#z = line.strip().split(";")

while line:
    z = line.strip().split(";")
    num_seq = z[0]
    processo = z[1]
    data_nascimento = z[2]
    hora = z[3]
    gestacao = z[4]
    peso = z[5]
    sexo = z[6]
    puerperio = z[7]
    local_nascimento = z[8]
    apgar1 = z[9]
    apgar5 = z[10]
    avaliacao1 = z[11]
    data_avaliacao1 = z[12]
    nmec_avaliador1 = z[13]
    data_avaliacaor = z[14]
    risco = z[15]
    nmec_avaliadorr = z[16]
    avaliacao2 = z[17]
    data_avaliacao2 = z[18]
    nmec_avaliador2 = z[19]
    avaliacao3 = z[20]
    data_avaliacao3 = z[21]
    nmec_avaliador3 = z[22]
    fator1 = z[23]
    fator2 = z[24]
    fator3 = z[25]
    fator4 = z[26]
    fator5 = z[27]
    fator6 = z[28]
    fator7 = z[29]
    fator8 = z[30]
    fator9 = z[31]
    fator10 = z[32]
    #print(type(time.strftime("%H:%M:%S", time.gmtime(int(hora)))))
    #if fator10 == "1":
    #    print(fator10)
    ########################################### Birth Registration RANU ##################################################
    #dic["patient ID"] = num_seq
    #dic["process ID"] = processo
    #dic["date/time of birth"] = data_nascimento + " " + time.strftime("%H:%M:%S", time.gmtime(int(hora)))
    data_nascimento = data_nascimento + " " + time.strftime("%H:%M:%S", time.gmtime(int(hora)))
    #print(dic["date/time of birth"])
    #dic["pregnancy duration"] = gestacao
    #dic["birthweight"] = {"magnitude":peso,"units":"g"}
    #----------------------------------------------------SEXO-------------------------------------------------------------
    if sexo == "2":
        sexo = "at0114"
        sexot = "Female"
        #dic["sex"] ={"terminology_id":sexo,"code_string":sexot}
    elif sexo == "1":
        sexo = "at0113"
        sexot = "Male"
        #dic["sex"] ={"terminology_id":sexo,"code_string":sexot}
    else :
        sexo = "at0115"
        sexot = "Undefined"
        #dic["sex"] ={"terminology_id":sexo,"code_string":sexot}
    #--------------------------------------------------PUERPÉRIO----------------------------------------------------------
    if puerperio == "N":
        puerperio = "at0242"
        puerperiot = "Normal"
        #dic["puerperium"] = {"terminology_id":puerperio,"code_string":puerperiot}
    elif puerperio == "C":
        puerperio = "at0241"
        puerperiot = "Complicated"
        #dic["puerperium"] = {"terminology_id":puerperio,"code_string":puerperiot}
    else :
        puerperio = None
        puerperiot = None
        #dic["puerperium"] = None
    #----------------------------------------------------LOCAL------------------------------------------------------------
    if local_nascimento == "I":
        local_nascimento = "at0120"
        local_nascimentot = "Internal"
        #dic["place of birth category"] = {"terminology_id":local_nascimento,"code_string":local_nascimentot}
    elif local_nascimento == "E":
        local_nascimento = "at0188"
        local_nascimentot = "External"
        #dic["place of birth category"] = {"terminology_id":local_nascimento,"code_string":local_nascimentot}
    else :
        local_nascimento = None
        local_nascimentot = None
        #dic["place of birth category"] = None

    dic["Birth Registration RANU"] = {"data":{"Pregnancy":{"Pregnancy Duration":gestacao,"Puerperium":{"terminology_id":puerperio,"code_string":puerperiot}},"Childbirth":{"Place of Birth Category":{"terminology_id":local_nascimento,"code_string":local_nascimentot}},"Newborn":{"Date/Time of Birth": data_nascimento, "Sex":{"terminology_id":sexo,"code_string":sexot},"Birthweight":{"magnitude":peso,"units":"g"}}},"protocol":{"Patient ID":num_seq, "Process ID":processo}}


    ############################################## APGAR SCORE ###########################################################
    dic["Apgar Score"] = {"data":{"1 minute":{"data":{"Total":apgar1}}, "5 minute":{"data":{"Total":apgar5}}}}
    
    ################################################ PHASE 1 #############################################################
    if avaliacao1 == "1":
        avaliacao1 = "at0011"
        avaliacao1t = "Pass"
        dic["phase 1"] = {"data":{"evaluation":{"terminology_id":avaliacao1, "code_string":avaliacao1t}, "evaluation date":data_avaliacao1}, "protocol": {"evaluator ID": nmec_avaliador1}}
    elif avaliacao1 == "2":
        avaliacao1 = "at0014"
        avaliacao1t = "Refer Both"
        dic["phase 1"] = {"data":{"evaluation":{"terminology_id":avaliacao1, "code_string":avaliacao1t}, "evaluation date":data_avaliacao1}, "protocol": {"evaluator ID": nmec_avaliador1}}
    elif avaliacao1 == "3":
        avaliacao1 = "at0013"
        avaliacao1t = "Refer Right"
        dic["phase 1"] = {"data":{"evaluation":{"terminology_id":avaliacao1, "code_string":avaliacao1t}, "evaluation date":data_avaliacao1}, "protocol": {"evaluator ID": nmec_avaliador1}}
    elif avaliacao1 == "4":
        avaliacao1 = "at0012"
        avaliacao1t = "Refer Left"
        dic["phase 1"] = {"data":{"evaluation":{"terminology_id":avaliacao1, "code_string":avaliacao1t}, "evaluation date":data_avaliacao1}, "protocol": {"evaluator ID": nmec_avaliador1}}
    else:
        dic["phase 1"] = None
    ################################################ PHASE 2 #############################################################
    if avaliacao2 == "1":
        avaliacao2 = "at0011"
        avaliacao2t = "Pass"
        dic["phase 2"] = {"data":{"evaluation":{"terminology_id":avaliacao2, "code_string":avaliacao2t}, "evaluation date":data_avaliacao2}, "protocol": {"evaluator ID": nmec_avaliador2}}
    elif avaliacao2 == "2":
        avaliacao2 = "at0014"
        avaliacao2t = "Refer Both"
        dic["phase 2"] = {"data":{"evaluation":{"terminology_id":avaliacao2, "code_string":avaliacao2t}, "evaluation date":data_avaliacao2}, "protocol": {"evaluator ID": nmec_avaliador2}}
    elif avaliacao2 == "3":
        avaliacao2 = "at0013"
        avaliacao2t = "Refer Right"
        dic["phase 2"] = {"data":{"evaluation":{"terminology_id":avaliacao2, "code_string":avaliacao2t}, "evaluation date":data_avaliacao2}, "protocol": {"evaluator ID": nmec_avaliador2}}
    elif avaliacao2 == "4":
        avaliacao2 = "at0012"
        avaliacao2t = "Refer Left"
        dic["phase 2"] = {"data":{"evaluation":{"terminology_id":avaliacao2, "code_string":avaliacao2t}, "evaluation date":data_avaliacao2}, "protocol": {"evaluator ID": nmec_avaliador2}}
    else:
        dic["phase 2"] = None
    ################################################ PHASE 3 #############################################################
    if avaliacao3 == "1":
        avaliacao3 = "at0011"
        avaliacao3t = "Pass"
        dic["phase 3"] = {"data":{"evaluation":{"terminology_id":avaliacao3, "code_string":avaliacao3t}, "evaluation date":data_avaliacao3}, "protocol": {"evaluator ID": nmec_avaliador3}}
    elif avaliacao3 == "2":
        avaliacao3 = "at0014"
        avaliacao3t = "Refer Both"
        dic["phase 3"] = {"data":{"evaluation":{"terminology_id":avaliacao3, "code_string":avaliacao3t}, "evaluation date":data_avaliacao3}, "protocol": {"evaluator ID": nmec_avaliador3}}
    else:
        dic["phase 3"] = None
    
    ####################################### Deafness Risk Factors in Newborn #############################################
    if fator1 == "1":
        f1={"terminology_id":"at0029", "code_string":"Family history of congenital sensorineural hearing loss"}
        fatores.append(f1)
    if fator2 == "1":
        f2={"terminology_id":"at0034", "code_string":"Congenital infectious disease"}
        fatores.append(f2)
    if fator3 == "1":
        f3={"terminology_id":"at0039", "code_string":"Congenital anomaly of face"}
        fatores.append(f3)
    if fator4 == "1":
        f4={"terminology_id":"at0049", "code_string":"Hyperbilirubinemia"}
        fatores.append(f4)
    if fator5 == "1":
        f5={"terminology_id":"at0040", "code_string":"Low birth weight infant"}
        fatores.append(f5)
    if fator6 == "1":
        f6={"terminology_id":"at0047", "code_string":"Ototoxic medication"}
        fatores.append(f6)
    if fator7 == "1":
        f7={"terminology_id":"at0042", "code_string":"Bacterial meningitis"}
        fatores.append(f7)
    if fator8 == "1":
        f8={"terminology_id" : "at0043","code_string" : "Apgar at 1 minute and at 5 min"}
        fatores.append(f8)
    if fator9 == "1":
        f9={"terminology_id" : "at0046","code_string" : "Artificial respiration"}
        fatores.append(f9)
    if fator10 == "1":
        f10={"terminology_id" : "at0045","code_string" : "Deafness symptom"}
        fatores.append(f10)
    ##################################################### RISK ##################################################################
    if risco == "2": 
        risco = "at0055"
        riscot = "Late risk factors"
        dic["Deafness Risk Factors in Newborn"] = {"data":{"risk":{"terminology_id":risco, "code_string":riscot,"screening date":data_avaliacaor},"Risk factors":fatores},"protocol":{"evaluator ID": nmec_avaliadorr}}
    elif risco == "1": 
        risco = "at0054"
        riscot = "Only risk factors"
        dic["Deafness Risk Factors in Newborn"] = {"data":{"risk":{"terminology_id":risco, "code_string":riscot,"screening date":data_avaliacaor},"Risk factors":fatores},"protocol":{"evaluator ID": nmec_avaliadorr}}
    elif risco == "0": 
        risco = "at0053"
        riscot = "No risk factors"
        dic["Deafness Risk Factors in Newborn"] = {"data":{"risk":{"terminology_id":risco, "code_string":riscot,"screening date":data_avaliacaor},"Risk factors":fatores},"protocol":{"evaluator ID": nmec_avaliadorr}}
    else:
        dic["Deafness Risk Factors in Newborn"] = None

    list.append(dic)
    line = file.readline()
    cnt += 1
    dic={}
    fatores=[]
    

#print(dic)
#print (list)
print ("Lines: ", cnt)
#test = open("test.json","w", encoding="utf-8")
#json.dump(list,test,ensure_ascii= False,indent=4)
mycol.insert_many(list)