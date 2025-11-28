import math

import numpy as np
import matplotlib.pyplot as plt

#Berechnung Sollwert
c=299792458
me=9.109*10**(-31)
E=662
EJ=(1.60218*10**(-16))*E
phi=math.radians(20)


def f(x):
    EJ / (1 + (EJ / (me * c ** 2)) * (1 - math.cos(x)))
    return np.EJ / (1 + (EJ / (me * c ** 2)) * (1 - math.cos(x)))

# ---- Bereich der Funktion ----
x_values = np.linspace(0, 10, 400)
y_values = f(x_values)

# ---- Punkte eintragen (7 Punkte) ----
# Beispielpunkte – diese kannst du anpassen
points_x = [ -8, -3, -1, 0, 2, 5, 7 ]
points_y = [ 678.0, 655.0 , 614.0, 481.0, 336.0, 268.0, 216.0 ]  # y-Werte automatisch aus der Funktion

# ---- Plot erstellen ----
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="f(x)", linewidth=2)

# Punkte einzeichnen
plt.scatter(points_x, points_y, color="red", s=50, label="Punkte")

# Achsen & Raster
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.5)

plt.title("Funktion mit 7 eingezeichneten Punkten")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
