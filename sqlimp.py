from asyncio.windows_events import NULL
from bson.json_util import dumps
from pymongo import MongoClient
import mysql.connector
from datetime import datetime
import pandas as pd
import maskpass

client = MongoClient("mongodb://localhost:27017/")
db = client.local
collection = db.RANU

#dada a dimensao do dataset e necessario alterar o ficheiro my.ini abrindo o ficheiro no notepad como admin e definir max_allowed_packet=64M caso 
#contrario o servidor dara timeout


pwd = maskpass.askpass()
documents_count = collection.count_documents({})
print(documents_count)
cnt=0 
records_to_insert=[]

def days_between(d1, d2):

    d1=datetime.strptime(str(d1),'%Y-%m-%dT%H:%M:%S')
    d2=datetime.strptime(str(d2),'%Y-%m-%dT%H:%M:%S')
    return abs((d2 - d1).days)

if __name__ == '__main__':
    lista=[]
    #preciso mudar aqui as variaveis consoante a base de dados a ser usada
    connection = mysql.connector.connect(host='localhost',user='root', database='pce', password=f'{pwd}')
    cursor = collection.find({})
    #print(cursor)
    

    for document in cursor:
        cnt+=1
        #print(cnt)
        gestacao = int(document["Birth Registration RANU"]["data"]["Pregnancy"]["Pregnancy Duration"])
        #print(gestacao)
        
        puerperio = document["Birth Registration RANU"]["data"]["Pregnancy"]["Puerperium"]["code_string"]
        if puerperio == None:
            puerperio = "Unknown"
        print(puerperio)
        #code_puerperio = document["Birth Registration RANU"]["data"]["Pregnancy"]["Puerperium"]["terminology_id"]
        local_nascimento = document["Birth Registration RANU"]["data"]["Childbirth"]["Place of Birth Category"]["code_string"]
        #code_local_nascimento = document["Birth Registration RANU"]["data"]["Childbirth"]["Place of Birth Category"]["terminology_id"]
        #transformar em datetime
        data_nascimento = datetime.strptime(document["Birth Registration RANU"]["data"]["Newborn"]["Date/Time of Birth"],'%d/%m/%Y %H:%M:%S')
        data_nascimento = data_nascimento.isoformat()
        #print(data_nascimento)
        #sexo
        sexo = document["Birth Registration RANU"]["data"]["Newborn"]["Sex"]["code_string"]
        if sexo ==None:
            sexo = "Unknown"
        #code_sexo = document["Birth Registration RANU"]["data"]["Newborn"]["Sex"]["terminology_id"]
        #peso dadas as diferentes unidades e passar os valores para int
        if document["Birth Registration RANU"]["data"]["Newborn"]["Birthweight"]["units"] == "g":
            peso = int(document["Birth Registration RANU"]["data"]["Newborn"]["Birthweight"]["magnitude"])
        else:
            #passar de lb para g
            peso = int(document["Birth Registration RANU"]["data"]["Newborn"]["Birthweight"]["magnitude"])//2.2046
        #passar para int o num_seq, o num_processo, apgar1 e apgar5
        num_seq = document["Birth Registration RANU"]["protocol"]["Patient ID"]
        num_processo = document["Birth Registration RANU"]["protocol"]["Process ID"]
        apgar1 = document["Apgar Score"]["data"]["1 minute"]["data"]["Total"]
        if apgar1 == "":
            apgar1 = "Unknown"
        else:
            apgar1 = apgar1
        apgar5 = document["Apgar Score"]["data"]["5 minute"]["data"]["Total"]
        if apgar5 == "":
            apgar5 = "Unknown"
        else:
            apgar5 = apgar5
        if document["phase 1"] != None:
            avaliacao1 = document["phase 1"]["data"]["evaluation"]["code_string"]
            #code_avaliacao1 = document["phase 1"]["data"]["evaluation"]["terminology_id"]
            data_avaliacao1 = datetime.strptime(document["phase 1"]["data"]["evaluation date"],'%d/%m/%Y')
            data_avaliacao1 = data_avaliacao1.isoformat()
            nmec_avaliador1 = document["phase 1"]["protocol"]["evaluator ID"]
        else:
            avaliacao1 = "Unknown"
            data_avaliacao1 =datetime.strptime('01/01/0001','%d/%m/%Y').isoformat()
            nmec_avaliador1 =NULL
        if document["phase 2"] != None:
            avaliacao2 = document["phase 2"]["data"]["evaluation"]["code_string"]
            #code_avaliacao2 = document["phase 2"]["data"]["evaluation"]["terminology_id"]
            data_avaliacao2 = datetime.strptime(document["phase 2"]["data"]["evaluation date"],'%d/%m/%Y')
            data_avaliacao2 = data_avaliacao2.isoformat()
            nmec_avaliador2 = document["phase 2"]["protocol"]["evaluator ID"]
        else:
            avaliacao2 = "Unknown"
            data_avaliacao2 = datetime.strptime('01/01/0001','%d/%m/%Y').isoformat()
            nmec_avaliador2 = NULL
        if document["phase 3"] != None:
            avaliacao3 = document["phase 3"]["data"]["evaluation"]["code_string"]
            #code_avaliacao3 = document["phase 3"]["data"]["evaluation"]["terminology_id"]
            data_avaliacao3 = datetime.strptime(document["phase 3"]["data"]["evaluation date"],'%d/%m/%Y')
            data_avaliacao3 = data_avaliacao3.isoformat()
            nmec_avaliador3 = document["phase 3"]["protocol"]["evaluator ID"]
        else:
            avaliacao3="Unknown"
            #data_avaliacao3="null"
            #data_avaliacao3=pd.to_datetime(data_avaliacao3)
            #print(type(data_avaliacao3))
            #data_avaliacao3 = pd.to_datetime(data_avaliacao3)
            data_avaliacao3 = datetime.strptime('01/01/0001','%d/%m/%Y').isoformat()
            #data_avaliacao3 = ''
            #data_avaliacao3 = data_avaliacao3.isoformat()
            #print("AQQQQQQQUUIII",type(data_avaliacao3))
            nmec_avaliador3 = NULL
            #print(data_avaliacao3)
        
        
        if document["Deafness Risk Factors in Newborn"] != None:
            nmec_avaliadorr = document["Deafness Risk Factors in Newborn"]["protocol"]["evaluator ID"]
            #code_risco= document["Deafness Risk Factors in Newborn"]["data"]["risk"]["terminology_id"]
            risco = document["Deafness Risk Factors in Newborn"]["data"]["risk"]["code_string"]
            data_avaliacaor = datetime.strptime(document["Deafness Risk Factors in Newborn"]["data"]["risk"]["screening date"],'%d/%m/%Y')
            data_avaliacaor = data_avaliacaor.isoformat()
            #print(nmec_avaliadorr)
            #print(cnt)
            
        else:
            nmec_avaliadorr =NULL
            risco = "Unknown"
            data_avaliacaor = datetime.strptime('01/01/0001','%d/%m/%Y').isoformat()
            
            
        #por default os fatores a 0
        for i in range(1,11):
            exec(f'fator{i} = "No risk factor"')
        
        if document["Deafness Risk Factors in Newborn"] != None:
            fatores= document["Deafness Risk Factors in Newborn"]["data"]["Risk factors"]
            for x in fatores:
                #print(x)
                if x['terminology_id'] == "at0029":
                    #print("fator1: ", 1)
                    fator1 = x['code_string']
                #print(fator1)
                if x['terminology_id'] == "at0034":
                    #print("fator2: ", 1)
                    fator2 = x['code_string']
                #print(fator2)
                if x['terminology_id'] == "at0039":
                    #print("fator3: ", 1)
                    fator3 = x['code_string']
                #print(fator3)
                if x['terminology_id'] == "at0049":
                    #print("fator4: ", 1)
                    fator4 = x['code_string']
                #print(fator4)
                if x['terminology_id'] == "at0040":
                    #print("fator5: ", 1)
                    fator5 = x['code_string']
                #print(fator5)
                if x['terminology_id'] == "at0047":
                    #print("fator6: ", 1)
                    fator6 = x['code_string']
                #print(fator6)
                if x['terminology_id'] == "at0042":
                    #print("fator7: ", 1)
                    fator7 = x['code_string']
                #print(fator7)
                if x['terminology_id'] == "at0043":
                    #print("fator8: ", 1)
                    fator8 = x['code_string']
                #print(fator8)
                if x['terminology_id'] == "at0046":
                    #print("fator9: ", 1)
                    fator9 = x['code_string']
                #print(fator9)
                if x['terminology_id'] == "at0045":
                    #print("fator10: ", 1)
                    fator10 = x['code_string']
                #print(fator10)
       
        #idade do bebe em dias na avaliacao1
        if data_avaliacao1 != "0001-01-01T00:00:00":
            idade1= days_between(data_nascimento,data_avaliacao1)
        #idade do bebe em dias na avaliacao2
        else:
            #idade1=None
            idade1=NULL
        #print("idade1 ",idade1)
        if data_avaliacao2 != "0001-01-01T00:00:00":
            idade2= days_between(data_nascimento,data_avaliacao2)
            #print(cnt)
            #print("idade2 ",time2)
        else:
            idade2=NULL
        #idade do bebe em dias na avaliacao3
        if data_avaliacao3 != "0001-01-01T00:00:00":
            idade3= days_between(data_nascimento,data_avaliacao3)
            #print("idade3 ",idade3)
        else:
            idade3 = NULL
        #calculo de tempo entre a avaliacao 1 e a 2
        if data_avaliacao1!= "0001-01-01T00:00:00" and data_avaliacao2 != "0001-01-01T00:00:00":
            tempo1_2= days_between(data_avaliacao1,data_avaliacao2)
            #print(cnt)
            #print("time1_2 ", time1_2)
        #calculo de tempo entre a avaliacao 3 e a 2
        else:
            tempo1_2=NULL
        if data_avaliacao3!= "0001-01-01T00:00:00" and data_avaliacao2!= "0001-01-01T00:00:00":
            tempo2_3= days_between(data_avaliacao2,data_avaliacao3)
            #print(cnt)
            #print("time2_3 ", time2_3)
        else:
            tempo2_3=NULL
        person=(num_seq,num_processo,data_nascimento,gestacao,peso,data_avaliacao1,nmec_avaliador1,data_avaliacao2,nmec_avaliador2,data_avaliacao3,
        nmec_avaliador3,data_avaliacaor,nmec_avaliadorr,idade1,idade2,idade3,tempo1_2,tempo2_3,sexo,local_nascimento,apgar1,apgar5,puerperio,risco,avaliacao3,
        avaliacao2,avaliacao1,fator1,fator2,fator3,fator4,fator5,fator6,fator7,fator8,fator9,fator10)
        print(person)
        records_to_insert.append(person)
        

       
        
        print("PROGRESSO: %d/%d"%(cnt,documents_count))
        
        
        #if cnt ==1:
           # break
    #print(lista)
    #print(documents_count)
    #print(document["phase 3"]["data"]["evaluation"]["code_string"])
    #print(records_to_insert)
    mySql_insert_query = f"""INSERT INTO FACT_RANU (num_seq, num_processo, data_nascimento, gestacao,peso,data_avaliacao1,nmec_avaliador1,data_avaliacao2,
        nmec_avaliador2,data_avaliacao3,nmec_avaliador3,data_avaliacao_r,nmec_avaliador_r,idade1,idade2,idade3,tempo1_2,tempo2_3,sexo,local_nascimento,apgar1,
        apgar5,puerperio,risco,avaliacao3,avaliacao2,avaliacao1,fator1,fator2,fator3,fator4,fator5,fator6,fator7,fator8,fator9,fator10) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,(select id from DIM_sexo where descricao = %s),
        (select id from DIM_LocalNascimento where descricao=%s), (select id from DIM_Apgar1 where descricao = %s),(select id from DIM_Apgar5 where descricao = %s),
        (select id from DIM_Puerperio where descricao=%s), (select id from DIM_Risco where descricao=%s),(select id from DIM_Avaliacao3 where descricao = %s),
        (select id from DIM_Avaliacao2 where descricao = %s),(select id from DIM_Avaliacao1 where descricao = %s),(select id from DIM_Fator1 where descricao = %s),
        (select id from DIM_Fator2 where descricao = %s),(select id from DIM_Fator3 where descricao = %s),(select id from DIM_Fator4 where descricao = %s),
        (select id from DIM_Fator5 where descricao = %s),(select id from DIM_Fator6 where descricao = %s),(select id from DIM_Fator7 where descricao = %s),
        (select id from DIM_Fator8 where descricao = %s),(select id from DIM_Fator9 where descricao = %s),(select id from DIM_Fator10 where descricao = %s)) """

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query,records_to_insert)
    print(cursor.rowcount, "Record inserted successfully")

    #visto que o conetor do sql nao interpreta nones e o python muda null para 0 substituimos todas os atributos por nulo onde a data é a que foi 
    # considerada como nula ('0001-01-01T00:00:00')
    sql_update_query3 = """UPDATE FACT_RANU set data_avaliacao3 = NULL, tempo2_3 = NULL, idade3 = NULL, nmec_avaliador3 = NULL
     where data_avaliacao3 = '0001-01-01T00:00:00'"""
    sql_update_query2 = """UPDATE FACT_RANU set data_avaliacao2 = NULL, tempo1_2 = NULL, idade2 = NULL, nmec_avaliador2 = NULL
     where data_avaliacao2 = '0001-01-01T00:00:00'"""
    sql_update_query1 = """UPDATE FACT_RANU set data_avaliacao1 = NULL, idade1 = NULL, nmec_avaliador1 = NULL
     where data_avaliacao1 = '0001-01-01T00:00:00'"""
    sql_update_queryr = """UPDATE FACT_RANU set data_avaliacao_r = NULL, nmec_avaliador_r = NULL
     where data_avaliacao_r = '0001-01-01T00:00:00'"""
    
    
    cursor.execute(sql_update_query3)
    cursor.execute(sql_update_query2)
    cursor.execute(sql_update_query1)
    connection.commit()
    

if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")


"""except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")"""