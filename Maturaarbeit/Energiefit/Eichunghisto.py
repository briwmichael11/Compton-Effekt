import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Gauss-Funktion
def func(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

# Pfad zur .Spe Datei
dateipfad = "22Na_Kalibration - Edit.Spe"

# Bereich wählen: Start- und Endzeile
startzeile = 1  # erste Zeile = 1
endzeile = 4000  # letzte Zeile, inklusive

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

# Curve-Fit
popt, _ = curve_fit(func, x, y, p0=p0)
ym = func(x, *popt)

# ---------- Plot als Säulen ----------
plt.figure(figsize=(10,5))
plt.bar(x, y, width=0.8, color='skyblue', edgecolor='blue', label='Counts')
plt.xlabel('Mark')
plt.ylabel('Counts')
plt.title(f'Histogramm der Messwerte (marks {startzeile}-{endzeile})')
plt.legend()
plt.tight_layout()
plt.show()

# Fit-Parameter ausgeben
print("Fit-Parameter (Amplitude, Zentrum, Sigma):", popt)

# ---------- Alle y-Werte im gewählten Zeilenbereich summieren ----------
n = np.sum(y)
print("n(",startzeile,"-",endzeile,")=",n)

#Berechnung Fehler m
#Berechnung Fehler
s=popt[2]
m=s/(n**0.5)
print("m=",m)
