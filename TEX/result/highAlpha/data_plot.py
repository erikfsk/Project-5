# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from data_dict import *
from scipy.special import gamma
import re
import os

def pareto(x,a,k=1):
	return k*x**(-1-a)

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)

"""
for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "00" in txtfile or "50" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,3)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-0050.pdf" ,bbox_inches="tight")
clf()


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "90" in txtfile or "25" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,3)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-2590.pdf" ,bbox_inches="tight")
clf()



for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "00" in txtfile or "50" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-0050-log.pdf" ,bbox_inches="tight")
clf()


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "90" in txtfile or "25" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-2590-log.pdf" ,bbox_inches="tight")
clf()




for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "00" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-00-log.pdf" ,bbox_inches="tight")
clf()
"""

# ------------------- MIKAEL VAR HER ---------------------
for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "00" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			data1 = data["Y"]
			#loglog(data["X"],data1*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			data2 = data["Y"]
			#loglog(data["X"],data2*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			data3 = data["Y"]
			#loglog(data["X"],data3*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			data4 = data["Y"]
			#loglog(data["X"],data4*100,"r-",label=label_text)

"""
for i in range(len(data1)):
	if(data1[i] == 0):
		data1[i] = data1[i-1]

for i in range(len(data2)):
	if(data2[i] == 0):
		data2[i] = data2[i-1]

for i in range(len(data3)):
	if(data3[i] == 0):
		data3[i] = data3[i-1]

for i in range(len(data4)):
	if(data4[i] == 0):
		data4[i] = data4[i-1]
"""
data1 = data["Y"]
loglog(data["X"],data1)

#loglog(data["X"],fitting(data1,0.5))
#loglog(data["X"],pareto(data2,1.0))
#loglog(data["X"],fitting(data3,1.5))
#loglog(data["X"],fitting(data4,2.0))

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,20)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
show()
clf()

# ------------------------------------------------------------
"""

for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "25" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-25-log.pdf" ,bbox_inches="tight")
clf()


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "50" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-50-log.pdf" ,bbox_inches="tight")
clf()


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "90" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			semilogy(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-90-log.pdf" ,bbox_inches="tight")
clf()




























for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "00" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,3)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-00.pdf" ,bbox_inches="tight")
clf()


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "25" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,3)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-25.pdf" ,bbox_inches="tight")
clf()


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "50" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,3)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-50.pdf" ,bbox_inches="tight")
clf()


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	if "90" in txtfile:
		if 0 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			plot(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,3)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-90.pdf" ,bbox_inches="tight")
clf()
"""