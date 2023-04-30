import numpy as np
import matplotlib.pyplot as plt


my_numpy1 = np.linspace(0,15,20)
my_numpy2 = my_numpy1 ** 3
plt.plot(my_numpy1,my_numpy2,"g*-")
#plt.show()


my_figure2 = plt.figure()


my_axes3 = my_figure2.add_axes([0.1,0.1,0.9,0.9])
my_axes3.plot(my_numpy1,my_numpy2,"r*-")
my_axes3.set_xlabel("X Data Large")
my_axes3.set_ylabel("Y Data Large")
my_axes3.set_title("Large Graph")

my_axes2 = my_figure2.add_axes([0.25,0.4,0.3,0.3])
my_axes2.plot(my_numpy1,my_numpy2,"g*")
my_axes2.set_xlabel("X Data Small")
my_axes2.set_ylabel("Y Data Small")
my_axes2.set_title("Small Graph")
