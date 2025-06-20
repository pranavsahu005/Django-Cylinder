from django.shortcuts import redirect,render,HttpResponse

data=[]
bin=[]

def home(request):
    return render(request,"home.html")

def save(request):
    data.append(request.GET)
    return render(request,"save.html",request.GET)

def display(request):
    return render(request,"display.html",{"data":data,"bin":bin})

def remove(request,index):
    data.pop(index)
    return redirect('/display')

def bin(request,index):
    temp={"value":data,"index":index}
    data.insert(index)
    return redirect('/remove')