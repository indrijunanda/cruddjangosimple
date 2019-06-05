from django.shortcuts import render,redirect
from simplecrud.forms import CrudsimpleForm
from simplecrud.models import Crudsimple

def tampildata(request):        
    return render(request,"index.html",{'tampilkandata':Crudsimple.objects.all()})

def inputdata(request):
    return render(request, "inputdata.html")

def simpandata(request):
    if request.method == "POST":
        form = CrudsimpleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/') #Lihat Pada urls.py saat ingin men-redirect setelah aksi save.
            except:
                pass
    else:
        form = CrudsimpleForm()
    return render(request,'inputdata.html',{'form':form})

def hapusdata(request, id):
    Crudsimple.objects.get(id=id).delete()
    return redirect('/')

def editdata(request, id):
    return render(request, "editdata.html", {'editdatanya':Crudsimple.objects.get(id=id)})

def updatedata(request, id):
    formupdatedata = CrudsimpleForm(request.POST, instance=Crudsimple.objects.get(id=id))
    if formupdatedata.is_valid():
        formupdatedata.save()
        return redirect('/')
    return render(request,'editdata.html',{'updatedatanya':Crudsimple.objecs.get(id=id)})