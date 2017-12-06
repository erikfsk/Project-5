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
	plot(data["X"],data["Y"]*100,"-",label=label_text)
	plot(data["X"],fitting(data["X"],float(txtfile[-6:-4])/100),"r--",label="Gibbs distribution")

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,5)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5a-test.pdf" ,bbox_inches="tight")
show()




