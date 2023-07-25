```python
import numpy as np

def monte_carlo_simulation(returns, num_simulations, num_periods):
    """
    Perform Monte Carlo simulation to model potential outcomes and assess the probability of loss.
    
    Parameters:
    - returns (np.ndarray): Array of historical returns.
    - num_simulations (int): Number of simulations to run.
    - num_periods (int): Number of periods to simulate.
    
    Returns:
    - np.ndarray: Array of simulated portfolio values for each simulation.
    """
    portfolio_values = np.zeros((num_simulations, num_periods))
    portfolio_values[:, 0] = 1.0
    
    for i in range(num_simulations):
        for j in range(1, num_periods):
            random_returns = np.random.choice(returns, size=num_periods-1)
            portfolio_values[i, j] = portfolio_values[i, j-1] * (1 + random_returns[j-1])
    
    return portfolio_values
```
This code defines a function `monte_carlo_simulation` that performs Monte Carlo simulation to model potential outcomes and assess the probability of loss. It takes in an array of historical returns, the number of simulations to run, and the number of periods to simulate. It returns an array of simulated portfolio values for each simulation.

The function initializes an array `portfolio_values` with zeros and sets the initial portfolio value to 1.0 for each simulation. It then iterates over each simulation and period, generating random returns from the historical returns array and updating the portfolio values accordingly.

Note: The code assumes that the `returns` array contains the historical returns for each period. You may need to modify the code to fit your specific data structure and requirements.