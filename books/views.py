from django.shortcuts import render
from django.views import View
from .models import Book


class ListView(View):
    def get(self,request):
        lists=Book.objects.all()
        return render(request,'list.html',{'lists':lists})

class DetailsView(View):
    def get(self,request,pk):
        details=Book.objects.get(id=pk)
        return render(request,'details.html',{'details':details})