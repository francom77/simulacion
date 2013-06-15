import numpy as np

class Corrida:

    def __init__(self, remises):
        #Variables de control
        self.remises = remises

        #Variables de resultado
        self.pte = 0
        self.pvnr = 0
        self.pto = 0

        #variables auxiliares
        self.ns = 0
        self.n = 0
        self.tpll = 0
        self.sto = 0
        self.stv = 0
        self.stp = 0
        self.svnr = 0
        self.t = 0
        self.cto = 0
        #tf esta en minutos, resulta de 6 hs por 60 min por 365 dias
        self.tf =  131400
        self.tps = []


        for x in range(1,remises):
            self.tps.append(0)

    def generarIA(self):

        "Genera el intervalo entre arribos"

        r = np.random.rand()
        x = 7*r + 3

        return x

    def generarTV(self):

        "Genera el tiempo de viaje"

        r = np.random.rand()
        x = 15*r + 5

        return x

    def generarDE(self):

        if self.ns < 5:
            de = 25
        elif self.ns < 10:
            de = 20
        elif self.ns < 15:
            de = 15
        elif self.ns < 20:
            de = 10
        elif self.ns < 25:
            de = 5
        elif self.ns >= 25:
            de = 3

        return de

    def tratarArrepentimiento(self):

        "Este metodo devuelve true o false, es decir si el pasajero viaja o no"

        de = self.generarDE()

        if de < 5:
            resul = True
        elif de < 10:
            r = np.random.rand()
            if r < 0.9:
                resul = True
            else:
                resul = False
                self.svnr+=1
        elif de < 20:
            r = np. random.rand()
            if r < 0.5:
                resul = True
            else:
                resul = False
                self.svnr+=1
        else: 
            r = np. random.rand()
            if r < 0.1:
                resul = True
            else:
                resul = False
                self.svnr+=1    

        return resul


    def realizarCorrida(self):

        while self.t <= self.tf:
            
            self.tps.sort()

            if (self.tpll <= self.tps[0]):
                self.stp = self.stp + (self.tpll - self.t) * self.ns
                self.t = self.tpll
                ia = self.generarIA()
                self.tpll = self.t + ia

                arr = self.tratarArrepentimiento()

                if arr:
                    self.ns += 1
                    self.n += 1

                    if self.ns <= self.remises:
                        tv = self.generarTV()
                        self.stv += tv
                        self.tps[0] = self.t + tv
                        self.sto = self.sto + (self.t - self.cto) * (self.remises - self.ns)

            else:
                self.stp = self.stp + (self.tps[0] - self.t) * self.ns
                self.t = self.tps[0]
                self.ns -= 1

                if self.ns <= self.remises:
                    tv = self.generarTV()
                    self.stv += tv
                    self.tps[0] = self.t + tv
                else:
                    self.cto = self.t
                    self.tps[0] = 400000 #un valor muy grande

        #calculo de resultados
        self.pte = (self.stp - self.stv) / self.n
        self.pvnr = (self.svnr * 100) / (self.n + self.svnr)
        self.pto = (self.sto / 365*60) / self.remises


