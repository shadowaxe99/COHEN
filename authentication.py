```python
import hashlib

def authenticate(username, password):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username and hashed password match the stored credentials
    if username == "admin" and hashed_password == "c4ca4238a0b923820dcc509a6f75849b":
        return True
    else:
        return False
```
