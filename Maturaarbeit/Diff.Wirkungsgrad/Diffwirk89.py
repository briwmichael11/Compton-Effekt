import math

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Gauss-Funktion für den Fit
def func(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

# Lineare Umrechnungsfunktion für X-Werte (Zeilennummern)
a_lin = 0.8919940215753929
b_lin = -31.934619491620538

def transform_x(x):
    return a_lin * x + b_lin

def inverse_transform_x(x_trans):
    return (x_trans - b_lin) / a_lin

# Pfad zur .Spe Datei
dateipfad = "89_diff.Wirkungsgrad - Edit.Spe"

# Bereich wählen: Start- und Endzeile
startzeile = 300  # erste Zeile = 1
endzeile = 370 # letzte Zeile, inklusive

y_values = []
x_original = []  # Originale Zeilennummern für Plot
x_transformed = []  # Transformierte Werte für Fit

with open(dateipfad, 'r') as f:
    for i, line in enumerate(f, start=1):
        if i < startzeile or i > endzeile:
            continue
        line = line.strip()
        if not line:
            continue
        for val in line.split():
            y_values.append(float(val))
            x_original.append(i)  # Unveränderte Zeilennummer für Anzeige
            x_transformed.append(transform_x(i))  # Transformiert für Fit

x_orig = np.array(x_original, dtype=float)
x_fit = np.array(x_transformed, dtype=float)
y = np.array(y_values, dtype=float)

# Startwerte für den Fit
p0 = [np.max(y), x_fit[np.argmax(y)], (np.max(x_fit) - np.min(x_fit)) / 5]

# Curve-Fit mit transformierten X-Werten
popt, _ = curve_fit(func, x_fit, y, p0=p0)
a_fit, x0_fit, sigma_fit = popt

# Zentrum zurückrechnen auf ursprüngliche Zeilennummer
x0_original_scale = inverse_transform_x(x0_fit)

# Fitkurve erzeugen (auf transformierter Basis, aber für Original x anzeigen)
ym = func(x_fit, *popt)

# ---------- Alle y-Werte im gewählten Zeilenbereich summieren ----------
n = np.sum(y)

# ---------- Plot mit originalen Zeilennummern ----------
plt.figure(figsize=(10,5))
plt.bar(x_orig, y, width=0.8, color='skyblue', edgecolor='black', linewidth=0.8, label='Messwerte (counts)')
plt.plot(x_orig, ym, color='orange', linewidth=2, label='Gefittete Gaussfunktion')
plt.xlabel('Mark')
plt.ylabel('Counts')
plt.title(f'Gaussfunktion der Messwerte (mark {startzeile}-{endzeile})')
plt.legend()
plt.tight_layout()
plt.show()

# Fit-Parameter ausgeben
print("Fit-Parameter (basierend auf transformierter X-Achse):")
print(f"Amplitude (a)     = {a_fit} (counts)")
print(f"Zentrum (x0')     = {x0_fit}  (in keV)")
print(f"Zentrum (Zeile)   = {x0_original_scale}  (Stärke Elektrischer Impuls)")
print(f"Sigma             = {sigma_fit}")
print("n(",startzeile,"-",endzeile,")=",n)

#Berechnung Fehler
m=sigma_fit/(n**0.5)
print("m=",m)

#Berechnung Sollwert
c=299792458
me=9.109*10**(-31)
E=662
EJ=(1.60218*10**(-16))*E
phi=math.radians(95)

Eq=EJ/(1+(EJ/(me*c**2))*(1-math.cos(phi)))
Eg=(6.242*10**(15))*Eq
print("Sollwert=", Eg, "keV")

#Berechnung differentieller Wirkungsquerschnitt
time = 19392.00
Rgamma = 19.807047486892024
Rgestreut = (n/time)
print("Rgestreut=",Rgestreut)
M = 0.029982 #kg/mol
Avogadro = 6.02214076 * 10**(23)
d = 0.00295
Z = 13
rho = 2700 #kg/m^3
Ohm = (math.pi*11.5**2)/(283**2)
print("Raumwinkel", Ohm)
Ohmgrad = Ohm*(180/math.pi)
print("Ohmgrad=",Ohmgrad)
Diffwirk= (Rgestreut * M)/(Rgamma*Z*d*Avogadro*rho*Ohm)
print("Differentieller Wirkungsgrad=",Diffwirk)

#Theoretischer Wert
kappa = Eg/662
re= 2.8179403205 * (10**(-15))
Theodiffwirk= ((re**2)/2)*((kappa)-(kappa**2*math.sin(phi))+(kappa**3))
print("Theodiffwirk=",Theodiffwirk)