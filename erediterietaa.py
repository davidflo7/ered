class anagrafica():
    
        dati_personali =[]
        nome = "nome"
        cognome = "cognome"
        età = 18 
        professione = "professione"

        dati=anagrafica()

        dati.nome = input("insert your name")
        if(type(dati.nome) == str):
            dati.datipersonali.append(dati.nome)

            dati.cognome =input("insert your last name")
            if(type(dati.cognome) == str):
                dati.datipersonali.append(dati.cognome)

                dati.età = input("write your age")
                if(int(dati.età)):
                    dati.datipersonali.append(dati.età)

                    dati.professione =input("write your work")
                    if(type(dati.professione)==str) :
                        dati.datipersonali.append(dati.professione)

                        print(dati_personali)


        