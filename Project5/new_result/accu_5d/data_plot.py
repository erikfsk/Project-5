# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from data_dict import *
import re
import os

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)




for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[2:4])/100)
	label_text += "   $\\alpha = $" + str(0.5 + int(txtfile[-5:-4])*0.5)
	sum_y = sum(data["Y"])
	sum_xy = sum(data["Y"]*data["X"])
	accu_y = array([sum(data["Y"][:i])/sum_y for i in range(len(data["Y"]))])
	accu_xy = array([sum(data["Y"][:i]*data["X"][:i])/sum_xy for i in range(len(data["Y"]))])
	if 0 == int(txtfile[-5:-4]):
		plot(data["X"],accu_y*100,"k-",label=label_text)
		plot(data["X"],accu_xy*100,"k--",label=label_text)
		for j in range(4,5,2):
			for i in range(len(accu_xy)):
				if accu_xy[i] > 0.0999*(j+1):
					plot([data["X"][i],data["X"][i]],[accu_xy[i]*100,accu_y[i]*100],"ko")
					break
	elif 1 == int(txtfile[-5:-4]):
		plot(data["X"],accu_y*100,"m-",label=label_text)
		plot(data["X"],accu_xy*100,"m--",label=label_text)
		for j in range(4,5,2):
			for i in range(len(accu_xy)):
				if accu_xy[i] > 0.0999*(j+1):
					plot([data["X"][i],data["X"][i]],[accu_xy[i]*100,accu_y[i]*100],"mo")
					break
	elif 2 == int(txtfile[-5:-4]):
		plot(data["X"],accu_y*100,"g-",label=label_text)
		plot(data["X"],accu_xy*100,"g--",label=label_text)
		for j in range(4,5,2):
			for i in range(len(accu_xy)):
				if accu_xy[i] > 0.0999*(j+1):
					plot([data["X"][i],data["X"][i]],[accu_xy[i]*100,accu_y[i]*100],"go")
					break
	elif 3 == int(txtfile[-5:-4]):
		plot(data["X"],accu_y*100,"r-",label=label_text)
		plot(data["X"],accu_xy*100,"r--",label=label_text)
		for j in range(4,5,2):
			for i in range(len(accu_xy)):
				if accu_xy[i] > 0.0999*(j+1):
					plot([data["X"][i],data["X"][i]],[accu_xy[i]*100,accu_y[i]*100],"ro")
					break



ylabel("Accumulative percentage of total [%]",fontsize=20)
xlabel("Wealth [$]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-accu-persons-accu-money.pdf" ,bbox_inches="tight")
show()