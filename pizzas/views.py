# Create your views here.
 
 
from django.shortcuts import render, redirect
from .models import *
from .forms import *
#from .forms import *
 
# Create your views here.
 
# When a URL request matches the pattern we just defined,
# Django looks for a function called index() in the views.py file
 
def index(request):
   """The home page for Pizzeria"""
   return render(request, 'pizzas/index.html')
   #return render(request, 'pizzas/index.html')
 
def pizzas(request):
   pizzas = Pizza.objects.all()
   #pizzas = Pizza.objects.order_by('date_added')
 
   context = {'all_pizzas':pizzas}
   return render(request, 'pizzas/pizzas.html', context)
 
 
def pizza(request, pizza_id):
   pizza = Pizza.objects.get(id=pizza_id)
 
   toppings = Topping.objects.filter(pizza=pizza)
 
   context = {'pizza':pizza, 'toppings':toppings}
 
   return render(request, 'pizzas/pizza.html', context)



def new_review(request,pizza_id):

   if request.method != 'POST':
      form = ReviewForm()
   else:
      form = ReviewForm(date=request.POST)

      if form.is_valid():
         new_review = form.save(commit=False)
         new_review.pizza = pizza
         new_review.save
         return redirect('pizzas:pizza',pizza_id=pizza_id)

   context = {'form':form, 'pizza':pizza}
   return render(request, 'pizza/new_review.html', context)
