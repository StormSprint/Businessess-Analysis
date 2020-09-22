from django.shortcuts import render
from django.db.models import Sum
from .analysis import contractAnalysis
from .models import Expiration
from Business.models import Product
# Create your views here.


def index(requests):
    # 专线数量
    busniess_count = Product.objects.count()

    # 本月收入（应收/实收）
    income = float(Product.objects.aggregate(income=Sum('price'))['income'])

    # 合同预警
    # expiration_count = Expiration.objects.count()
    # expiration_amount = float(Expiration.objects.aggregate(amount=Sum('contract_amount'))['amount'])
    expiration_count = 3
    expiration_amount = 3000

    context = {
        'busniess_count': busniess_count,
        'income': income,
        'expiration_count': expiration_count,
        'expiration_amount': expiration_amount
    }

    return render(requests, 'templates/index.html', context=context)
