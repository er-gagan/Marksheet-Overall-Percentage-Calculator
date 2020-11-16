from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request,'home/home.html')

@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        tenObtain = request.POST['tenObtain']
        tenTotal = request.POST['tenTotal']
        twelveObtain = request.POST['twelveObtain']
        twelveTotal = request.POST['twelveTotal']
        GraduationObtain = request.POST['GraduationObtain']
        GraduationTotal = request.POST['GraduationTotal']
        PostGraduationObtain = request.POST['PostGraduationObtain']
        PostGraduationTotal = request.POST['PostGraduationTotal']
        if GraduationObtain == "" and PostGraduationObtain == "":
            A = sum([eval(tenObtain),eval(twelveObtain)])*100
            B = sum([eval(tenTotal),eval(twelveTotal)])
            result = A/B
            msg = "Overall Percentage for Class 10th and 12th is "+"%0.2f"%result
        elif PostGraduationObtain == "":
            A = sum([eval(tenObtain),eval(twelveObtain),eval(GraduationObtain)])*100
            B = sum([eval(tenTotal),eval(twelveTotal),eval(GraduationTotal)])
            result = A/B
            msg = "Overall Percentage for Class 10th, 12th and Graduation is "+"%0.2f"%result
        else:
            A = sum([eval(tenObtain),eval(twelveObtain),eval(GraduationObtain),eval(PostGraduationObtain)])*100
            B = sum([eval(tenTotal),eval(twelveTotal),eval(GraduationTotal),eval(PostGraduationTotal)])
            result = A/B
            msg = "Overall Percentage for Class 10th, 12th, Graduation and Post-Graduation is "+"%0.2f"%result
        return render(request,"home/home.html",{'msg':msg})
    else:
        return HttpResponse("404 - Not Found")