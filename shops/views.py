from django.shortcuts import render,redirect
from .models import Product, Cart, CartItem
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to my shopping")


def home(request):
    return render(request, 'shops/home.html')


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shops/products.html', context=context)


def cart(request):
    if 'cart_id' not in request.session:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)

    cart_items = CartItem.objects.filter(cart=cart)
    context = {'cart_items': cart_items}
    return render(request, 'shops/cart.html', context=context)


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    if 'cart_id' not in request.session:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


def checkout(request):
    if 'cart_id' in request.session:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        return render(request, 'shops/checkout.html', {'cart_items': cart_items, 'total_price': total_price})
    else:
        # Handle error when there's no cart in session
        return redirect('cart')


def place_order(request):
    if request.method == 'POST':
        # Process the order details and create the order
        # You can access the form data using request.POST dictionary
        # Clear the cart and session once the order is placed
        if 'cart_id' in request.session:
            cart_id = request.session['cart_id']
            Cart.objects.get(id=cart_id).delete()
            del request.session['cart_id']

        # Redirect to a thank you page or order confirmation page
        return redirect('order_confirmation')
    else:
        # Handle error if place_order view is accessed via GET request
        return redirect('cart')