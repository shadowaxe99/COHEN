# alerting_notifications.py

"""
This module implements the alerting and notification mechanisms of the automated trading system.
It is responsible for informing users of significant events or changes in performance metrics.

"""

def send_alert(message):
    """
    Sends an alert to the user with the specified message.
    
    Parameters:
    - message (str): The message to be sent in the alert.
    
    Returns:
    - None
    """
    # Code to send the alert to the user
    print(f"ALERT: {message}")

def send_notification(message):
    """
    Sends a notification to the user with the specified message.
    
    Parameters:
    - message (str): The message to be sent in the notification.
    
    Returns:
    - None
    """
    # Code to send the notification to the user
    print(f"NOTIFICATION: {message}")

# Example usage
send_alert("Market volatility exceeded threshold")
send_notification("New trade executed successfully")