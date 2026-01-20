
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ---------- Task 5.1 ----------
fs = 500            # Sampling frequency (Hz)
f = 10              # Signal frequency (Hz)
A = 5               # Amplitude
t = np.arange(0, 1, 1/fs)   # Time from 0–1 sec

signal = A * np.sin(2 * np.pi * f * t)

plt.figure()
plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("10 Hz Sinusoidal Signal")
plt.show()

# ---------- Task 5.2 ----------
noise = 0.25 * np.random.randn(500)
noisy_signal = signal + noise

plt.figure()
plt.plot(t, signal, label="Clean Signal")
plt.plot(t, noisy_signal, label="Noisy Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Signal with Noise")
plt.legend()
plt.savefig("Task4_2.png")
plt.show()

# ---------- Task 5.3 ----------#

time_minutes = np.arange(0, 120)  # 120 minutes
temperature = 36 + np.random.uniform(-0.5, 0.5, 120)

data = {
    "Time (s)": time_minutes * 60,
    "Temperature (°C)": temperature
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sensor_readings.csv", index=False)

print("sensor_readings.csv created successfully!")




