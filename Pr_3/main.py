import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon

# 1. Generate data
np.random.seed(42)

# Normal distribution (e.g., average household energy consumption)
normal_data = np.random.normal(loc=50, scale=10, size=1000)

# Exponential distribution (e.g., energy spikes from appliance startups)
exp_data = np.random.exponential(scale=30, size=1000)

# 2. Visualization
plt.figure(figsize=(14, 6))

# ---- Histogram for Normal Distribution ----
plt.subplot(1, 2, 1)
count, bins, ignored = plt.hist(normal_data, bins=30, density=True, alpha=0.6, color='skyblue', label='Histogram')
plt.plot(bins, norm.pdf(bins, loc=50, scale=10), 'r-', label='Density Curve (Normal)')
plt.title("Normal Distribution of Energy Consumption")
plt.xlabel("Energy Consumption (kWh)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)

# ---- Histogram for Exponential Distribution ----
plt.subplot(1, 2, 2)
count, bins, ignored = plt.hist(exp_data, bins=30, density=True, alpha=0.6, color='lightgreen', label='Histogram')
plt.plot(bins, expon.pdf(bins, scale=30), 'm-', label='Density Curve (Exponential)')
plt.title("Exponential Distribution of Energy Consumption")
plt.xlabel("Energy Consumption (kWh)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# 3. Summary analysis
print("Distribution Analysis:\n")

print("Normal Distribution:")
print(f"  Mean: {np.mean(normal_data):.2f}")
print(f"  Standard Deviation: {np.std(normal_data):.2f}")

print("\nExponential Distribution:")
print(f"  Mean: {np.mean(exp_data):.2f}")
print(f"  Standard Deviation: {np.std(exp_data):.2f}")
