import wx
import matplotlib.pyplot as plt
import views
from Corrida import Corrida
from views.PrincipalFrame import PrincipalFrame
from wxPython.wx import *



class Controller:

    def __init__(self):
        
        self.corridas = []
        self.window = PrincipalFrame(None, -1, "simulacion")
        self.initUI()
        self.connectEvent()
        self.window.Centre()
        self.window.Show()


    def initUI(self):

        lista = self.window.resultados

        lista.InsertColumn(0, "Corrida", width=80)
        lista.InsertColumn(1, "Prom. Tiempo Ocioso", width=150)
        lista.InsertColumn(2, "Porc. Viajes no Realizados", width=200)
        lista.InsertColumn(3, "Cant. de Viajes no Realizados", width=200)
        lista.InsertColumn(4, "Prom. Tiempo de Espera", width=200)

        self.window.Corridas.SetValue(30)
        self.window.remises.SetValue(25)

    def connectEvent(self):

        self.window.simular.Bind(wx.EVT_BUTTON, self.simular)
        self.window.graficos.Bind(wx.EVT_BUTTON, self.graficos)

    def simular(self, event):

        corr = self.window.Corridas.GetValue() + 1 
        rem = self.window.remises.GetValue() + 1

        self.corridas = []
        self.window.resultados.DeleteAllItems()

        for x in range(1, corr):
            
            c = Corrida(rem)
            c.realizarCorrida()

            self.corridas.append(c)

        self.agregarCorridasLista()


    def graficos(self, event):
        
        lst_pto = []
        lst_pvrn = []
        lst_pte = []

        for c in self.corridas:

            lst_pto.append(c.pto)
            lst_pvrn.append(c.pto)
            lst_pte.append(c.pte)

        plt.figure("Graficos")
        plt.title("Variacion entre las corridas")
        plt.xlabel("Corridas")
        plt.plot(lst_pto, label= "Prom. Tiempo Ocioso")
        plt.plot(lst_pvrn, label= "Porc. Viajes no Realizados")
        plt.plot(lst_pte, label= "Prom. Tiempo de Espera")
        plt.legend(loc=2)
        plt.show()




    def agregarCorridasLista(self):
        lista= self.window.resultados

        for c in self.corridas:

            idx = lista.GetItemCount()
            lista.InsertStringItem(idx, "%s" % idx) 
            lista.SetStringItem(idx, 1, "%s" % c.pto) 
            lista.SetStringItem(idx, 2, "%s" % c.pvnr) 
            lista.SetStringItem(idx, 3, "%s" % c.svnr)
            lista.SetStringItem(idx, 4, "%s" % c.pte)


if __name__=='__main__':
    
    app = wx.App(False)
    controller = Controller()
    app.MainLoop()