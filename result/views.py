from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import names,subject,marks

# Create your views here.
# data retreive methods all , get , filter 
def index(request):
 
    return render(request,'result/index.html')

def grade_point_calc(marks):
    if marks>=90 :return 10;
    if marks>=75 :return 9;
    if marks>=60 :return 8;
    if marks>=50 :return 7;
    if marks>=40 :return 6;
    return 0;

class A:
    total_credit_points = float()
    total_credits = float()
    total_marks = int()
    percentage = str()
    sgpa = float()
    total_max_marks = int()
    list_of_subjects = list()
    sem=int()

def find(reg,semes=1):
    list2 = marks.objects.filter(reg_no=reg,sem=semes)
    sem1 = A()
    if not list2:return sem1
    sem1.list_of_subjects = list2
    i=0
    total_marks = 0
    total_m_marks = 0
    total_credits = 0 
    total_credit_points = 0
    while i<len(list2):
        total_credits += list2[i].sub_code.sub_credit
        if list2[i].sub_code.sub_credit == 1.0:
            total_marks += list2[i].internal
            total_m_marks +=50
            if not list2[i].internal<20:
                total_credit_points += grade_point_calc(list2[i].internal*2)
        else:
            total_marks += (list2[i].theory + list2[i].internal)
            total_m_marks += 100
            if not (list2[i].internal<20 or list2[i].theory<20):
                total_credit_points += grade_point_calc(list2[i].theory + list2[i].internal)*list2[i].sub_code.sub_credit
        i+=1
    sem1.total_max_marks = total_m_marks
    sem1.total_marks = total_marks  
    sem1.total_credit_points = total_credit_points 
    sem1.total_credits = total_credits
    sem1.percentage = str(round((total_marks/total_m_marks)*100,2))
    sem1.sgpa = str(round((total_credit_points/total_credits),2))
    sem1.sem = semes
    return sem1



def fetch_result(request):
    reg=request.GET['reg']
    reg=reg.upper()
    try: 
        list1 = names.objects.get(reg_no=reg)
    except:
        return HttpResponse("Register Number not found...!")
    
    dummy = marks.objects.filter(reg_no=reg)
    if not dummy:
        return HttpResponse("Sorry !! " + list1.name + ", No results found in database")
    
    sems=list()
    for i in range(9):
        sems.append(find(reg,i+1))

    total_marks=0
    total_credits = 0
    total_credit_points = 0
    total_max_marks =0
    
    for each_sem in sems:
        total_marks += int(each_sem.total_marks)
        total_credits += each_sem.total_credits
        total_credit_points += each_sem.total_credit_points
        total_max_marks += int(each_sem.total_max_marks)

    
    context = {
        'cgpa':str(round((total_credit_points/total_credits),2)),
        'aggregate':str(round(((total_marks/total_max_marks)*100),2)),
        'basic':list1,
        'sems':sems,
    }
   
    
    
    return render(request,'result/index-r.html',context)
    


       
