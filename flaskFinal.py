try:
    from flask import Flask
    from flask import render_template
    print("all modules loaded")

except:
    print("some modules missing")

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tryout')
def tryout():
    return render_template('tryout.html')

@app.route('/ga4setup')
def ga4setup():
    return render_template('ga4setup.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')

if __name__ == '__main__':
    app.run(debug=True)