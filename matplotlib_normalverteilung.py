# Module importieren
import numpy as np
import matplotlib.pyplot as plt
# Diagramm im Stil 'seaborn plotten'
plt.style.use('seaborn')

# Zufallswerte normieren
np.random.seed(1)
 
# Erwartungswert und Standardabweichung definieren
mu, sigma = 170, 8
 
# Normalverteilte Zufallswerte generieren
x = mu + sigma * np.random.randn(10000)
 
# Histogramm zeichnen
plt.hist(x, 100, normed=True, alpha=0.75)

# Sichbaren Bereich festlegen
plt.axis([140, 200, 0, 0.06])
 
# Beschriftungen setzen
plt.xlabel('Körpergröße')
plt.ylabel('Wahrscheinlichkeit')
plt.title('Normalverteilung von Körpergrößen')
plt.text(150, 0.05, r'$\mu=170,\ \sigma=8$')
 
# Bild anzeigen
plt.show()
