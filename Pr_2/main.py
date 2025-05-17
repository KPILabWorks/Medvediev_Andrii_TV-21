import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fill_nan_custom(data):
    """
        Fills NaN values in a numeric list or series
        using the average of the nearest (left and right) neighbors.
    """
    data = data.copy()
    nan_indices = []

    for i in range(len(data)):
        if pd.isna(data[i]):
            nan_indices.append(i)
            left = right = None

            # Search for left neighbor
            for j in range(i - 1, -1, -1):
                if not pd.isna(data[j]):
                    left = data[j]
                    break

            # Search for right neighbor
            for j in range(i + 1, len(data)):
                if not pd.isna(data[j]):
                    right = data[j]
                    break

            # Calculate average
            if left is not None and right is not None:
                data[i] = (left + right) / 2
            elif left is not None:
                data[i] = left
            elif right is not None:
                data[i] = right
            else:
                data[i] = 0

    return data, nan_indices

# Data with missing values
original_data = pd.Series([1.0, np.nan, 3.0, np.nan, np.nan, 6.0, np.nan, 8.0])

# Fill missing values
filled_data, nan_indices = fill_nan_custom(original_data)

# Console output
print("Before filling:")
print(original_data)

print("\nAfter filling:")
print(filled_data)

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(original_data.index, filled_data, 'bo-', label='Filled values')
plt.plot(original_data.index, original_data, 'ro--', label='Original (with NaN)', alpha=0.4)

# Arrows and annotations
for idx in nan_indices:
    plt.annotate(f"{filled_data[idx]:.2f}",
                 (idx, filled_data[idx]),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center',
                 color='green',
                 fontsize=10,
                 arrowprops=dict(arrowstyle="->", color='green'))

plt.title("Filling Missing Values (NaN) Using Neighbor Average", fontsize=14)
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()