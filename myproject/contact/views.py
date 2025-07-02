# contact/views.py
from django.shortcuts import render
from .forms import ContactForm
from .models import Message  # ixtiyoriy

def contact_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():

            return render(request,'contact/success.html')
    else:
        form=ContactForm()
    return render(request,'contact/contact_form.html',{'form':form})


