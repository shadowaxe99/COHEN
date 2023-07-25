```python
import pandas as pd
import numpy as np

def handle_missing_values(data):
    # Handle missing values by filling them with the mean of the column
    data.fillna(data.mean(), inplace=True)
    return data

def normalize_data(data):
    # Normalize data using z-score normalization
    data = (data - data.mean()) / data.std()
    return data

def remove_outliers(data, threshold=3):
    # Remove outliers using z-score method
    z_scores = np.abs((data - data.mean()) / data.std())
    data = data[z_scores < threshold]
    return data

# Example usage
data = pd.DataFrame({'A': [1, 2, np.nan, 4, 5],
                     'B': [6, 7, 8, 9, 10],
                     'C': [11, 12, 13, 14, 15]})

data = handle_missing_values(data)
data = normalize_data(data)
data = remove_outliers(data)
print(data)
```
