from django.shortcuts import render
from django.views import View
from .models import *
from django.core.paginator import Paginator
# Create your views here.


class HomeView(View):
    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        name = request.POST['Name']
        email = request.POST['Email']
        subject = request.POST['Subject']
        message = request.POST['Message']
        ContactForm.objects.create(name=name, email=email, subject=subject, text=message)
        return render(request, 'index.html')




class BlogView(View):
    def get(self,request):

        contact_list = BlogPost.objects.all()
        paginator = Paginator(contact_list, 5) 

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj":page_obj,
        }
        return render(request,'blog.html',context)

class SubribeView(View):
    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        email = request.POST['email']
        Subcribe.objects.create(email=email)
        return render(request, 'index.html')