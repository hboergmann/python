import sympy as sy
# Funktionsgleichung als String einlesen:
print("Beispiel 3*x**2 - 5*x +7):")
parable_function_input = input("Bitte die Funktionsgleichung einer Parabel eingeben: ")

# Eingelesenen String in Sympy-Ausdruck umwandeln:
parable_function = sy.S(parable_function_input)

# Orientierung der Parabel bestimmen:
if parable_function.coeff(x, n=2) > 0:
    orientation = "up"
else:
    orientation  = "down"

# Erste und zweite Ableitung bilden:
parable_function_diff_1 = sy.diff(parable_function, x, 1)
parable_function_diff_2 = sy.diff(parable_function, x, 2)

# Extremstelle bestimmen (liefert Liste an Ergebnissen):
extremes = sy.solve(sy.Eq(parable_function_diff_1, 0))

# Der gesuchte x_0-Wert ist der einzige Eintrag der Ergebnisliste:
x_0 = extremes[0]

# Zugehörigen Funktionswert bestimmen:
y_0 = parable_function.subs(x, x_0)

print("Die Orientierung der Parabel ist \"%s\", ihr Scheitel liegt bei \
     (% .2 f, % .2 f). " % (orientation, x_0, y_0) )
