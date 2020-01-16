from django.shortcuts import render
from laoliprices.models import product_price
from django.http import HttpResponseRedirect

# def hello(request):
#     return HttpResponse("Hello world ! ")

def homepage(request):
    return render(request, 'homepage.html')
    
def add_record(request):
    if request.method == 'POST':
        product_title = request.POST['item_name']
        product_spec = request.POST['item_desc']
        quantity = request.POST['item_quantity']
        unit = request.POST['item_unit']
        unit_price = request.POST['item_price']

        which = ''
        if not product_title:
            which += ' ' + '品名'
        if not unit_price:
            which += ' ' + '单价'

        any_product = product_title and unit_price
        if not any_product:
            error_msg = which + ' 不能为空'
            return render(request, 'homepage.html', {'error_msg': error_msg})

        if quantity:
            total_price = int(unit_price) * int(quantity)
        else:
            total_price = 0

        p = product_price()
        p.product_title = product_title
        p.product_spec = product_spec
        p.quantity = quantity
        p.unit = unit
        p.unit_price = unit_price
        p.total_price = total_price

        p.save()
    print('******************here')
    return render(request, 'homepage.html')


def query_page(request):
    return render(request, 'query_page.html')

def query_record(request):
    if request.method == 'GET':
        product_title = request.GET.get('item_name')
        product_spec = request.GET.get('item_desc')
        unit = request.GET.get('item_unit')
        unit_price = request.GET.get('item_price')

    print('******************here')
    error_msg = ''

    any_product = product_title or product_spec or unit or unit_price
    if not any_product:
        error_msg = '请输入关键词'
        return render(request, 'query_page.html', {'error_msg': error_msg})

    # post_list = product_price.objects.filter(product_title=product_title,
    #                                          product_spec=product_spec,
    #                                          unit=unit,
    #                                          unit_price=unit_price)
    post_list = product_price.objects.filter(product_title__icontains=product_title)

    return render(request, 'query_page.html', {'error_msg': error_msg,
                                                 'post_list': post_list})