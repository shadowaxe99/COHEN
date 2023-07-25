```python
import matplotlib.pyplot as plt
import pandas as pd

def plot_data(data, x_label, y_label, title):
    plt.plot(data[x_label], data[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def generate_visualization(data):
    # Example usage
    plot_data(data, 'Date', 'Price', 'Stock Price Over Time')

# Example data
data = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                     'Price': [100, 120, 110]})

generate_visualization(data)
```
