from django.shortcuts import render
from django.views import View
from core.forms import ContactForm

# Create your views here.


class HomePage(View):
    def get(self,request):
        return render(request,"core/home_page.html")
    



class ContactPage(View):
    def get(self,request):
        form =  ContactForm()
        return render(request,"core/contact.html",{"form":form})

    def post(self,request):
        pass
