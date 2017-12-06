# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from scipy.special import gamma
from data_dict import *
import re
import os

def fitting(x,lam):
	n = 1 + 3*lam/(1-lam)
	an = n**n/gamma(n)
	return an*x**(n-1)*exp(-n*x)


output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[-6:-4])/100)
	# plot(data["X"],fitting(data["X"],float(txtfile[-6:-4])/100),"b--")
	# if 0.0 == float(txtfile[-6:-4])/100:
	if "_00." == txtfile[-7:-3]:
		plot(data["X"],data["Y"]*100,"k-",label=label_text)
		plot(data["X"],fitting(data["X"],float(txtfile[-6:-4])/100),"r--",label="Gibbs distribution")


xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,4)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5a.pdf" ,bbox_inches="tight")
clf()



for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[-6:-4])/100)
	# plot(data["X"],fitting(data["X"],float(txtfile[-6:-4])/100),"b--")
	# if 0.0 == float(txtfile[-6:-4])/100:
	if "_00." == txtfile[-7:-3]:
		semilogy(data["X"],data["Y"]*100,"k-",label=label_text)
		semilogy(data["X"],fitting(data["X"],float(txtfile[-6:-4])/100),"r--",label="Gibbs distribution")


xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
ylim(10**-4.2,10**1)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5b.pdf" ,bbox_inches="tight")
clf()


