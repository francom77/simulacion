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
		self.sta = 0
		self.stp = 0
		self.svnr = 0
		self.t = 0
		self.cto = 0
		#tf esta en minutos, resulta de 6 hs por 60 min por 365 dias
		self.tf =  131400
		self.tps = []


		for x in xrange(1,remises):
			tps.append(0) #un valor muy grande

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

		if ns < 5:
			de = 25
		elif ns < 10:
			de = 20
		elif ns < 15:
			de = 15
		elif ns < 20:
			de = 10
		elif ns < 25
			de = 5
		elif ns >= 25:
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

		while t <= tf:
			
			self.tps.sort()

			if (tpll <= tps[0]):
				stp = stp + (tpll - t) * ns
				t = tpll
				ia = self.generarIA()
				tpll = t + ia

				arr = self.tratarArrepentimiento()

				if arr:
					ns += 1
					n += 1

					if ns <= remises:
						tv = self.generarTV()
						stv += tv
						tps[0] = t + tv
						sto = sto + (t - cto) * (remises - ns)

			else:
				stp = stp + (tps[0] - t) * ns
				t = tps[0]
				ns -= 1

				if ns <= remises:
					tv = self.generarTV()
					stv += tv
					tps[0] = t + tv
				else:
					cto = t
					tps[0] = 400000 #un valor muy grande

		#calculo de resultados
		pte = (stp - stv) / remises
		pvnr = (svnr * 100) / (n + svnr)
		pto = (pto * 100) / t


