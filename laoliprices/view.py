from django.shortcuts import render
from laoliprices.models import ProductPrices
from django.http import HttpResponseRedirect

# def hello(request):
#     return HttpResponse("Hello world ! ")

def homepage(request):
    return render(request, 'homepage.html')

def add_record(request):
    if request.method == 'POST':
        product_title = request.POST.get('item_name')
        product_spec = request.POST.get('item_desc')
        # quantity = request.POST.get('item_quantity')
        quantity = 1
        unit = request.POST.get('item_unit')
        unit_price = request.POST.get('item_price')

        which = ''
        if not product_title:
            which += ' ' + '品名'
        if not unit_price:
            which += ' ' + '单价'

        any = product_title and unit_price
        if not any:
            error_msg = which + ' 不能为空'
            return render(request, 'homepage.html', {'error_msg': error_msg})

        if quantity:
            total_price = int(unit_price) * int(quantity)
        else:
            total_price = 0

        if 'add' in request.POST:
            product_price = ProductPrices()

            product_price.product_title = product_title
            product_price.product_spec = product_spec
            product_price.quantity = quantity
            product_price.unit = unit
            product_price.unit_price = unit_price
            product_price.total_price = total_price

            product_price.save()
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

    any = product_title or product_spec or unit or unit_price
    if not any:
        error_msg = '请输入关键词'
        return render(request, 'query_page.html', {'error_msg': error_msg})

    # post_list = ProductPrices.objects.filter(product_title=product_title,
    #                                          product_spec=product_spec,
    #                                          unit=unit,
    #                                          unit_price=unit_price)
    post_list = ProductPrices.objects.filter(product_title__icontains=product_title)

    return render(request, 'query_page.html', {'error_msg': error_msg,
                                                 'post_list': post_list})