# synthetic-data-generator/synthetic_data.py

import numpy as np

# Generate synthetic data (e.g., for classification)
def generate_data(num_samples=1000, num_features=20, num_classes=2):
    X = np.random.randn(num_samples, num_features)
    y = np.random.randint(0, num_classes, num_samples)
    return X, y

# Example usage
X, y = generate_data()
print(X.shape, y.shape)
