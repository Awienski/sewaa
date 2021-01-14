from django.shortcuts import render, reverse
from .models import Product, Category, ProductInstance
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product/index.html', {
        'products' : products,
        'categories' : categories,
    })

def product_category(request, category):
    products = Product.objects.filter(category__name__contains=category).order_by('-created_on')
    return render(request, 'product/product_category.html', {
        'products' : products,
        'category' : category,
    })

def detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product/detail.html', {
        'product' : product,
    })

@login_required
def sewaa(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product/sewaa.html', {
        'product' : product,
    })

def loanedprodcuctbyuser(request):
    user = User.objects.get(username='rinta')
    products = ProductInstance.objects.filter(borrower=user).filter(status__exact='o').order_by('due_back')
    return render(request, 'product/productinstance_list_borrowed_user.html', {
        'products' : products,
        'user' : user,
    })

def profile(request):
    user= request.user
    loanedproducts = ProductInstance.objects.filter(borrower=user).order_by('due_back')
    ownedprodcuts = Product.objects.filter(owner=user).order_by('name')
    return render(request, 'product/profile.html', {
        'user' : user,
        'loanedproducts' : loanedproducts,
        'ownedprodcuts' : ownedprodcuts,
    })

def about(request):
    return render(request, 'product/about.html')

def add(request):
    return render(request, 'product/add.html')

def update(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product/update.html', {
        'product' : product,
    })

def delete(request, id):
    product = Product.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('product:profile'))

def productchatdetail(request, id):
    product = Product.objects.get(pk=id)
    chat = product.chat_set.all()
    return render(request, 'product/productchatdetail.html', {
        'product' : product,
        'chats' : chat,
    })

def chat(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        new_chat = request.POST['chat']
    
    product.chat_set.create(text=new_chat)
    return HttpResponseRedirect(reverse('product:productchatdetail', args=(product.id,)))