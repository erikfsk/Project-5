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
	label_text += "   $\\alpha = $" + str(5 + 5*(int(txtfile[-5:-4])**2))
	if "00" in txtfile:
		print sum(data["Y"][:len(data["Y"])/10])
		if 0 == int(txtfile[-5:-4]):
			loglog(data["X"],data["Y"]*100,"k-",label=label_text)
		elif 1 == int(txtfile[-5:-4]):
			loglog(data["X"],data["Y"]*100,"b-",label=label_text)
		elif 2 == int(txtfile[-5:-4]):
			loglog(data["X"],data["Y"]*100,"g-",label=label_text)
		elif 3 == int(txtfile[-5:-4]):
			loglog(data["X"],data["Y"]*100,"r-",label=label_text)

xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("5d-00-log.pdf" ,bbox_inches="tight")
show()














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
show()