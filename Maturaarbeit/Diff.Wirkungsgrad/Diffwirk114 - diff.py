import math

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# --- Gauss-Funktion für den Fit ---
def func(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

# --- Lineare Transformation für X-Werte ---
a_lin = 0.8919940215753929
b_lin = -31.934619491620538

def transform_x(x):
    return a_lin * x + b_lin

def inverse_transform_x(x_trans):
    return (x_trans - b_lin) / a_lin

# --- Pfade zu den Dateien ---
datei_haupt = "114_diff.Wirkungsgrad - Edit.Spe"      # Hauptdatei (wird gefittet)
datei_zusatz = "114_diff.Wirkungsgrad_ohneTarget2 - Edit.Spe"    # Zweite Datei (nur Darstellung)

# --- Bereich wählen ---
startzeile = 260
endzeile = 300

# ---------- Hauptdatei einlesen ----------
y_main, x_orig_main, x_fit_main = [], [], []

with open(datei_haupt, 'r') as f:
    for i, line in enumerate(f, start=1):
        if i < startzeile or i > endzeile:
            continue
        line = line.strip()
        if not line:
            continue
        for val in line.split():
            y_main.append(float(val))
            x_orig_main.append(i)
            x_fit_main.append(transform_x(i))

x_orig_main = np.array(x_orig_main, dtype=float)
x_fit_main = np.array(x_fit_main, dtype=float)
y_main = np.array(y_main, dtype=float)

# ---------- Zusatzdatei einlesen (nur für Darstellung) ----------
y_add, x_orig_add = [], []

with open(datei_zusatz, 'r') as f:
    for i, line in enumerate(f, start=1):
        if i < startzeile or i > endzeile:
            continue
        line = line.strip()
        if not line:
            continue
        for val in line.split():
            y_add.append(float(val))
            x_orig_add.append(i)

x_orig_add = np.array(x_orig_add, dtype=float)
y_add = np.array(y_add, dtype=float)

# ---------- Fit nur für Hauptdatei ----------
p0 = [np.max(y_main), x_fit_main[np.argmax(y_main)], (np.max(x_fit_main) - np.min(x_fit_main)) / 5]
popt, _ = curve_fit(func, x_fit_main, y_main, p0=p0)
a_fit, x0_fit, sigma_fit = popt
x0_original_scale = inverse_transform_x(x0_fit)
ym = func(x_fit_main, *popt)

# ---------- Alle y-Werte im gewählten Zeilenbereich summieren ----------
n = np.sum(y_main)

# ---------- Plot ----------
plt.figure(figsize=(10,5))

# Hauptdaten (blau)
plt.bar(x_orig_main, y_main, width=0.8, color='skyblue', edgecolor='blue', linewidth=1, label='Messwerte mit Target (counts)')

# Zusatzdaten (rot, leicht transparent, überlagert)
plt.bar(x_orig_add, y_add, width=0.8, color='red', edgecolor='darkred', linewidth=1, alpha=0.6, label='Messwerte ohne Target (counts)')

# Gauss-Fit-Kurve
plt.plot(x_orig_main, ym, color='orange', linewidth=2.5, label='Gefittete Gaussfunktion')

# Achsen, Titel etc.
plt.xlabel('Mark')
plt.ylabel('Counts')
plt.title(f'Gaussfunktion (mark {startzeile}-{endzeile})\nMit und ohne Target')
plt.legend()
plt.tight_layout()
plt.show()

# ---------- Ausgabe ----------
print("Fit-Parameter (basierend auf transformierter X-Achse):")
print(f"Amplitude (a)         = {a_fit}")
print(f"Zentrum (x0\')         = {x0_fit}  (transformiert)")
print(f"Zentrum (Zeile)       = {x0_original_scale}  (entspricht ursprünglicher Zeilennummer)")
print(f"Sigma                 = {sigma_fit}")
print("n(",startzeile,"-",endzeile,")=",n)

#Berechnung Fehler
m=sigma_fit/(n**0.5)
print("m=",m)

#Berechnung Sollwert
c=299792458
me=9.109*10**(-31)
E=662
EJ=(1.60218*10**(-16))*E
phi=math.radians(120)
print("phi=",phi)

Eq=EJ/(1+(EJ/(me*c**2))*(1-math.cos(phi)))
Eg=(6.242*10**(15))*Eq
print("Sollwert=", Eg, "keV")

#Berechnung differentieller Wirkungsquerschnitt
time = 3550.58
Rgamma = 19.807047486892024
Rgestreut = (n/time)
print("Rgestreut=",Rgestreut)
M = 0.029982 #kg/mol
Avogadro = 6.02214076 * 10**(23)
d = 0.00295 #m
Z = 13
rho = 2700 #kg/m^3
Ohm = (math.pi*11.5**2)/(283**2)
print("Raumwinkel", Ohm)
Ohmgrad = Ohm*(180/math.pi)
print("Ohmgrad=",Ohmgrad)
Diffwirk= (Rgestreut * M)/(Rgamma*Z*d*Avogadro*rho*Ohm)
print("Totaler Wirkungsgrad=",Diffwirk)

#Theoretischer Wert
kappa = Eg/662
re= 2.8179403205 * (10**(-15))
Theodiffwirk= ((re**2)/2)*((kappa)-(kappa**2*math.sin(phi))+(kappa**3))
print("Theodiffwirk=",Theodiffwirk)