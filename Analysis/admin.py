from django.contrib import admin
from .models import *
from BAS.base_admin import BaseAdmin
# Register your models here.

#修改网站主标题
admin.AdminSite.site_header = "政企专线管理平台"


@admin.register(Expiration)
class ExpirationAdmin(BaseAdmin):
    list_display = ('contract_id', 'contract_amount', 'contract_date',
                    'contract_expire', 'days', 'staff', 'group', 'remark')
    list_per_page = 20
    list_editable = ('remark', )


@admin.register(Abnormal)
class AbnormalAdmin(BaseAdmin):
    list_display = ('product_id', 'area', 'month', 'billing_amount',
                    'payment_amount', 'allowance_amount', 'staff', 'group', 'remark')
    list_per_page = 20
    list_editable = ('remark', )

