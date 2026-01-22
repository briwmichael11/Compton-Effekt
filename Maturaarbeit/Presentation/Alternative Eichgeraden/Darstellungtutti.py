import numpy as np
import matplotlib.pyplot as plt

# Sichtbaren Bereich anpassen
x_min, x_max = 500, 1600
y_min, y_max = 450, 1350

x = np.linspace(x_min, x_max, 500)

# Farben festlegen
farben_geraden = ["blue", "green", "red", "yellow", "magenta", "cyan"]
farbe_punkte = "black"

# Geraden (m, b, Label)
geraden = [
    (0.8919940215753929, -31.934619491620538, "Original"),
    (0.8919940215753929, -26.934619491620538, "v1"),
    (0.8919940215753929, -36.93461949162054, "v2"),
    (0.903669335993919, -44.04109356873596, "v3"),
    (0.8803187071568668, -19.828145414505116, "v4"),
    (0.898328, -43.320829, "lin. Reg.")
]

# Geraden plotten
for (m, b, label), farbe in zip(geraden, farben_geraden):
    y = m * x + b
    plt.plot(x, y, color=farbe, label=label, zorder=1)

# Punkte
punkte = {
    "A": (608.67517759, 511),
    "B": (795.8771895423947, 662),
    "C": (1465.18316029, 1275)
}

# Punkte mit + Zeichen, groß & im Vordergrund
for name, (px, py) in punkte.items():
    plt.scatter(px, py, marker="+", s=200, color=farbe_punkte, zorder=5)
    plt.text(px + 15, py - 30, f"{name}({round(px,1)}|{py})", fontsize=10, zorder=6)

# Achsenbereich
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# Layout
plt.grid(True)
plt.legend()
plt.title("Eichgeraden und Punkte A, B, C")
plt.xlabel("Mark")
plt.ylabel("keV")

plt.show()
