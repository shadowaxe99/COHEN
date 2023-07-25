```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_returns(prices):
    returns = prices.pct_change()
    return returns

def calculate_cumulative_returns(returns):
    cumulative_returns = (returns + 1).cumprod() - 1
    return cumulative_returns

def calculate_annualized_returns(returns):
    annualized_returns = returns.mean() * 252
    return annualized_returns

def calculate_volatility(returns):
    volatility = returns.std() * np.sqrt(252)
    return volatility

def calculate_sharpe_ratio(returns, risk_free_rate):
    excess_returns = returns - risk_free_rate
    sharpe_ratio = excess_returns.mean() / excess_returns.std() * np.sqrt(252)
    return sharpe_ratio

def calculate_drawdown(prices):
    cumulative_returns = calculate_cumulative_returns(calculate_returns(prices))
    peak = prices.cummax()
    drawdown = (prices - peak) / peak
    return drawdown

def plot_performance(prices, benchmark=None):
    cumulative_returns = calculate_cumulative_returns(calculate_returns(prices))
    plt.plot(cumulative_returns, label='Strategy')
    if benchmark is not None:
        benchmark_cumulative_returns = calculate_cumulative_returns(calculate_returns(benchmark))
        plt.plot(benchmark_cumulative_returns, label='Benchmark')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.show()
```
