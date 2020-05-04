import matplotlib.pyplot as pyplot
import pandas as pandas

dataset = pandas.read_csv("data-science-blog-python-beispiel.txt", sep="|", header=0, encoding="utf8")

print(dataset)

# Pie Chart
var= dataset.groupby(['Funktion']).sum().stack()
temp = var.unstack()
type(temp)
x_list = temp['Mitarbeiter']
label_list = temp.index
pyplot.axis("equal") # Kreisdiagramm rund gestaltet (sonst Standard: oval!)
pyplot.pie(x_list, labels=label_list, autopct="%1.1f%%")
pyplot.title('Aufteilung alle Mitarbeiter auf die Standorte nach Funktion')
pyplot.show()


# Balkendiagramm
var = dataset.groupby('Funktion').Umsatz.sum()
fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Funktion')
ax.set_ylabel('Umsatz in Summe')
ax.set_title('Umsatzvolumen nach Funktion der Filialen')
var.plot(kind='bar')
pyplot.show()

# gestapelte Säulen
var = dataset.groupby(['Funktion', 'Standort']).Umsatz.sum()
var.unstack().plot(kind='bar', stacked=True, grid=True)
pyplot.legend(bbox_to_anchor=(1.09, 1), loc=0, borderaxespad=0.5)
pyplot.show()

# Histogramm
fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(dataset['Mitarbeiter'], bins=5, color='#9400D3')
pyplot.title('Mitarbeiter Verteilung')
pyplot.xlabel('Verteilung')
pyplot.ylabel('Anzahl Mitarbeiter')
pyplot.show()

#Line Chart
var = dataset.groupby('Standort').Umsatz.sum()
fig = pyplot.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Umsatz')
ax1.set_ylabel('Standort')
var.plot(kind='line')
pyplot.show()


# Kastengrafik
fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)
ax.boxplot(dataset['Mitarbeiter'])
pyplot.show()

# Punktverteilungsdiagramm (Scatter Plot)
fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(dataset["Mitarbeiter"], dataset["Umsatz"])
ax.set_xlabel('Anzahl Mitarbeiter')
ax.set_ylabel('Umsatz')
pyplot.show()


# Balkendiagramm
var = dataset.groupby('Kosten').Kosten.sum()
fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Funktion')
ax.set_ylabel('Umsatz in Summe')
ax.set_title('Umsatzvolumen nach Funktion der Filialen')
var.plot(kind='bar')
pyplot.show()

# Blasendiagramm (Bubble Chart)
fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(dataset['Kosten'], dataset['Umsatz'], s=dataset['Mitarbeiter'])
ax.set_xlabel('Umsatz')
ax.set_ylabel('Kosten')
pyplot.xscale('log')
pyplot.yscale('log')
pyplot.show()