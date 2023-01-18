from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from testapp.models import Product
from django.core.paginator import Paginator
# Create your views here.
class create_view(CreateView):
    model=Product
    fields=['pname','pid','category','categoryid']


class Product_list(ListView):
    model=Product

class Product_detail(DetailView):
    model=Product

class Product_update(UpdateView):
    model=Product
    fields=['pname','category']

def listing(request):
    product_list=Product.objects.all()
    paginator=Paginator(product_list,10)


    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'testapp/product_list.html',{'page_obj':page_obj,'product_list':product_list})
