from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from .forms import usersForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contact.models import Contact
from .forms import TaskForm
from tasks.models import Task
from django.utils import timezone 

def home_view(request):
    newsData=News.objects.all()
    data={
        'newsData':newsData
    }

    
    return render(request, 'index.html',data)

def aboutus_view(request):
    return render(request, 'aboutus.html')

def service_view(request):
    servicesData=Service.objects.all().order_by('service_title')
    paginator=Paginator(servicesData,2)
    page_number=request.GET.get('page')
    ServiceDataFinal=paginator.get_page(page_number)
    totalpage=ServiceDataFinal.paginator.num_pages
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            servicesData=Service.objects.filter(service_title__icontains=st)
    data={
        'servicesData':ServiceDataFinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range (totalpage)]
    }
    return render(request, 'service.html',data)

def tasks_view(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    tasks = Task.objects.all().order_by('deadline')
    current_time = timezone.now()  # ✅ Proper way to get current time
    return render(request, 'tasks.html', {
        'form': form,
        'tasks': tasks,
        'now': current_time  # ✅ Pass to template
    })


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks')

def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('tasks')  

def userform(request):
   
    finalans=0
    fn=usersForm()
    data={'form':fn}
    try:
        if request.method=="POST":
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))
        finalans=n1+n2
        data={
            'form':fn,
            'output':finalans
        }
        return redirect(f'/thankyou/?output={finalans}')
       
    except:
        pass
    return render(request, 'userform.html',data)

def thankyou_view(request):
    if request.method=="GET":
        output=request.GET.get('output')
        
    return render(request, 'thankyou.html',{'output':output})

def calculator(request):

    result = None
         
    if request.method == "POST":
        try:
            if request.POST.get('number1')=="":
             return render(request, 'calculator.html', {'error':True})
            n1 = float(request.POST.get('number1'))
            n2 = float(request.POST.get('number2'))
            op = request.POST.get('operator')

            if op == '+':
                result = n1 + n2
            elif op == '-':
                result = n1 - n2
            elif op == '*':
                result = n1 * n2
            elif op == '/':
                result = n1 / n2 if n2 != 0 else 'Cannot divide by zero'
            else:
                result = 'Invalid operation'
        except Exception as e:
            result = f'Error: {e}'
    return render(request, 'calculator.html', {'result': result})

def contact_view(request):
     
    return render(request, "contact.html")

def savedata(request):
    if request.method == "POST":
        name = request.POST.get("contact_name")
        email = request.POST.get("contact_email")
        number = request.POST.get("contact_number")
        en=Contact.objects.create(contact_name=name, contact_email=email, contact_number=number)
        en.save()
        n='Form Filled'
    return render(request, "contact.html",{'n':n})


    


