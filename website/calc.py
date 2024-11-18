from flask import Blueprint, render_template, request, jsonify

calc = Blueprint('calc', __name__)

@calc.route('/calc', methods=['GET','POST'])
def arvuta():
    result = None
    if request.method == 'POST':
        vonkeKiirus = request.form.get('vonkeKiirus')
        kaugus = request.form.get('kaugus')
        laenguMass = request.form.get('laenguMass')

        if vonkeKiirus == None and kaugus != None and laenguMass != None:
            result = testFunc(0, kaugus, laenguMass)
        elif vonkeKiirus != None and kaugus != None and laenguMass == None:
            result = testFunc(vonkeKiirus, kaugus, 0)
        elif vonkeKiirus != None and kaugus == None and laenguMass != None:
            result = testFunc(vonkeKiirus, 0, laenguMass)
        elif vonkeKiirus != None and kaugus != None and laenguMass != None:
            result = testFunc(vonkeKiirus, kaugus, laenguMass)
        else:
            result = testFunc(1, 2, 5)
    return render_template("calc.html", result = result)


def parameetriArvutamine(vonk, kaug, laen): #funktsioon parameetri leidmiseks, kirjuta arvutamis meetod
    result = vonk + kaug + laen
    return result
