import matplotlib.pyplot as plt
import numpy as np

# ===== Punkte definieren =====
x1, y1 = 608.67517759, 511  # Punkt P
x2, y2 = 1465.18316029, 1275   # Punkt Q

# ===== Sichtbarer Bereich (Koordinatensystem-Ausschnitt) =====
x_min, x_max = 0, 1600   # Bereich der x-Achse
y_min, y_max = 0, 1400    # Bereich der y-Achse

# ===== Gerade berechnen =====
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1

# ===== Gerade zeichnen =====
x_values = np.linspace(x_min, x_max, 200)
y_values = m * x_values + b

# ===== Plot erstellen =====
plt.figure(figsize=(7, 5))
plt.plot(x_values, y_values, color='orange', label='Eichgerade')
plt.scatter([x1, x2], [y1, y2], color='blue', marker='x', s=100, label='Punkte')

# ===== Punkte beschriften =====
plt.text(x1 + 50, y1 - 75, f'P({x1}, {y1})', color='black', fontsize=12)
plt.text(x2 + 50, y2 - 75, f'Q({x2}, {y2})', color='black', fontsize=12)

# ===== Achsen, Titel, Bereich =====
plt.xlabel("mark")
plt.ylabel("Energie in keV")
plt.title("Eichgerade durch die Punkte P und Q")
plt.legend()
plt.grid(True)

# Sichtbarer Bereich
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.axis('equal')

plt.show()

