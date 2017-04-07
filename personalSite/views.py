from personalSite import application
from flask import render_template

@application.route('/')
def index():
    #JLC since we are using template inheritance we must render the child template
    return render_template('index.html')

@application.route('/Projects')
def projects():
    return render_template('projects.html')

@application.route('/Research')
def research():
    return render_template('research.html')

@application.route('/Tutorials')
def tutorials():
    return render_template('tutorials.html')

@application.route('/first-hackathon-project')
def first_hackathon_project():
    return render_template('FirstProject.html')


