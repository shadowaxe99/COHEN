```python
import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Automated Trading System!"

if __name__ == '__main__':
    app.run()
```