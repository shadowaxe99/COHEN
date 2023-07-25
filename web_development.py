```python
# web_development.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get user input from the form
    user_input = request.form['user_input']
    
    # Process user input and perform necessary actions
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
```
Note: This code assumes that you have HTML templates named 'index.html' and 'result.html' in the same directory as the 'web_development.py' file. You can modify the code to match your specific HTML templates and logic.