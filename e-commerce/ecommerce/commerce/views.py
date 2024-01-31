from django.shortcuts import render
from django.http import HttpResponse

products = [{
    'id': 1,
    'price': '20$',
    'path': '0.jpg',
    'category':'jeans'
},
{
    'id': 2,
    'price': '30$',
    'path': '1.jpg',
    'category':'jeans'
},
{
    'id': 3,
    'price': '40$',
    'path': '2.jpg',
    'category':'jeans'
},
{
    'id': 4,
    'price': '20$',
    'path': '3.jpg',
    'category':'jeans'
},
{
    'id': 5,
    'price': '30$',
    'path': 's3.jpg',
    'category':'suit'
},
{
    'id': 6,
    'price': '40$',
    'path': 'b3.jpg',
    'category':'jeans'
},
{
    'id': 7,
    'price': '20$',
    'path': 'b5.jpg',
    'category':'jeans'
},
{
    'id': 8,
    'price': '30$',
    'path': 'b6.jpg',
    'category':'jeans'
},
{
    'id': 9,
    'price': '40$',
    'path': 's1.jpg',
    'category':'jeans'
}]

def hello(request):
    return render(request, 'index.html', {'products': products})

def category(request):
    return render(request, 'category.html', {'products': products})

def product_list(request, id):
    filtered_products = filter(lambda item: item['id'] == id, products)
    product_list = list(filtered_products)
    if product_list:
        return HttpResponse(f'Product: {product_list[0]["price"]}')
    else:
        return HttpResponse('Product not found')

def about_us(request):
    return render(request, 'about_us.html')
