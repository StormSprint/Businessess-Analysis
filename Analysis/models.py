from django.db import models
from django.contrib.auth.models import User, Group

from Business.models import Contract


class Expiration(models.Model):
    contract_id = models.CharField(verbose_name='合同编码', max_length=32)
    contract_amount = models.DecimalField(verbose_name='合同金额', max_digits=9,
                                          decimal_places=2)
    contract_date = models.DateField(verbose_name='合同签订时间')
    contract_expire = models.DateField(verbose_name='合同到期时间')
    days = models.IntegerField(verbose_name='到期天数')
    remark = models.CharField(verbose_name='备注', max_length=128)

    staff = models.CharField(max_length=8, verbose_name='客户经理', blank=True, null=True)
    group = models.CharField(max_length=8, verbose_name='支局(行客中心)', blank=True, null=True)

    def __str__(self):
        return self.contract_id

    class Meta:
        verbose_name = verbose_name_plural = '合同到期预警'


class Abnormal(models.Model):
    product_id = models.CharField(max_length=32, verbose_name='专线号')
    area = models.CharField(max_length=8, verbose_name='地域标识')
    month = models.DateField(verbose_name='当前月份')
    billing_amount = models.DecimalField(verbose_name='计费金额', max_digits=9, decimal_places=2)
    payment_amount = models.DecimalField(verbose_name='出账金额', max_digits=9, decimal_places=2)
    allowance_amount = models.DecimalField(verbose_name='交叉补贴', max_digits=9, decimal_places=2)

    staff = models.CharField(max_length=8, verbose_name='客户经理', blank=True, null=True)
    group = models.CharField(max_length=8, verbose_name='支局(行客中心)', blank=True, null=True)

    remark = models.CharField(verbose_name='备注', max_length=128)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = verbose_name_plural = '收入异常列表'
