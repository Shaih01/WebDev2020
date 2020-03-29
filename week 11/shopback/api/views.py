from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from api.models import Product, Category
from django.http.request import HttpRequest


def get_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id).to_json()
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.to_json())


def get_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id).to_json()
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())


def get_categories(request):
    categories = Category.objects.all()
    category_json = [category.to_json() for category in categories]
    return JsonResponse(category_json, safe=False)


def get_category_products(request, need_category_id):
    products = Product.objects.all()
    out = []

    for i in products:
        if i.category_id.id == need_category_id:
            out.append(i.to_json())
        else:
            return JsonResponse({'error'})

    return JsonResponse(out, safe=False)
