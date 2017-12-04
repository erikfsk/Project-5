# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from data_dict import *
import re
import os

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)


for txtfile in txtfiles:
	data = data_dict(txtfile)
	plot(data["X"],data["Y"]*100,"o",label="$\lambda$ = " + txtfile[:-4])


xlabel("Wealth [$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,3)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("test.pdf" ,bbox_inches="tight")
show()





