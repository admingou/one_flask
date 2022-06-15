from flask import render_template

def web_errors():
    return render_template("error.html")