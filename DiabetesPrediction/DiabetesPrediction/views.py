from django.shortcuts import render
import joblib


def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')
def result(request):
    val1=float(request.GET['n1'])
    val2=float(request.GET['n2'])
    val3=float(request.GET['n3'])
    val4=float(request.GET['n4'])
    val5=float(request.GET['n5'])
    val6=float(request.GET['n6'])
    val7=float(request.GET['n7'])
    val8=float(request.GET['n8'])
    loaded_model=joblib.load("C:/Users/Albin T S/Desktop/AIML project/diabetes_prediction/DiabetesPrediction/DiabetesPrediction/knn.pkl")
    pred=loaded_model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    result1=""
    if pred==[1]:
        result1="positive"
    else:
        result1="negative"
    return render(request,"predict.html",{"result2":result1})