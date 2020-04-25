# parabel
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# Wertereihen erzeugen:
x = np.arange(-3, 11, 0.01)
y = x ** 2 - 8 * x - 15
y1 = 2 * x - 8


# Funktion plotten:
plt.plot(x, y)
plt.plot(x, y1)

# Layout anpassen:
plt.axis([-3, 11, -35, 35])
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid(True)
plt.text(-2, 15, "$f(x)=x^2 - 8x - 15$")
plt.text(3, -5, "$f(x)=2x - 8$")
plt.show()
