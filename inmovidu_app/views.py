from django.shortcuts import render , redirect
from .models import company,job,student,apply
# Create your views here.
id_for_comp=""
def index(request):
    return render(request,"index.html")
def company_login(request):
    name=request.POST["id-company-login"]
    password=request.POST["pass-company-login"]
    Company=company.objects.all()
    for x in Company:
        if (x.name==name or x.email==name) :
            if(x.password==password):
                global id_for_comp
                id_for_comp=x.id
                return redirect("company1")
    return redirect("home")
def companylog(request):
    Job_by_you=job.objects.filter(compid=id_for_comp)
    all_jobs=job.objects.all()
    Company=company.objects.filter(id=int(id_for_comp))
    name=""
    for x in Company:
        name=x.name
    Apply=apply.objects.filter(jobid=name)
    return render(request,"company_page.html",{'jobs_by_you':Job_by_you,'alljobs':all_jobs,'apply':Apply})
def addjob(request):
    position=request.POST["addjob_position"]
    req=request.POST["addjob_req"]
    mail=request.POST["addjob_mail"]
    ctc=request.POST["addjob_CTC"]
    id=0
    cname=""
    Company=company.objects.all()
    for x in Company:
        if (x.email==mail) :
            id=x.id
            global id_for_comp
            id_for_comp=x.id
            cname=x.name
    Job=job()
    Job.position=position
    Job.requirement=req
    Job.ctc=ctc
    Job.compid=id
    Job.cname=cname
    Job.save()
    return redirect("company1")
def reg_comp(request):
    name=request.POST['name-company-reg']
    email=request.POST['id-company-reg']
    password=request.POST['pass-company-reg']
    Company=company()
    Company.name=name
    Company.email=email
    Company.password=password
    Company.save()
    return redirect("company1")
def studentlogin(request):
    name=request.POST['id-student-login']
    password=request.POST['pass-student-login']
    Student=student.objects.all()
    for x in Student:
        if (x.name==name or x.email==name) :
            if(x.password==password):
                return redirect("studentlog")
    return redirect("home")
def studentlog(request):
    Jobs=job.objects.all()
    return render(request,"student_page.html",{'jobs':Jobs})
def student_apply(request):
    name=request.POST['name']
    email=request.POST['email']
    yop=request.POST['yop']
    url=request.POST['url']
    jobid=request.POST['job_id']
    position=request.POST['position']
    Apply=apply()
    Apply.name=name
    Apply.email=email
    Apply.yop=yop
    Apply.resume=url
    Apply.jobid=jobid
    Apply.position=position
    Apply.save()
    return redirect("studentlog")
def studentregister(request):
    name=request.POST['name-student-reg']
    email=request.POST['id-student-reg']
    password=request.POST['pass-student-reg']
    Student=student()
    Student.name=name
    Student.email=email
    Student.password=password
    Student.save()
    return redirect("studentlog")
