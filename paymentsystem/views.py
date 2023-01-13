from django.shortcuts import render, redirect
from .models import UserDetail
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        zipcode = request.POST.get("code")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        minamount = request.POST.get("minamount")
        maxamount = request.POST.get("maxamount")
        email = request.POST.get("email")
        account_name = request.POST.get("account_name")
        cardnumber = request.POST.get("cardnumber")
        date_2 = request.POST.get("date_2")
        month_2 = request.POST.get("month_2")
        year_2 = request.POST.get("year_2")
        userdetail = UserDetail(firstname=first_name,lastname=last_name,gender=gender,address=address,
        phonenumber=phone,zipcode=zipcode,password1=password1,password2=password2,minimumtransaction=minamount,
        maximumtransaction=maxamount,emailaddress=email,nameoncard=account_name,cardnumber=cardnumber,
        expiryday=date_2,expirymonth=month_2,expiryyear=year_2)
        message = "Your Details saved successfully, Thank you!!"
        userdetail.save()
        context = {
                'message' : message,
        }
        print(message)
        return render(request, 'paymentsystem/index.html',context)
    return render(request, 'paymentsystem/index.html',{'message':""})
