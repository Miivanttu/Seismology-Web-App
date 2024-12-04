from flask import Blueprint, render_template, request
import numpy as numpy

calc = Blueprint('calc', __name__)
A = -0.4119
B = 0.9096
@calc.route('/calc', methods=['GET','POST'])
def arvuta():
    result = None
    if request.method == 'POST':
        arvutusMethod = request.form.get('arvutusMethod')
        arvutusObject = request.form.get('arvutusObject')
        vonkeKiirus = request.form.get('vonkeKiirus', type=float)
        kaugus = request.form.get('kaugus', type=float)
        laenguMass = request.form.get('laenguMass', type=float)
        ehitiseLiik = request.form.get('ehitiseLiik', type=float)
        obejAluspin = request.form.get('objectAluspinnas', type=float)
        ehitiseAluspin = request.form.get('ehitiseAluspinnas')
        if arvutusObject == "1":
            if arvutusMethod == "1":
                if kaugus != None and laenguMass != None:
                    result = vonkeKiirusArvuta(kaugus, laenguMass)
                else:
                    result = 40 
            elif arvutusMethod == "2":
                if vonkeKiirus != None and kaugus != None:
                    result = laenguMassArvuta(vonkeKiirus, kaugus)
                else:
                    result = 50 
        elif arvutusObject == "2":
            maxVonkeKiirus = vonkeMaxKiirusArvuta(kaugus, ehitiseLiik)
            result = maxLaenguMassArvuta(maxVonkeKiirus, kaugus, obejAluspin)
    return render_template("calc.html", result = result)

def vonkeKiirusArvuta(kaugus, laenguMass):
    d1 = kaugus/numpy.sqrt(laenguMass)
    vonkeKiirus = B * d1**A
    return vonkeKiirus

def laenguMassArvuta(vonkeKiirus, kaugus):
    laenguMass = (kaugus/((B/vonkeKiirus)**(-1/A)))**2
    return laenguMass


def vonkeMaxKiirusArvuta(lubatudKiitus, ehiLiik):
    maxVonkeKiirus = lubatudKiitus * ehiLiik
    return maxVonkeKiirus

def maxLaenguMassArvuta(maxVonkeKiirus, kaugus, pinnas):
    laenguMass = (maxVonkeKiirus**2)*(kaugus**2.7)/(pinnas**2)
    return laenguMass