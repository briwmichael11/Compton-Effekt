import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Definiere die Gauß-Funktion (3 Parameter: Amplitude a, Zentrum x0, Breite sigma)
def func(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

# Erzeuge x-Werte: 100 Punkte gleichmäßig zwischen 0 und 10
x = np.linspace(0, 10, 100)

# Berechne die "wahre" Gauß-Kurve (Amplitude=1, Zentrum=5, Breite=2)
y = func(x, 1, 5, 2)

# Füge Rauschen hinzu, um Messdaten zu simulieren
yn = y + 0.2 * np.random.normal(size=len(x))

# Curve Fitting: finde optimale Parameter (a, x0, sigma) für die verrauschten Daten
popt, _ = curve_fit(func, x, yn)

# Berechne die Kurve mit den gefitteten Parametern
ym = func(x, *popt)

# Darstellung:
plt.plot(x, y, label='Original')      # theoretische, "wahre" Kurve
plt.scatter(x, yn, label='Noisy')     # verrauschte Messpunkte
plt.plot(x, ym, label='Fitted')       # Fit-Kurve
plt.legend()
plt.show()

# Ausgabe der gefitteten Parameter
print("Fit Parameter:", popt)
