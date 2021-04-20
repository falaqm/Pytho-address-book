from django.shortcuts import render,redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages

# Create your views here.
def home(request):
    all_addresses = Address.objects.all()
    return render(request,"home.html",{"all_addresses":all_addresses})

def add_address(request):
    # form = AddressForm()
    if request.method=='POST':
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Details Saved")
            return redirect("home")
        else:
            messages.error(request,"Something went wrong")
            return render(request,"add_address.html",{})
    # return render(request,"add_address.html",{"form":form})
    return render(request,"add_address.html",{})

def edit(request,list_id):
    get_address = Address.objects.get(id=list_id)
    if request.method=="POST":
        form = AddressForm(request.POST or None,instance=get_address)
        if form.is_valid():
            form.save()
            messages.success(request,"Address Has been edited")
            return redirect("home")
        else:
            messages.error(request,"Seems like an error")
            return render(request,"edit.html",{"get_address":get_address})
    return render(request,"edit.html",{"get_address":get_address})

def delete(request,list_id):
    if request.method=="POST":
        current_address = Address.objects.get(id=list_id)
        current_address.delete()
        messages.success(request,("Address Deleted"))
        return redirect("home")
    else:
        messages.success(request,"Nothing to see Here...")
        return redirect("home")
