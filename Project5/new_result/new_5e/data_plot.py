# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from data_dict import *
import re
import os

output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)


for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_plot("1","00",data,txtfile,label_text)
make_plot("5e-1-00.pdf")

for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_semi("1","00",data,txtfile,label_text)
make_plot("5e-1-00-log.pdf")





for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_plot("1","50",data,txtfile,label_text)
make_plot("5e-1-50.pdf")

for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_semi("1","50",data,txtfile,label_text)
make_plot("5e-1-50-log.pdf")





for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_plot("1","90",data,txtfile,label_text)
make_plot("5e-1-90.pdf")

for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_semi("1","90",data,txtfile,label_text)
make_plot("5e-1-90-log.pdf")





for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_plot("2","00",data,txtfile,label_text)
make_plot("5e-2-00.pdf")

for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_semi("2","00",data,txtfile,label_text)
make_plot("5e-2-00-log.pdf")





for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_plot("2","50",data,txtfile,label_text)
make_plot("5e-2-50.pdf")

for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_semi("2","50",data,txtfile,label_text)
make_plot("5e-2-50-log.pdf")





for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_plot("2","90",data,txtfile,label_text)
make_plot("5e-2-90.pdf")

for txtfile in txtfiles:
	data = data_dict(txtfile)
	label_text = label_(txtfile)
	plot_semi("2","90",data,txtfile,label_text)
make_plot("5e-2-90-log.pdf")