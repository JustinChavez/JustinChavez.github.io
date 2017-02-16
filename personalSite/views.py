from personalSite import app
from flask import render_template

@app.route('/')
def index():
    #JLC since we are using template inheritance we must render the child template
    return render_template('index.html')

@app.route('/Projects')
def projects():
    return render_template('projects.html')

@app.route('/Research')
def research():
    return render_template('research.html')

@app.route('/Tutorials')
def tutorials():
    return render_template('tutorials.html')