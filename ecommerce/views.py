from django.shortcuts import render, get_object_or_404
from .models import Product
from paymentsystem.models import UserDetail
from django.contrib import messages

# Create your views here.
def allproducts(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'ecommerce/products.html', context)


def productdetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product' : product,
    }
    return render(request, 'ecommerce/single-product.html', context)

def pay(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'ecommerce/confirm.html', context)


def confirm(request, pk):
    product = get_object_or_404(Product, pk=pk)
    price = product.price
    if request.method == 'POST':
        try:
            phonenumber = request.POST.get('phonenumber')
            userdetail = get_object_or_404(UserDetail, phonenumber=phonenumber)
        except:
            messages.error(request,"Ensure you fill your phone number and form appropriately.")
        pin = request.POST.get('pin')
        cardnum = request.POST.get('card_number')
        cvv = request.POST.get('card_code')
        expirationmonth = request.POST.get('expmonth')
        expirationyear = request.POST.get('expyear')
        emailaddress = request.POST.get('email')
        name = request.POST.get('name')
        zipcode = request.POST.get('zip_code')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        useraddress = address + city + state
        
        print(type(userdetail.maximumtransaction))
        print(type(userdetail.minimumtransaction))
        print(type(product.price))
        
        if userdetail.maximumtransaction < product.price:
            msg = "Sorry, Transaction not possible. Fraudulent status is more than average.(System detected inconsistent transaction amount)"
            return render(request, 'ecommerce/machine.html', {'msg':msg})
        elif userdetail.minimumtransaction > product.price:
            msgs = "Sorry, Transaction not possible. Fraudulent status is more than average. (System detected inconsistent transaction amount)"
            return render(request, 'ecommerce/machine.html', {'msgs':msgs})
        elif userdetail.password1 != pin:
            msgx = "Sorry, Transaction not possible. Fraudulent status is more than average. (System detected pin mismatch)"
            return render(request, 'ecommerce/machine.html', {'msgx':msgx})      
        
        elif userdetail.cardnumber != cardnum:
            msgs = "Sorry, Transaction not possible. Fraudulent status is more than average. (System detected inconsistent card number)"
            return render(request, 'ecommerce/machine.html', {'msgs':msgs})
        elif userdetail.expirymonth != expirationmonth:
            msgx = "Sorry, Transaction not possible. Fraudulent status is more than average. (System detected inconsistent expiration month)"
            return render(request, 'ecommerce/machine.html', {'msgx':msgx})     
        elif userdetail.expiryyear < expirationyear:
            msgs = "Sorry, Transaction not possible. Fraudulent status is more than average. (System detected inconsistent expiration year)"
            return render(request, 'ecommerce/machine.html', {'msgs':msgs})
        elif userdetail.emailaddress != emailaddress:
            msgx = "Sorry, Transaction not possible. Fraudulent status is more than average. (System detected inconsistent email address)"
            return render(request, 'ecommerce/machine.html', {'msgx':msgx})            
        # elif (userdetail.firstname + userdetail.lastname) not in name:
        #     msgs = "Sorry, Transaction not possible. Fraudulent status is more than average. (System detected inconsistent name)"
        #     return render(request, 'ecommerce/machine.html', {'msgs':msgs})
        elif userdetail.zipcode != zipcode:
            msgx = "Sorry, Transaction not possible. Fraudulent status is more than average. (System detected inconsistent zip code)"
            return render(request, 'ecommerce/machine.html', {'msgx':msgx})         
        elif userdetail.address not in useraddress:
            msgx = "Sorry, Transaction not possible. Fraudulent status is more than average. (System detected inconsistent user address)"
            return render(request, 'ecommerce/machine.html', {'msgx':msgx})       
          
        else:
            norm = "Success"
            return render(request, 'ecommerce/machine.html',{'norm':norm})
    context = {
        'price':price,
    }
    return render(request, 'ecommerce/machine.html',context)