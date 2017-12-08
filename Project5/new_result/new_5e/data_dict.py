# -*- coding: utf-8 -*-
from matplotlib.pyplot import *
from numpy import *

def data_dict(txtfile):
	with open(txtfile,"r") as infile:
		data = {}
		identifiers = infile.readline().split()
		for identifier in identifiers:
			data[identifier] = []

		lines = infile.readlines()
		for line in lines: 
			values = line.split()
			for identifier,value in zip(identifiers,values):
				data[identifier].append(float(value))
		for identifier in identifiers:
			data[identifier] = array(data[identifier])
	return data

def label_(txtfile):
	return "$\\alpha = $" + txtfile[2:3] + "   $\lambda = $" + str(float(txtfile[-8:-6])/100) + "   $\gamma = $" + txtfile[-5:-4]

def make_plot(savefile):
	xlabel("Wealth [$]",fontsize=20)
	ylabel("Probability [%]",fontsize=20)
	xticks(fontsize=20)
	yticks(fontsize=20)
	xlim(0,10)
	grid("on")
	tight_layout()
	legend(loc="best",fontsize=20)
	savefig(savefile ,bbox_inches="tight")
	show()

def plot_plot(constraint1, constraint2, data, txtfile, label_text):
	if constraint1 == txtfile[2:3] and constraint2  == txtfile[-8:-6]:
		if 0 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"r-",label=label_text)
		elif 4 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"m-",label=label_text)

def plot_semi(constraint1, constraint2, data, txtfile, label_text):
	if constraint1 == txtfile[2:3] and constraint2  == txtfile[-8:-6]:
		if 0 == int(txtfile[-5:-4]):
			loglog(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			loglog(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			loglog(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			loglog(data["X"],data["Y"]*100,"r-",label=label_text)
		elif 4 == int(txtfile[-5:-4]):
			loglog(data["X"],data["Y"]*100,"m-",label=label_text)
