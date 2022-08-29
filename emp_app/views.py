from django.shortcuts import render,redirect
from .models import Department,Role,Employee
from .forms import DepartmentForm,RoleForm,EmployeeForm
from django.db.models import Q

# Create your views here.
def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    emps=Employee.objects.filter(
        Q(name__icontains=q) |
        Q(department__name__icontains=q) |
        Q(role__name__icontains=q) )
        
     
    
    context={'emps':emps}
    return render(request,'emp_app/home.html',context)



def createEmployee(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'emp_app/create.html',{'form':form})
def createDepartment(request):
    form=DepartmentForm()
    if request.method=='POST':
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'emp_app/create.html',{'form':form})


def createRole(request):
    form=RoleForm()
    if request.method=='POST':
        form=RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'emp_app/create.html',{'form':form})

def update(request,pk):
    emp=Employee.objects.get(id=pk)
    form=EmployeeForm(instance=emp)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'emp_app/create.html',context)


def delete(request,pk):
    emp=Employee.objects.get(id=pk)
    if request.method=="POST":
        emp.delete()
        return redirect('home')
    return render(request,'emp_app/delete.html',{"obj":emp})
        
    
