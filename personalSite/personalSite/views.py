from personalSite import app
from flask import render_template

@app.route('/')
def index():
    #JLC since we are using template inheritance we must render the child template
    return render_template('head.html')
