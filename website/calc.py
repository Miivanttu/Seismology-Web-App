from flask import Blueprint, render_template

calc = Blueprint('calc', __name__)

@calc.route('/calc')
def login():
    return render_template("calc.html")