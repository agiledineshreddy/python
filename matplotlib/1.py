import matplotlib.pyplot as plt

import numpy as np
x=[2,3,455]
y=[22,45,6]
plt.plot(x,y,marker="s",mec="r",mfc="g",ms="3") 
# mec-marker edge color
# mfc- marker face color
# ms- marker size
plt.title("first")
plt.xlabel("x-axis")
plt.show()

a=np.arange(0,10,2)
b=(a**2)    
plt.plot(a,b,marker="o",mfc="g",ls="dotted",c="r",lw="5")
# ls-line style("dotted","solid","dashed","dasheddot","none")
# lw- line width
# c-color of line
plt.title("first")
plt.xlabel("x-axis")
plt.show()