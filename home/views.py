from django.shortcuts import render, HttpResponse
import joblib


import os
model_path = os.path.join(os.path.dirname(__file__), 'static', 'Random Forest.pkl')
model = joblib.load(model_path)



# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is the home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is the about page")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is the contact page")



def prediction(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))
        resting_BP = int(request.POST.get('resting_BP'))
        cholesterol = int(request.POST.get('cholesterol'))
        MaxHR = int(request.POST.get('MaxHR'))
        oldpeak = int(request.POST.get('oldpeak'))
        sex = int(request.POST.get('sex'))
        chest_pain = int(request.POST.get('chest_pain'))
        fasting_bs = int(request.POST.get('fasting_bs'))
        resting_ECG = int(request.POST.get('resting_ECG'))
        ExerciseAngina = int(request.POST.get('ExerciseAngina'))
        ST_Slope = int(request.POST.get('ST_Slope'))
        

        print(age, resting_BP, cholesterol, MaxHR, oldpeak, sex, chest_pain, fasting_bs, resting_ECG, ExerciseAngina, ST_Slope )

        pred = (model.predict([[age,sex,chest_pain, resting_BP, cholesterol,fasting_bs, resting_ECG, MaxHR,ExerciseAngina, oldpeak, ST_Slope]])[0]  ) 
        if (pred == 0 ) :
            output = "No Heart Disease"
            para = "The results are reassuring, but it's important to continue with heart-healthy habits like regular exercise and balanced nutrition."
        else : 
            output = "Heart Disease"
            para = "The results are reassuring, but it's important to continue with heart-healthy habits like regular exercise and balanced nutrition."

        print(pred)

        output = {
            "output":output,
            "para" : para
        }


        return render(request, 'prediction/.html', output)
    else:
        return render(request, 'prediction/.html')

       
    #return HttpResponse("This is the prediction page")    



'''Yaha par urls.py se path functionpath('', views.index, name='home'),
me jab kuchh bhi nhi h toh waha se request aayegi views.py ke index function me phir index function
jo h response return karega'''