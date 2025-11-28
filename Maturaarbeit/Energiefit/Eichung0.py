import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Gauss-Funktion
def func(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

# Pfad zur .Spe Datei
dateipfad = "22Na_Kalibration - Edit.Spe"

# Bereich wählen: z.B. startzeile = 10, endzeile = 50
startzeile = 540  # erste Zeile = 1
endzeile = 680  # letzte Zeile, inclusive

y_values = []
x_values = []

with open(dateipfad, 'r') as f:
    for i, line in enumerate(f, start=1):
        if i < startzeile or i > endzeile:
            continue  # außerhalb des gewählten Bereichs
        line = line.strip()
        if not line:
            continue  # leere Zeilen überspringen
        # jede Zahl in der Zeile als separaten Punkt
        for val in line.split():
            y_values.append(float(val))
            x_values.append(i)  # Zeilennummer als x-Koordinate

x = np.array(x_values, dtype=float)
y = np.array(y_values, dtype=float)

# Startwerte für den Fit
p0 = [np.max(y), x[np.argmax(y)], len(x)/5]

popt, _ = curve_fit(func, x, y, p0=p0)
ym = func(x, *popt)

# Plot
plt.plot(x, y, label='Messwerte (.Spe Datei)')
plt.plot(x, ym, label='Gefittete Gauss-Funktion')
plt.scatter(x, y, s=10)
plt.xlabel('x (Elektrischer Impuls)')
plt.ylabel('y (Counts)')
plt.title(f'Gaussian Fit der Messwerte (Zeilen {startzeile}-{endzeile})')
plt.legend()
plt.show()

print("Fit-Parameter (Amplitude, Zentrum, Sigma):", popt)


