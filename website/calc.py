from flask import Blueprint, render_template, request

calc = Blueprint('calc', __name__)

@calc.route('/calc', methods=['GET','POST'])
def arvuta():
    if request.method == 'POST':
        vonkeKiirus = request.form.get('vonkeKiirus')
        kaugus = request.form.get('kaugus')
        laenguMass = request.form.get('laenguMass')
        if vonkeKiirus == None and kaugus != None and kaugus != None:
            print(0)
        elif vonkeKiirus != None and kaugus != None and kaugus == None:
            print(1)
        elif vonkeKiirus != None and kaugus == None and kaugus != None:
            print(2)
    return render_template("calc.html")