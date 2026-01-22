import numpy as np
import matplotlib.pyplot as plt

# Deine Punkte
x = np.array([608.67517759, 795.8771895423947, 1465.18316029])
y = np.array([511, 662, 1275])

# Lineare Regression (Berechnung)
x_mean = np.mean(x)
y_mean = np.mean(y)

m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
b = y_mean - m * x_mean

# Geradengleichung in der Konsole ausgeben
print(f"Geradengleichung: y = {m:.6f}x  {b:.6f}")

# Gerade für das Diagramm
x_line = np.linspace(min(x)-50, max(x)+50, 100)
y_line = m * x_line + b

# Plot
plt.figure(figsize=(8, 6))

# Punkte (blau, +)
plt.scatter(x, y, color="blue", marker="+", s=100, label="Messpunkte")

# Gerade (orange)
plt.plot(x_line, y_line, color="orange", label="Lineare Regression")

# Koordinaten-Beschriftung
for i in range(len(x)):
    label = f"({x[i]}, {y[i]:.2f})"
    plt.text(x[i] + 10, y[i] + 10, label, fontsize=10)

# Achsen & Titel
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lineare Regression mit Koordinatenbeschriftung")
plt.legend()
plt.grid(True)

plt.show()
