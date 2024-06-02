from django.shortcuts import render
from .models import Person,Employee,LookUpTable
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')

def remove(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Person.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Person.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove.html',context)

def all(request):
    emps = Person.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'all.html',context)

def add(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone_number = request.POST.get('phone_number', '')
        username = request.POST['username']
        address = request.POST.get('address', '')
        region = request.POST.get('region', '')
        date_of_birth = request.POST.get('date_of_birth', None)
        cnic = request.POST.get('cnic', '')
        status = int(request.POST.get('status', 0))
        father_name = request.POST.get('father_name', '')
        gender = request.POST.get('gender', '')

        # Create new employee instance
        new_emp = Person(
            email=email,
            phone_number=phone_number,
            username=username,
            address=address,
            region=region,
            date_of_birth=date_of_birth,
            cnic=cnic,
            status=status,
            father_name=father_name,
            gender=gender
        )

        # Save the new employee to the database
        new_emp.save()
        
        return HttpResponse('Employee added Successfully')
    elif request.method == 'GET':
        return render(request, 'add.html')
    else:
        return HttpResponse("An Exception Occurred! Employee Has Not Been Added")