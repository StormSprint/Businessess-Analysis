from django.db import models
from django.contrib.auth.models import User, Group


class Contract(models.Model):
    """
    合同信息表
    包含字段：
        1、合同基本信息：合同编码、合同金额、合同签订时间、合同到期时间；
        2、客户信息：客户名称、客户地址、客户联系人、联系电话
        3、客户经理信息：客户经理、支局（行客中心）。暂定客户经理和支局可以为空。
        4、备注
        5、创建时间、更新时间
    """
    contract_id = models.CharField(max_length=32, unique=True, verbose_name='合同编码')
    contract_amount = models.DecimalField(verbose_name='合同金额',
                                          max_digits=8, decimal_places=2)
    contract_date = models.DateField(verbose_name='合同签订时间')
    contract_expire = models.DateField(verbose_name='合同到期时间')

    customer_name = models.CharField(max_length=128, verbose_name='客户名称')
    address = models.CharField(max_length=256, verbose_name='安装地址')
    linkman = models.CharField(max_length=128, verbose_name='联系人')
    phone = models.CharField(max_length=32, verbose_name='联系电话')

    staff = models.ForeignKey(to=User, verbose_name='客户经理',
                              on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(to=Group, verbose_name='支局(行客中心)',
                              on_delete=models.CASCADE, blank=True, null=True)

    remark = models.TextField(verbose_name='备注', blank=True, null=True)

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.contract_id

    class Meta:
        verbose_name = verbose_name_plural = '合同信息'

    def __unicode__(self):
        return u"%s" % self.contract_id


class Product(models.Model):
    """
    专线信息表
    包含字段：
        1、专线信息：专线号、状态、带宽、计费金额、产品类型、地域标识；
        2、客户信息：客户名称、安装地址、联系人、联系电话、合同编码（外键）;
        3、客户经理信息：客户经理（外键）、支局(行客中心)（外键）
        4、备注
        5、创建时间、更新时间
    """

    # 状态0，1，2，3，4分别对应状态正常、拆机、单停、双停、停机保号
    STATUS_NORMAL = 0
    STATUS_DELETE = 1
    STATUS_ONE_WAY_STOP = 2
    STATUS_STOP = 3
    STATUS_STORE_NUMBER = 4
    STATUS_OTHER = 5
    # 状态选项
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '拆机'),
        (STATUS_ONE_WAY_STOP, '单停'),
        (STATUS_STOP, '双停'),
        (STATUS_STORE_NUMBER, '停机保号'),
        (STATUS_OTHER, '其他'),
    )
    # 区域选项，0、1、2、3、4分别对应本地，市级，集团一站，其他分公司和测试
    AREA_IDENTIFIER_LOCAL = 0
    AREA_IDENTIFIER_MUNICIPAL = 1
    AREA_IDENTIFIER_OUTSKIRT = 2
    AREA_IDENTIFIER_GROUP = 3
    AREA_IDENTIFIER_TEST = 4
    AREA_IDENTIFIER_ITEMS = (
        (AREA_IDENTIFIER_LOCAL, '本地'),
        (AREA_IDENTIFIER_MUNICIPAL, '市级'),
        (AREA_IDENTIFIER_OUTSKIRT, '其他分公司'),
        (AREA_IDENTIFIER_GROUP, '集团一站'),
        (AREA_IDENTIFIER_TEST, '测试'),
    )

    # 产品类型选项
    TYPE_INTERNET = 0
    TYPE_MPLS = 1
    TYPE_MSTP = 2
    TYPE_IPRAN = 3
    TYPE_DIGIT = 4
    TYPE_IPVPN = 5
    TYPE_FIBER = 6
    TYPE_VPDN = 7
    TYPE_OTHER = 8
    TYPE_ITEMS = (
        (TYPE_INTERNET, '互联网'),
        (TYPE_MPLS, 'MPLS'),
        (TYPE_MSTP, 'MSTP'),
        (TYPE_IPRAN, 'IPRAN'),
        (TYPE_DIGIT, '数字中继'),
        (TYPE_IPVPN, 'IPVPN'),
        (TYPE_FIBER, '纯光纤出租'),
        (TYPE_VPDN, 'VPND'),
        (TYPE_OTHER, '其他'),
    )
    product_id = models.CharField(max_length=32, verbose_name='专线号', unique=True)
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='状态')
    bandwidth = models.PositiveIntegerField(verbose_name='带宽(M)', help_text='带宽单位为M')
    price = models.DecimalField(verbose_name='计费金额(￥)', max_digits=8, decimal_places=2)
    product_type = models.PositiveIntegerField(default=TYPE_OTHER,
                                               choices=TYPE_ITEMS, verbose_name='产品类型')
    area = models.PositiveIntegerField(default=AREA_IDENTIFIER_LOCAL, choices=AREA_IDENTIFIER_ITEMS,
                                       blank=True, verbose_name='地域标识')

    customer_name = models.CharField(max_length=128, verbose_name='客户名称')
    address = models.CharField(max_length=256, verbose_name='安装地址')
    linkman = models.CharField(max_length=128, verbose_name='联系人')
    phone = models.CharField(max_length=32, verbose_name='联系电话')
    contract_id = models.ForeignKey(to=Contract, on_delete=models.CASCADE,
                                    verbose_name='合同编码', blank=True, null=True, help_text='没有合同可不填')

    staff = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='客户经理', blank=True, null=True)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, verbose_name='支局(行客中心)', blank=True, null=True)

    remark = models.TextField(verbose_name='备注', blank=True, null=True)

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.product_id

    def __unicode__(self):
        return u"%s" % self.product_id

    class Meta:
        verbose_name = verbose_name_plural = '专线信息'


class Allowance(models.Model):
    """
    交叉补贴信息表
    包含字段：
        1、基本信息：设备号、计费金额
        2、关联信息：专线号（外键）、客户经理（外键）、支局（行客中心）（外键）
        3、备注
        3、创建时间、更新时间
    """
    number = models.CharField(max_length=32, verbose_name='设备号')
    price = models.DecimalField(verbose_name='计费金额', max_digits=7, decimal_places=2)

    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='专线号')
    staff = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='客户经理')
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, verbose_name='支局(行客中心)')

    remark = models.TextField(verbose_name='备注', blank=True, null=True)

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = verbose_name_plural = '交叉补贴'


class Resource(models.Model):
    """
    资源信息表
    包含字段：
        1、基本信息：专线号、套餐带宽、实际带宽
        2、备注
        3、创建时间、更新时间
    """
    product_id = models.OneToOneField(to=Product, on_delete=models.CASCADE, verbose_name='专线号')
    bandwidth = models.PositiveIntegerField(verbose_name='套餐带宽')
    true_bandwidth = models.IntegerField(verbose_name='实际带宽')

    remark = models.TextField(verbose_name='备注', blank=True, null=True)

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = verbose_name_plural = '资源信息'


# class Income(models.Model):
#     """
#     列收异常表
#     包含字段：专线号、日期、出账金额
#     """
#     sid = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='专线号')
#     date = models.DateTimeField(verbose_name='时间')  # -年-月-日
#     income = models.FloatField(verbose_name='出账金额')
#
#     class Meta:
#         verbose_name = verbose_name_plural = '历史列收信息'
#
