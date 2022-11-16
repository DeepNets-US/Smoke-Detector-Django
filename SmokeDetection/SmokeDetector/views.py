from django.shortcuts import render
from keras.models import load_model
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create your views here.
def Welcome(request):

    if request.method == "POST":
        temp = request.POST['temp']
        hum = request.POST['hum']
        tvoc = request.POST['tvoc']
        eco2 = request.POST['eCO2']
        rawh2 = request.POST['rawh2']
        rawet = request.POST['rawet']
        pres = request.POST['pres']
        pm1 = request.POST['pm1']
        pm25 = request.POST['pm2.5']
        nc05 = request.POST['nc0.5']
        nc1 = request.POST['nc1']
        nc25 = request.POST['nc2.5']
        cnt = request.POST['cnt']

        scaler = StandardScaler()
        X = np.array([temp, hum, tvoc, eco2, rawh2, rawet, pres, pm1, pm25, nc05, nc1, nc25, cnt])
        X = scaler.fit_transform(X.reshape(1,-1))
        model = load_model('Smoke-Detection-Model.h5')
        class_names = ['Off', 'On']
        pred = class_names[np.argmax(model.predict(X))]
        return render(request, "main.html", {'pred':pred})

    return render(request, "main.html")