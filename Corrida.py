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
        self.stv = 0
        self.stp = 0
        self.svnr = 0
        self.sde = 0
        self.t = 0

        #tf esta en minutos, resulta de 6 hs por 60 min por 365 dias
        self.tf = 131400
        self.tps = []
        self.sto = []
        self.cto = []
        for x in range(1, remises + 1):
            self.tps.append(400000)  # un valor muy grande
            self.sto.append(0)
            self.cto.append(0)

    def generarIA(self):

        "Genera el intervalo entre arribos"

        r = np.random.rand()
        x = 2 * r + 1

        return x

    def generarDE(self):

        "Genera la demora entre viaje y viaje"

        r = np.random.rand()
        x = 7 * r + 3

        return x

    def generarTV(self):

        "Genera el tiempo de viaje"

        r = np.random.rand()
        x = 15 * r + 5

        return x

    def tratarArrepentimiento(self):

        "Este metodo devuelve true o false, es decir si el pasajero viaja o no"

        cant = self.ns - self.remises
        if cant <= 1:
            resul = True
        elif cant <= 3:
            r = np.random.rand()
            if r < 0.9:
                resul = True
            else:
                resul = False
                self.svnr += 1
        elif cant <= 5:
            r = np.random.rand()
            if r < 0.5:
                resul = True
            else:
                resul = False
                self.svnr += 1
        else:
            r = np.random.rand()
            if r < 0.1:
                resul = True
            else:
                resul = False
                self.svnr += 1

        return resul

    def menorTPS(self):

        minimo = 500000
        posmin= "sin posicion"
        for x in range (0, len(self.tps)):
            if self.tps[x] < minimo:
                minimo = self.tps [x]
                posmin = x

        return posmin

    def menorTPSLibre(self):

        minimo = 500000
        posmin= "sin posicion"
        for x in range (0, len(self.tps)):
            if (self.tps[x] < minimo):

                if (self.tps[x] < self.t) or (self.tps[x] == 400000):
                    minimo = self.tps [x]
                    posmin = x

        return posmin

    def realizarVaciamiento(self):
        while self.ns > 0:
            minimo = self.menorTPS()
            self.stp = self.stp + (self.tps[minimo] - self.t) * self.ns
            self.t = self.tps[minimo]
            self.ns -= 1
            if self.ns >= self.remises:
                tv = self.generarTV()
                self.stv += tv
                self.tps[minimo] = self.t + tv
                de = self.generarDE()
                self.sde += de
            else:
                self.cto[minimo] = self.t
                self.tps[minimo] = 400000  # un valor muy grande            

    def calcularOciosos(self):

        "calculo para los que estan ociosos al terminar la simulacion"
        
        for x in range(0, len(self.tps)):
            if self.tps[x] == 400000:
                self.sto[x] = self.sto[x] + (self.t - self.cto[x])

    def realizarCorrida(self):

        while self.t <= self.tf:

            minimo = self.menorTPS()

            if (self.tpll <= self.tps[minimo]):
                self.stp = self.stp + (self.tpll - self.t) * self.ns
                self.t = self.tpll
                ia = self.generarIA()
                self.tpll = self.t + ia

                arr = self.tratarArrepentimiento()

                if arr:
                    self.ns += 1
                    self.n += 1

                    if self.ns <= self.remises:
                        minimo = self.menorTPSLibre()
                        tv = self.generarTV()
                        self.stv += tv
                        self.sto[minimo] = self.sto[minimo] + (self.t - self.cto[minimo])
                        self.tps[minimo] = self.t + tv
                        de = self.generarDE()
                        self.sde += de


            else:
                self.stp = self.stp + (self.tps[minimo] - self.t) * self.ns
                self.t = self.tps[minimo]
                self.ns -= 1

                if self.ns >= self.remises:
                    tv = self.generarTV()
                    self.stv += tv
                    self.tps[minimo] = self.t + tv
                    de = self.generarDE()
                    self.sde += de
                else:
                    self.cto[minimo] = self.t
                    self.tps[minimo] = 400000  # un valor muy grande

        self.calcularOciosos()
        self.realizarVaciamiento()

        #calculo de resultados
        self.pte = ((self.stp - self.stv) / self.n) + (self.sde / self.n)
        self.pte = round (self.pte, 2)

        self.pvnr = (self.svnr * 100) / (self.n + self.svnr)

        sum_sto = sum(self.sto)
        #self.pto = sum_sto / self.remises
        self.pto =  ((sum_sto / 365) / 60) / self.remises

        self.pto = round(self.pto, 2)

        print self.n
        print self.ns
        print self.t