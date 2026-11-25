import numpy as np
import matplotlib.pyplot as plt

LH = []
Lt = []

g = 10
H = 2.28
r_tangki = 1.44/2
r_lubang = 0.048/2
A_tangki = np.pi*r_tangki**2
A_lubang = np.pi*(r_lubang)**2
v = np.sqrt(2*g*H)

h = 0.1
t = 0

dh_dt = -A_lubang/A_tangki*v
H = H + dh_dt*h/2

while t <= 10:
    print(f"Waktu: {t:.1f} s, Ketinggian air: {H:.4f} m")
    LH.append(H)
    Lt.append(t)
    dh_dt = -A_lubang/A_tangki*v
    H = H + dh_dt*h/2
    t += h

plt.plot(Lt, LH, "b", label="Ketinggian air terhadap waktu")
plt.xlabel("Waktu (s)")
plt.ylabel("Ketinggian Air (m)")
plt.title("Dinamika Ketinggian Air dalam Tangki")
plt.legend()
plt.grid(True)
plt.show()