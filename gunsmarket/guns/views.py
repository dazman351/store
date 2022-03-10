from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Guns
from .cart import Cart
from .forms import CartAddProductForm
from django.core.paginator import Paginator



def search(request):
    search_query = request.GET.get('q')

    if search_query == "guns":
        return redirect('guns')

    else:
        sgun = Guns.objects.filter(name__icontains=search_query).order_by('-name')

    paginator = Paginator(sgun, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()
    if page_obj.has_previous():
        prev_url = '?page={}'.format(page_obj.previous_page_number())
    else:
        prev_url = ''

    if page_obj.has_next():
        next_url = '?page={}'.format(page_obj.next_page_number())
    else:
        next_url = ''

    return render(request, 'guns/guns.html', {
        'page_obj': page_obj,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    })

def guns(request):
    guns = Guns.objects.all()

    paginator = Paginator(guns, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()
    if page_obj.has_previous():
        prev_url = '?page={}'.format(page_obj.previous_page_number())
    else:
        prev_url = ''

    if page_obj.has_next():
        next_url = '?page={}'.format(page_obj.next_page_number())
    else:
        next_url = ''


    return render(request, 'guns/guns.html', {
        'page_obj': page_obj,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    } )


def product_detail(request, id):
    product = get_object_or_404(Guns,
                                id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'guns/description.html', {'product': product,
                                                        'cart_product_form': cart_product_form})



@require_POST
def cart_add(request, product_id):
    if request.user.is_authenticated:
        cart = Cart(request)
        product = get_object_or_404(Guns, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return redirect('cart_detail')
    else:
        return redirect('login')



def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Guns, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'guns/detail.html', {'cart': cart})

