from django.shortcuts import render,redirect
from . models import Cakes
from . forms import CakeForm
# Create your views here.




def demo2(request):
    cakes=Cakes.objects.all()
    return render(request,'index.html',{'cakes':cakes})

def detail(request,cake_id):
    cake_list=Cakes.objects.get(id=cake_id)
    context={
        'cakes': cake_list
    }
    return render(request,'detail.html',context)

def add_cake(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['img']
        cake=Cakes(name=name,desc=desc,price=price,img=image)

        cake.save()
    return render(request,'add.html')

def update(request,id):
    cake=Cakes.objects.get(id=id)
    form=CakeForm(request.POST or None, request.FILES, instance=cake)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'cake':cake})

def delete(request,id):
    if request.method == 'POST':
        cake=Cakes.objects.get(id=id)
        cake.delete()
        return redirect('/')

    return render(request,'delete.html')