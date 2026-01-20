
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


