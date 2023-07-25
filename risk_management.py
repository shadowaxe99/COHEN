```python
# risk_management.py

import numpy as np

def calculate_stop_loss(price, risk_percentage):
    stop_loss = price - (price * risk_percentage)
    return stop_loss

def calculate_position_size(account_balance, risk_percentage, stop_loss):
    position_size = (account_balance * risk_percentage) / stop_loss
    return position_size

def apply_risk_management(trade_price, risk_percentage, account_balance):
    stop_loss = calculate_stop_loss(trade_price, risk_percentage)
    position_size = calculate_position_size(account_balance, risk_percentage, stop_loss)
    return stop_loss, position_size
```
