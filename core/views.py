from django.shortcuts import render,redirect
from django.views import View
from core.forms import ContactForm
from django.contrib import messages

# Create your views here.


class HomePage(View):
    def get(self,request):
        return render(request,"core/home_page.html")
    



class ContactPage(View):
    def get(self,request):
        form =  ContactForm()
        return render(request,"core/contact.html",{"form":form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thank You!, Your message has been sent")
            return redirect("contact-page")
        
        return render(request,"core/contact.html",{"form":form})
        
