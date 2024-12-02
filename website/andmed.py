from flask import Blueprint, render_template

andmed = Blueprint('andmed', __name__)

@andmed.route('/andmed', methods=['GET'])
def andmed_home():
    return render_template('andmed.html')