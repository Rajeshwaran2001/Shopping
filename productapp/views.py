from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'index.html')


def listCategory(request):
    allcategories = Category.objects.all()
    return render(request, 'shop/listcategory.html', {'allcategories': allcategories})

@login_required()
def insertCategory(request, id=0):
    if id == 0:
        if request.method == 'GET':
            form = CategoryForm()
            return render(request, 'shop/insertcategory.html', {'form': form})
        else:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/listcategory')
    else:
        if request.method == 'GET':
            cat = Category.objects.get(id=id)
            form = CategoryForm(instance=cat)
            return render(request, 'shop/insertcategory.html', {'form': form})
        else:
            cat = Category.objects.get(id=id)
            form = CategoryForm(request.POST, instance=cat)
            if form.is_valid():
                form.save()
                return redirect('/listcategory')

@login_required()
def deleteCategory(request, id=0):
    Category.objects.filter(id=id).delete()

    return redirect('/listcategory')


def listProduct(request):
    allproducts = Product.objects.all()
    return render(request, 'shop/listproduct.html', {'allproducts': allproducts})

@login_required()
def insertProduct(request, id=0):
    if id == 0:
        if request.method == 'GET':
            form = ProductForm()
            return render(request, 'shop/insertproduct.html', {'form': form})
        else:
            form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listproduct')
    else:
        if request.method == 'GET':
            product = Product.objects.get(id=id)
            form = ProductForm(instance=product)
            return render(request, 'shop/insertproduct.html', {'form': form})
        else:
            product = Product.objects.get(id=id)
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('/listproduct')


@login_required()
def deleteProduct(request, id=0):
    Product.objects.filter(id=id).delete()

    return redirect('/listproduct')
