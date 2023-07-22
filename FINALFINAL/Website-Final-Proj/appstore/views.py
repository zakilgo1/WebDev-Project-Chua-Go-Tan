from django.shortcuts import render

from django.http import HttpResponse

from datetime import date
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login , logout

from django.shortcuts import render

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import QuotationForm
from .models import Quotation




# Create your views here.

all_products = [
  {
    "slug": "jeans-for-sale",
    "title": "Jeans",
    "image": "notebook 1.jpg",
    "price": 1000,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": True,
    "date": date(2023, 6, 21),
  },
  {
    "slug": "eyewear",
    "title": "Eyewear",
    "image": "eraser 1.jpg",
    "price": 2000,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": True,
    "date": date(2023, 6, 10),
  },
  {
    "slug": "shirt",
    "title": "Shirt",
    "image": "stapler 1.jpg",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": True,
    "date": date(2023, 6, 22),
  },
  {
    "slug": "shop_img",
    "title": "Shop",
    "image": "whiteboard 1.jpg",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
  
   {
    "slug": "shop_img",
    "title": "Shop",
    "image": "ballpen 1.jpg",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
   
    {
    "slug": "shop_img",
    "title": "Shop",
    "image": "calc 1.jpg",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
]

def get_date(product):
  return product['date']


@login_required(login_url = 'login')
def starting_page(request): 
  sorted_products = sorted(all_products, key=get_date)
  latest_products = sorted_products[-3:]
  return render(request, "store/index.html", {
    "products": latest_products
  })


  

def product_detail(request, slug):
  identified_product = next(product for product in all_products if product['slug'] == slug)
  return render(request, "store/product_detail.html", {
    "product": identified_product
  })
 






  

  

def home(request):
    return render(request, 'appstore/dashboard.html')

def products(request):
    return render(request, 'appstore/products.html')

def index(request):
    return render(request, 'appstore/index.html')

def featured(request):
    return render(request, 'appstore/featured.html')

def product_detail(request):
  pass



def quotation_page(request):
    try:
        quotation = Quotation.objects.first()
    except Quotation.DoesNotExist:
        quotation = None

    if request.method == 'POST':
        pen_count = request.POST.get('pen_count')
        eraser_count = request.POST.get('eraser_count')
        notebook_count = request.POST.get('notebook_count')
        stapler_count = request.POST.get('stapler_count')
        calculator_count = request.POST.get('calculator_count')
        if quotation:
            quotation.Pen_count = pen_count
            quotation.Eraser_count = eraser_count
            quotation.Notebook_count = notebook_count
            quotation.Stapler_count = stapler_count
            quotation.Calculator_count = calculator_count
            quotation.save()
            return redirect('quotation_page')

    context = {'quotation': quotation}
    return render(request, 'quotation_page.html', context)