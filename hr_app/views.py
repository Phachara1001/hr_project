from django.shortcuts import render,redirect
from .models import Person
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    person_qry = Person.objects.all()
    context = {'person':person_qry}
    return render(request,'base.html',context)

def add(request):
    if request.method == 'POST':
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        workyear = request.POST['workyear']
        contract = request.POST['contract']
        email = request.POST['email']
        facecook = request.POST['facebook']
        line = request.POST['line']
        telephone = request.POST['telephone']
        pic = request.FILES['picture']
        person = Person(
            p_firstname=f_name,p_lastname=l_name,p_picture=pic,p_workyear=workyear,p_contract=contract,p_email=email,p_facebook=facecook,p_line=line,p_telephone=telephone
            )
        person.save()
        return redirect('/list')
    return render(request,'add.html')

def list(request):
    person_qry = Person.objects.all()
    context = {'person':person_qry}
    return render(request,'list.html',context)

def manage(request):
    person_qry = Person.objects.all()
    context = {'person':person_qry}
    return render(request,'manage.html',context)

def custom_login(request): #ชื่อฟังชั่น
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:#ถ้าไม่เป็นค่าว่าง
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/list')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
            pass
    return render(request,'login.html') #ชื่อไฟล์ที่จะแสดง

def logout_view(request):
    logout(request)
    return render(request,'login.html')