"""
Application to demo AJAX web app using Flask.
The home page will call AJAXDemo.html where on user button click, we will load the contents of 
a div by calling an API.

The API is located at /testAPI and returns another HTML file rendered.

The demo also shows how to use form elements into request object and use AJAX to load content without page refresh
"""
import flask
from flask import jsonify
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

"""
Home page route
"""
@app.route("/")
def index():
    return render_template("AJAXDemo.html", urlroot=request.url_root, project="Projectname")

"""
API route
"""
@app.route("/testAPI", methods=['GET', 'POST'])
def test():
    # Get values from drop down form elements
    select1 = request.form.get('select1').strip()
    select2 = request.form.get('select2').strip()

    # Get checkbox selection boolean value
    # True or False depending on selection
    check1 = "option1" in request.form 
    check2 = "option2" in request.form
    
    return render_template("small_html.html", select1=select1, select2=select2, project_hidden=request.form.get('project_hidden'))

    """
    You can also return direct HTML contents instead of render_template call

    # return f"<h3>Hello from API!</h3><p>You selected { select1.upper() } and { select2.upper() } from dropdowns.</p> <br/> \
    # Checkbox values are { check1 } and { check2 } \
    # 
    """

if __name__ == "__main__":
    app.run(debug=True)