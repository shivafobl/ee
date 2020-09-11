from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import EeeStudentRegister,Faculty
from django.contrib import messages
from .forms import FacultyRegisterForm
from College import settings
from django.core.mail import EmailMessage
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.models import User

# Create your views here.
def index(req):
	return render(req,"EEE/index.html")


def home(req):
	return render(req,"EEE/home.html")

def about(req):
	return render(req,"EEE/about.html")

def gallery(req):
    return render(req,"EEE/gallery.html")

def register(request):
    error=""

    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        uname=request.POST['username']
        em=request.POST['email']
        img=request.FILES['img']
        mb=request.POST['mobileno']
        dob=request.POST['dob']
        pwd=request.POST['pswd']
        

        try:
            user=User.objects.create_user(first_name=fname,last_name=lname,
                username=uname,email=em,password=pwd)
            EeeStudentRegister.objects.create(user=user,image=img,mobileno=mb,dob=dob)
            
            
            error = "no"

            sub='Regards Student Register'
            body='hi  '+fname +lname+',\n We are glad to have you in our platform'
            send=settings.EMAIL_HOST_USER
            reciever=em
            #message.attach('design.png', img_data, 'image/png')
            email_msg=EmailMessage(sub,body,send,[reciever])
            email_msg.send()

        except:
            error="yes"
    

    # sub='Regards Student Register'
    # body='hi'+fname+',\n We are glad to have you in our platform'
    # send=settings.EMAIL_HOST_USER
    # reciever=em
    # #message.attach('design.png', img_data, 'image/png')
    # email_msg=EmailMessage(sub,body,send,[reciever])
    # email_msg.send()
    

    context={'error':error}     




    return render(request,'EEE/register.html',context)



def signin(request):
    error=""
    if request.method=="POST":
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=authenticate(username=uname,password=pwd)
        try:
            if user:
                login(request,user)
                error="no"
            else:
                error='yes'
        except:
            error="yes"
    context={'error':error}
    return render(request,'EEE/signin.html',context)


def userprofile(request):
    user=User.objects.get(id=request.user.id)
    pro=EeeStudentRegister.objects.get(user=user)
    context={'user':user,'pro':pro}
    return render(request,'EEE/userprofile.html',context)

def changepassword(request):

    error=""
    if request.method=="POST":
        o=request.POST['oldpwd']
        n=request.POST['newpwd']
        con=request.POST['conpwd']

        if n==con:


            user=User.objects.get(username__exact=request.user.username)
            user.set_password(n)
            user.save()
            error='no'


        else:
            error="yes"

    context={'error':error}


    return render(request,'EEE/changepassword.html',context)


def signout(request):
    logout(request)
    return redirect('home')

def editprofile(request):
    user=User.objects.get(id=request.user.id)
    pro=EeeStudentRegister.objects.get(user=user)
    error=""
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        if 'img' in request.FILES:
            img=request.FILES['img']
        else:
            img=None
        mb=request.POST['mobileno']
        dob=request.POST['dob']
        user.first_name=fname
        user.last_name=lname
        pro.mobileno=mb
        pro.dob=dob
        if img:
            pro.image=img

        try:
            user.save()
            pro.save()
            error="no"
        except:
            error="yes"

    context={"error":error,'user':user,'pro':pro}
    
    
    return render(request,'EEE/editprofile.html',context)



# def register(request):
#     if request.method == 'POST':
#         #fname=request.POST['first_name']
#         #lname=request.POST['last_name']
#         #uname=request.POST['username']
#         #em=request.POST['email']
#         name = request.POST.get('name')
#         username=request.POST.get('username')
#         phone_num = request.POST["phone_num"]
#         email = request.POST.get('email')
#         age = request.POST.get('age')
#         pwd=request.POST.get('pwd')
#         #pwd=request.POST['pswd']
#         #user=User.objects.create_user(username=uname,password=pwd)
#         student = EeeStudentRegister(student_name=name,user_name=username, phone_num=phone_num,
#                                      email=email, age=age,password=pwd)
#         student.save()
#         # sub='Regards Student Register'
#         # body='hi'+name+',\n We are glad to have you in our platform'
#         # send=settings.EMAIL_HOST_USER
#         # reciever=email
#         # #message.attach('design.png', img_data, 'image/png')
#         # email_msg=EmailMessage(sub,body,send,[reciever])
#         # email_msg.send()

#         messages.success(request,'Student added successfully')

#         return redirect('student_details')
#     return render(request, 'EEE/register.html')

# def login(request):
#     #return render(request,"EEE/login.html")



#     error=""
#     if request.method=="POST":
#         uname=request.POST['uname']
#         pwd=request.POST['pwd']
#         user=authenticate(user_name=uname,password=pwd)
#         try:
#             if user:
#                 login(request,user)
#                 error="no"
#             else:
#                 error="yes"
#         except:
#             error="yes"
#     context={'error':error}
#     #return render(request,'accounts/signin.html',context)
#     return render(request,"EEE/login.html",context)




def student_details(request):
    details = EeeStudentRegister.objects.all()
    return render(request,'EEE/student_data.html', {'data': details})



def faculty_data(request):
    details1 = Faculty.objects.all()
    return render(request,'EEE/faculty_data.html', {'data': details1})




def edit(request, id):
    student = EeeStudentRegister.objects.get(id=id)
    if request.method == "POST":
        student.username = request.POST.get('username')
        student.email = request.POST.get('email')
        student.mobileno = request.POST.get('mobileno')
        student.dob = request.POST.get('dob')

        student.save()
        messages.info(request,'Student details updated successfully')
        return redirect('student_details')
    return render(request, 'EEE/edit.html', {'data': student})



# def fedit(request, id):
#     faculty = Faculty.objects.get(id=id)
#     if request.method == "POST":
#         faculty.name = request.POST.get('name')
#         faculty.email = request.POST.get('email')
#         faculty.phone = request.POST.get('phone')
#         faculty.emp_id = request.POST.get('emp_id')

#         student.save()
#         messages.info(request,'Faculty details updated successfully')
#         return redirect('faculty_data')
#     return render(request, 'Faculty/fedit.html', {'data': faculty})



def delete(request,id):
    student = EeeStudentRegister.objects.get(id=id)
    student.delete()
    messages.info(request,'Student details Deleted successfully')
    return redirect('student_details')

def fdelete(request,num):
    faculty = Faculty.objects.get(id=num)
    
    faculty.delete()
    return redirect('faculty_data')


def facultyregister(request):
    form=FacultyRegisterForm()
    if request.method == "POST":
        form_data=FacultyRegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('faculty_data')
        return HttpResponse("invailid")

    return render(request,'EEE/facultyregister.html',{'form':form})
    


def facultyedit(request,num):
    faculty_data = Faculty.objects.get(id=num)
    form = FacultyRegisterForm(request.POST or None,instance=faculty_data)
    # if request.method == "POST":
    #     form_data_html = FacultyRegisterForm(request.POST,instance=instance)
    if form.is_valid():

        form.save()

        return redirect('student_details')
    return render(request,'EEE/facultyedit.html',{'form':instance})


def eee(request):
    return HttpResponse("welcome")



























