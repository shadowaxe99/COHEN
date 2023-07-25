```python
import requests

def api_integration():
    # Function to integrate with APIs and collect financial data
    
    # API endpoint and parameters
    endpoint = "https://api.example.com/financial-data"
    params = {
        "symbol": "AAPL",
        "interval": "daily",
        "start_date": "2022-01-01",
        "end_date": "2022-12-31"
    }
    
    try:
        # Send GET request to API
        response = requests.get(endpoint, params=params)
        
        # Check if request was successful
        if response.status_code == 200:
            # Process the response data
            data = response.json()
            
            # Perform further data processing or store the data
            
            # Return success message
            return "API integration successful"
        else:
            # Return error message
            return f"API integration failed with status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        # Return error message
        return f"API integration failed: {str(e)}"
```
This code snippet demonstrates the implementation of API integration for collecting financial data. It uses the `requests` library to send a GET request to the API endpoint with the specified parameters. The response is then processed and further data processing or storage can be performed. The function returns a success message if the API integration is successful, or an error message if it fails.