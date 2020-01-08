import os

f = open("Dump.sql", "rb")
read = f.readline()

insert = False
inserts = 0

table = False
tables = 0

db = False
dbs = 0

linhas = 0
total = 0

arq = open("0", "wb")
while read:
    if "create " in read or "CREATE " in read:
        if "database" in read or "DATABASE" in read:
            arq.close()
            dbs+=1
            os.system("mkdir dbs")
            
            nome = str(read)
            nome = nome[nome.find("`")+1:]
            nome = nome[:nome.find("`")]

            arq = open("dbs\\" + nome + ".sql", "wb")
            db = True
    if "drop table" in read or "DROP TABLE" in read:
        arq.close()
        tables+=1
        os.system("mkdir tables")

        nome = str(read)
        nome = nome[nome.find("`")+1:]
        nome = nome[:nome.find("`")]

        arq = open("tables\\" + nome + ".sql", "wb")
        table = True

    if "insert" in read or "INSERT" in read:
        nome = str(read)
        nome = nome[nome.find("`")+1:]
        nome = nome[:nome.find("`")]

        if nome == "config_nova_certidao":
            arq.close()
            inserts+=1
            os.system("mkdir inserts")

            arq = open("inserts\\" + nome + str(inserts) + ".sql", "wb")
            insert = True

    if insert or table or db:
        if "_binary " in read:
            read = f.readline()
            continue

        if insert:
            insert = False

        arq.write(read)
        read = f.readline()

    total += 1

arq.close()
f.close()