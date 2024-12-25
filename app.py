from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')  
        if not user: 
            return render_template('login.html', error="Please enter a valid name.")
        return redirect(url_for('success', name=user)) 
    return render_template('login.html', error=None)

@app.route('/success/<name>')
def success(name):
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
    
