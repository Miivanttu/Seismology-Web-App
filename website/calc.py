from flask import Blueprint, render_template, request
import numpy as numpy

calc = Blueprint('calc', __name__)
A = -0.0088
B = 3.9126
ehitisAluspinValue = [
    [1.8, 3.5, 14.0],
    [1.8, 3.5, 8.5],
    [1.8, 3.5, 7.0],
    [1.5, 2.8, 5.5],
    [1.4, 2.5, 4.5],
    [1.2, 2.1, 3.8],
    [1.0, 1.7, 2.8],
    [0.9, 1.4, 2.2],
    [0.7, 1.1, 1.5],
    [0.6, 0.9, 1.2],
    [0.5, 0.7, 0.9],
]

ehiAluspinKaugusRanges = [
    (0, 1),  
    (1.1, 5),
    (5.1, 10),
    (10.1, 20),
    (20.1, 30),  
    (30.1, 50), 
    (50.1, 100), 
    (100.1, 200), 
    (200.1, 500),  
    (500.1, 1000), 
    (1000.1, 2000)
]
@calc.route('/calc', methods=['GET','POST'])
def arvuta():
    result = None
    laenguMass = None
    vonkeKiirus = None
    maxVonkeKiirus = None
    checkMethod = 1
    if request.method == 'POST':
        arvutusMethod = request.form.get('arvutusMethod')
        arvutusObject = request.form.get('arvutusObject')
        vonkeKiirus = request.form.get('vonkeKiirus', type=float)
        kaugusArvuta = request.form.get('kaugusArvuta', type=float)
        kaugusOhutu = request.form.get('kaugusOhutu', type=float)
        laenguMass = request.form.get('laenguMass', type=float)
        ehitiseLiik = request.form.get('ehitiseLiik', type=float)
        obejAluspin = request.form.get('objectAluspinnas', type=float)
        ehitiseAluspin = request.form.get('ehitiseAluspinnas', type=int)
        if arvutusObject == "1":
            if arvutusMethod == "1":
                if kaugusArvuta != None and laenguMass != None:
                    result = vonkeKiirusArvuta(kaugusArvuta, laenguMass)
                    checkMethod = 1
            elif arvutusMethod == "2":
                if vonkeKiirus != None and kaugusArvuta != None:
                    result = laenguMassArvuta(vonkeKiirus, kaugusArvuta)
                    checkMethod = 1
        elif arvutusObject == "2":
            lubatudKiirus = ehitAluspinMaxVonkekiirus(ehitiseAluspin, kaugusOhutu)
            maxVonkeKiirus = vonkeMaxKiirusArvuta(lubatudKiirus, ehitiseLiik)
            result = maxLaenguMassArvuta(maxVonkeKiirus, kaugusOhutu, obejAluspin)
            checkMethod = 2
    return render_template("calc.html", result = result, 
                           laenguMass = laenguMass, 
                           vonkeKiirus = vonkeKiirus, 
                           maxVonkeKiirus = maxVonkeKiirus, 
                           checkMethod = checkMethod); result = None; laenguMass = None; vonkeKiirus = None

def vonkeKiirusArvuta(kaugus, laenguMass):
    ds = kaugus/numpy.sqrt(laenguMass)
    vonkeKiirus = A * ds + B
    return vonkeKiirus

def laenguMassArvuta(vonkeKiirus, kaugus):
    ds = (vonkeKiirus - B)/A
    laenguMass = (kaugus**2)/(ds**2)
    return laenguMass


def vonkeMaxKiirusArvuta(lubatudKiirus, ehiLiik):
    maxVonkeKiirus = lubatudKiirus * ehiLiik
    return maxVonkeKiirus

def maxLaenguMassArvuta(maxVonkeKiirus, kaugus, pinnas):
    laenguMass = (maxVonkeKiirus**2)*(kaugus**2.7)/(pinnas**2)
    return laenguMass

def ehitAluspinMaxVonkekiirus(ehitiseAluspin, kaugus):
    for idx, (low, high) in enumerate(ehiAluspinKaugusRanges):
        if low <= kaugus <= high:
            return ehitisAluspinValue[idx][ehitiseAluspin]
    return 0