import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)  # 1000 random numbers
plt.figure(figsize=(6,4))
plt.hist(data, bins=20, color='purple', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()