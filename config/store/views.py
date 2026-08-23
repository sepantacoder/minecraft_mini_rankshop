from django.shortcuts import render, get_object_or_404,redirect
import requests
from django.conf import settings
from .models import Rank,Order


def home(request):
    ranks = Rank.objects.filter(published=True)
    context= {
        "ranks": ranks
    }
    return render(request, "store/home.html",context)
def buy(request, rank_id):
    rank = get_object_or_404(Rank, id=rank_id)

    if request.method == "POST":
        username = request.POST.get("username")
        phone = request.POST.get("phone")

        order = Order.objects.create(
            rank=rank,
            username=username,
            phone=phone,
            amount=rank.price,
            commission=rank.price * 20 // 100
        )
        

        return render(request, "store/payment.html", {
            "order": order
        })

    return render(request, "store/buy.html", {
        "rank": rank
    })


def start_payment(request):
    order_id = request.session.get("order_id")

    if not order_id:
        return redirect("home")

    order = get_object_or_404(Order, id=order_id)

    merchant_id = settings.ZARINPAL_MERCHANT_ID

    if not merchant_id:
        return render(request, "store/payment.html", {
            "order": order,
            "error": "Merchant ID هنوز تنظیم نشده است."
        })

    return render(request, "store/payment.html", {
        "order": order
    })
def sql(request):
    selled=Order.objects.all().order_by("-id")
    context={
        "selled":selled,
    }
    return render(request,"store/sql.html",context)
def final(request,rank_id):
    rank=get_object_or_404(Order,id=rank_id)
    context={
        "rank":rank
    }
    return render (request,"store/final.html",context)