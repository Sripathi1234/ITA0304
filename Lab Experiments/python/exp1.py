import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(0.1, 5, 100)              # distance in km
f = 900                                   # frequency in MHz
fspl = 20*np.log10(d) + 20*np.log10(f) + 32.44   # free-space path loss (dB)
pr = 30 - fspl                            # transmit power 30 dBm

plt.plot(d, pr)
plt.xlabel("Distance (km)"); plt.ylabel("Received power (dBm)")
plt.title("Free-space path loss at 900 MHz"); plt.grid(True); plt.show()
print("Received power at 0.1 km :", round(pr[0], 2), "dBm")
print("Received power at 5 km   :", round(pr[-1], 2), "dBm")

