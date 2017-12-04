# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from data_dict import *
import re
import os

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = "$\\alpha = $" + txtfile[0:1]
	label_text += "   $\lambda = $" + str(float(txtfile[-7:-6])/10)
	label_text += "   $\gamma = $" + txtfile[-5:-4]
	plot(data["X"],data["Y"]*100,"-",label=label_text)


xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,10)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("test.pdf" ,bbox_inches="tight")
show()





