```python
import pandas as pd
import numpy as np

class DataCollectionStorage:
    def __init__(self):
        self.data = pd.DataFrame()

    def collect_data(self, source):
        # Code to collect financial data from the specified source
        # and store it in the data attribute
        pass

    def preprocess_data(self):
        # Code to handle missing values, normalize data, and remove outliers
        pass

    def get_data(self):
        return self.data
```
