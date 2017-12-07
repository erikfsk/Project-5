from matplotlib.pyplot import *
from numpy import * 


def c_ij(x,gamma):
	return x**gamma


x = linspace(1,0,1000)

for i in range(5):
	plot(x,c_ij(x,i),"-",linewidth=2,label="$\gamma$ = "+str(i))

xlabel("Ratio [$C_{ij}$ / $C_{ij}$ $_{max}}$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(1,0)
ylim(0,1.01)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("interactions.pdf" ,bbox_inches="tight")
clf()


def p_ij(x,alpha):
	alpha = 0.5*alpha 
	if x < 1: 
		return 1
	else:
		return x**-alpha
def p_ij_wrong(x,alpha):
	alpha = 0.5*alpha 
	return x**-alpha


x = linspace(0.01,10,1000)


colors = ["k","b","g","r","m"]
for i in range(4,-1,-1):
	y = [p_ij(j,i) for j in x]
	y2 = [p_ij_wrong(j,i) for j in x]
	plot(x,y2,"%s--"% colors[i])
	plot(x,y,"%s-"%colors[i],linewidth=2,label="$\\alpha$ = "+str(i*0.5))

xlabel("Ratio [$\Delta m_{ij}$]",fontsize=20)
ylabel("Probability [%]",fontsize=20)

xticks(fontsize=20)
yticks(fontsize=20)

xlim(0,5)
ylim(0,2)
grid("on")
tight_layout()
legend(loc="best",fontsize=20)
savefig("difference.pdf" ,bbox_inches="tight")
show()