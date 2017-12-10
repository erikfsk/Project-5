# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from data_dict import *
import re
import os

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[-6:-4])/100)
	# plot(data["X"],fitting(data["X"],float(txtfile[-6:-4])/100),"b--")
	# if 0.0 == float(txtfile[-6:-4])/100:
	print sum(data["X"]*data["Y"])
	if "_00." == txtfile[-7:-3]:
		plot(data["X"],data["X"]*data["Y"]*100,"k-",label=label_text)
	elif 25 == int(txtfile[-6:-4]):
		plot(data["X"],data["X"]*data["Y"]*100,"m-",label=label_text)
	elif 50 == int(txtfile[-6:-4]):
		plot(data["X"],data["X"]*data["Y"]*100,"g-",label=label_text)
	elif 90 == int(txtfile[-6:-4]):
		plot(data["X"],data["X"]*data["Y"]*100,"r-",label=label_text)


ylabel("Percentage of total wealth [%]",fontsize=20)
xlabel("Wealth [$]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,4)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5c-prosent-wealth-per-wealth-bin.pdf" ,bbox_inches="tight")
show()


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\lambda = $" + str(float(txtfile[-6:-4])/100)
	# plot(data["X"],fitting(data["X"],float(txtfile[-6:-4])/100),"b--")
	# if 0.0 == float(txtfile[-6:-4])/100:
	print sum(data["X"]*data["Y"])
	sum_y = sum(data["Y"])
	sum_xy = sum(data["Y"]*data["X"])
	accu_y = array([sum(data["Y"][:i])/sum_y for i in range(len(data["Y"]))])
	accu_xy = array([sum(data["Y"][:i]*data["X"][:i])/sum_xy for i in range(len(data["Y"]))])
	print len(accu_y*100),len(data["X"])
	if "_00." == txtfile[-7:-3]:
		plot(data["X"],accu_y*100,"k-",label=label_text)
		plot(data["X"],accu_xy*100,"k--",label=label_text)
		for j in range(4,5,2):
			for i in range(len(accu_xy)):
				if accu_xy[i] > 0.099*(j+1):
					plot([data["X"][i],data["X"][i]],[accu_xy[i]*100,accu_y[i]*100],"ko")
					break


	elif 25 == int(txtfile[-6:-4]):
		plot(data["X"],accu_y*100,"m-",label=label_text)
		plot(data["X"],accu_xy*100,"m--",label=label_text)
		for j in range(4,5,2):
			for i in range(len(accu_xy)):
				if accu_xy[i] > 0.099*(j+1):
					plot([data["X"][i],data["X"][i]],[accu_xy[i]*100,accu_y[i]*100],"mo")
					break

	elif 50 == int(txtfile[-6:-4]):
		plot(data["X"],accu_y*100,"g-",label=label_text)
		plot(data["X"],accu_xy*100,"g--",label=label_text)
		for j in range(4,5,2):
			for i in range(len(accu_xy)):
				if accu_xy[i] > 0.099*(j+1):
					plot([data["X"][i],data["X"][i]],[accu_xy[i]*100,accu_y[i]*100],"go")
					break

	elif 90 == int(txtfile[-6:-4]):
		plot(data["X"],accu_y*100,"r-",label=label_text)
		plot(data["X"],accu_xy*100,"r--",label=label_text)
		for j in range(4,5,2):
			for i in range(len(accu_xy)):
				if accu_xy[i] > 0.099*(j+1):
					plot([data["X"][i],data["X"][i]],[accu_xy[i]*100,accu_y[i]*100],"ro")
					break



ylabel("Accumulative percentage of total [%]",fontsize=20)
xlabel("Wealth [$]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,4)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5c-accu-persons-accu-money.pdf" ,bbox_inches="tight")
show()


