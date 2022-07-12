from inspect import BoundArguments


class comune:
    def__init__(self,budget):
    self.totsbudget=budget
    def printbudget(self):
        print(self.totsbudget)

    class ASL(comune):
        def__init__(self,budget):
        comune.__init__(self,budget)
        def printbudget(self):
            print(self.totsbudget)

    class comunelocale(comune):
        def__init__(self,budget):
        def printbudget(self):
             print(self.totsbudget)


    budgetcomune=float(input("inserisci il budget a disposizione"))
    budget=float("budgetComune"0.3)
    x=comune(budget)
    x.printbudget()
    budget=float(budgetComune"0.6)
    y=ASL(budget)
    y.printbudget()
    budget=float(budgetComune0.6)
    z=comunelocale(budget)
    z.printbudget()





    class ospedale()
    listaospedalenomi=[]
    listaospedaleore=[]
    listapagamentieffettuati=[]
    listapagamentidaeffetturare=[]
    u=0
    Diziopersonale={}
    def__init__(self, DizioD,Dizio6):
    self.DizioDottori=DizioD
    self.DizioSpecialisti=DizioS

    def CREALISTA1(self):
        self.listaospedaleore.append(self.DizioDottori.keys())
        self.Listaospedareore.append(self.DizioSpecialisti.keys())
        return self.ListaOspedaleore

    def CREALISTANOMI(self):
            self.listaospedaleore.append(self.DizioDottori.values())
            self.listaospedalenomi.append(self.Diziospecialisti.keys())
            return self.Lisaospedalenomi
        

    def PAGAMENTIEFFETTUATI(self):
        for i in self.listaospedaleore:
            u= 60"self.listaospedaleore[i]
            self.listapagamentieffettuati-append(u)
            return self.listapagamenti.append(u)

    def PAGAMENTIDAEFFETTUARE(self)
    for i in self.listaospedaleore:
        u=30"self.listaospedaleore[i]
        self.listapagamentiedaeffettuare-append(u)
        return self.listapagamentidaeffettuare.append(u)

    def diziopagamenti(self):
        for k in self.listapagamenti:
            self.Diziopersoanle.update((self.listaospedalenomi[k]))self.listapersonale

            print(self.Diziopersonale)

    def diziopagamentidaeffettuare(self):
        for t in self.listapagamentidaeffettuare:
            self.Diziopersonale.update((self.listaospedalenomi[t]))self.listanomi

        print(self.Diziopersonale)
    
    def SVUOTAGIAPAGATI(self)
    while(self.listaospedaleore !=False):
        self.listaospedalenomi.clear()
        self.listapagmaenti.clear()

    

    class Dottore(ospedale):
        def ::init__(self)





    
