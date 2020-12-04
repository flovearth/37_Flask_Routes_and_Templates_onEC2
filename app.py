from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1> <br>The purpose of this web site is: Handling Routes and Templates with Flask Web Application</br>'

@app.route('/about')
def about():
    return '<h1> This is my about page.</h1>'

@app.route('/error')
def error():
    return '<h1> Either you encountered an error or you are not authorized. </h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello, World! </h1> <br>This is hello world page.</br>'

@app.route('/admin')
def admin():
    return redirect(url_for('error'))  # it redirects to another page.

@app.route('/<name>')
def greet(name):
    return render_template('greet.html', guest = name)

@app.route('/hello/<name>')
def helloname(name):
    return f'<h1> Hello, {name} </h1> <br> You are very curious...</br>'

@app.route('/greet')
def greet_admin():
    return redirect(url_for('helloname', name = 'Master Admin!!!!'))

@app.route('/greet/<name>')
def greetingpage(name):
    greet_format=f"""
<!DOCTYPE html>
<html>
<head>
    <title>Greeting HTML Page</title>
</head>
<body>
    <h1>Hello, { name }!</h1>
    <h1>Welcome to my Greeting Page</h1>
    This is created via inside HTML codes...
</body>
</html>
    """
    return greet_format

@app.route('/list100')
def list10():
    return render_template('list100.html')

@app.route('/evens')
def evens():
    return render_template('evens.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug = True)