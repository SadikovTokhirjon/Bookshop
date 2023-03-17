from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Book

class ListView(ListView):
    template_name='list.html'
    queryset=Book.objects.all()
    context_object_name='lists'
    paginate_by=2

# class ListView(View):
#     def get(self,request):
#         lists=Book.objects.all()
#         return render(request,'list.html',{'lists':lists})

class DetailsView(DetailView):
    template_name = 'details.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'details'
    model = Book


# class DetailsView(View):
#     def get(self,request,pk):
#         details=Book.objects.get(id=pk)
#         return render(request,'details.html',{'details':details})