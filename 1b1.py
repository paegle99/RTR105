
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

#print(vars())

from numpy import sin

#print(vars())

from numpy import cos, linspace
#print(vars())

#x = linspace(0, 7, 70) #solis = (7-0)/(70-1)
x = linspace(0, 4, 11) #solis = (4-0)/(11-1)
y = cos(x)
y1 = sin(x)
#print(vars())


from matplotlib import pyplot as plt


plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$ UN $sin(x)$')
plt.plot(x, y, color = "#FF0000")
plt.plot(x, y1, color = '#FFFF00')
#plt.show()
plt.plot(x, y, 'bo')
plt.plot(x, y1, 'go')
plt.legend(['$cos(x)$' '$sin(x)$' '$cos(x)$', 'sin(x)'])
plt.show()
