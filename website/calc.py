from flask import Blueprint, render_template, request

calc = Blueprint('calc', __name__)

@calc.route('/calc', methods=['GET','POST'])
def arvuta():
    result = None
    if request.method == 'POST':
        vonkeKiirus = request.form.get('vonkeKiirus', type=float)
        kaugus = request.form.get('kaugus', type=float)
        laenguMass = request.form.get('laenguMass', type=float)
        if vonkeKiirus == None and kaugus != None and laenguMass != None:
            result = vonkeKiirusArvuta(vonkeKiirus, kaugus, laenguMass)
        elif vonkeKiirus != None and kaugus != None and laenguMass == None:
            result = laenguMassArvuta(vonkeKiirus, kaugus, laenguMass)
        elif vonkeKiirus != None and kaugus == None and laenguMass != None:
            result = kaugusArvuta(vonkeKiirus, kaugus, laenguMass)
        else:
            result = None 
    return render_template("calc.html", result = result)


def kaugusArvuta(vonkeKiirus, kaugus, laenguMass):  #täita kausguse arvutamiseks funktsioon
    result = 10
    return result

def vonkeKiirusArvuta(vonkeKiirus, kaugus, laenguMass):  #täita vonkeKiirus arvutamiseks funktsioon
    result = 20
    return result

def laenguMassArvuta(vonkeKiirus, kaugus, laenguMass):  #täita laenguMass arvutamiseks funktsioon
    result = 40
    return result
