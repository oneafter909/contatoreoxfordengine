import csv
from components.const import *


def count(text):
	punteggiatura = ["?",".",",","\"","\'","!",":",";","-","*", "(",")","!","/"]
	def CSVList():
		"""Useful method to retrieve the CSV list"""
		file = open(TERMS_LIST)
		csvreader = csv.reader(file, delimiter="\r")
		rows = []
		for row in csvreader:
			rows.append(row)
		return rows
	print("Contatore Oxford Engine (COX-e) Developed by Birbone")
	print("Analisi...")
	textsplit = text.split(' ')
	listaMoccoli = CSVList()
	partialCounter = 0
	pCounter = 0
	for parola in textsplit:
			for p in punteggiatura:
				if(p in parola):
					parola = parola.replace(p,"")
			for moccoli in listaMoccoli:
				if (parola.lower() == moccoli[0]):
					partialCounter += 1
					if(parola.lower() == "porco" or parola.lower() == "porca"):
						pCounter += 1

	return f"Ci sono {str(partialCounter)} moccoli. Con {str(pCounter)} porchi."