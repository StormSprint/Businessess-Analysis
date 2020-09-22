from django.contrib import admin
from django.contrib.admin.models import LogEntry

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from BAS.base_admin import FilterAdmin, BaseAdmin
from .models import Contract, Product, Resource, Allowance


class ContractResource(resources.ModelResource):

    class Meta:
        model = Contract
        import_id_fields = ('contract_id', )


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product
        import_id_fields = ('product_id', )


class ResourceResource(resources.ModelResource):

    class Meta:
        model = Resource
        import_id_fields = ('product_id', )


class AllowanceResource(resources.ModelResource):

    class Meta:
        model = Allowance
        import_id_fields = ('number', )


# Register your models here.
@admin.register(Contract)
class ContractAdmin(FilterAdmin):
    """
    合同信息表
    包含字段：
        1、合同基本信息：合同编码('contract_id')、合同金额('contract_amount')、合同签订时间('contract_date')、合同到期时间('contract_expire')；
        2、客户信息：客户名称('customer_name')、客户地址(展示页面不显示，编辑页面显示)、客户联系人（展示页面不显示，编辑页面显示）、联系电话（展示页面不显示，编辑页面显示）
        3、客户经理信息：客户经理（'staff'）、支局（行客中心）（'group'）。暂定客户经理和支局可以为空。
        4、备注（'remark'）
        5、创建时间（展示页面不显示，编辑页面显示，不可编辑）、更新时间（'update_time'，不可编辑）
    """
    resources = ContractResource
    list_display = ('contract_id', 'contract_amount', 'contract_date', 'contract_expire',
                    'customer_name', 'staff', 'group', 'update_time', 'remark')
    search_fields = ('contract_id', 'customer_name', 'staff')
    list_per_page = 20
    actions_on_top = True
    raw_id_fields = ('staff',)
    # fieldsets = (
    #     ('合同基本信息', {
    #         'fields': ('contract_id', 'contract_amount',
    #                    'contract_date', 'contract_expire',)
    #     }),
    #     ('客户信息', {
    #         'fields': ('customer_name', 'linkman', 'phone', 'address')
    #     }),
    #     ('客户经理', {
    #         'fields': ('staff', 'group')
    #     }),
    #     ('备注', {
    #         'classes': ('collapse',),
    #         'fields': ('remark', )
    #     }),
    # )

    # exclude = ('staff', )
    #
    # def get_queryset(self, request):
    #     qs = super(ContractAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         ContractAdmin.exclude = ()
    #         return qs
    #     elif request.user.groups.all():
    #         ContractAdmin.exclude = ()
    #         return qs.filter(group__in=request.user.groups.all())
    #     else:
    #         return qs.filter(staff=request.user)


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    """
    专线信息表
    包含字段：
        1、专线信息：专线号、状态、带宽、计费金额、产品类型、地域标识；
        2、客户信息：客户名称、安装地址、联系人、联系电话、合同编码（外键）;
        3、客户经理信息：客户经理（外键）、支局(行客中心)（外键）
        4、备注
        5、创建时间、更新时间
    """
    # resources = ProductResource
    list_display = ('product_id', 'status', 'bandwidth', 'price',
                    'product_type', 'area', 'staff', 'group', 'update_time', 'remark')
    search_fields = ('product_id', 'status', 'staff', 'group')
    list_per_page = 20
    actions_on_top = True
    raw_id_fields = ('contract_id', 'staff')

    # fieldsets = (
    #     ('专线信息', {
    #         'fields': ('product_id', 'status', 'bandwidth', 'price', 'product_type', 'area')
    #     }),
    #     ('客户信息', {
    #         'fields': ('customer_name', 'address', 'linkman', 'phone', 'contract_id')
    #     }),
    #     ('客户经理信息', {
    #         'fields': ('staff', 'group')
    #     }),
    #     ('备注', {
    #         'fields': ('remark', )
    #     })
    # )


@admin.register(Allowance)
class AllowanceAdmin(FilterAdmin):
    """
    交叉补贴信息表
    包含字段：
        1、基本信息：设备号、计费金额
        2、关联信息：专线号（外键）、客户经理（外键）、支局（行客中心）（外键）
        3、备注
        3、创建时间、更新时间
    """
    list_display = ('number', 'price', 'product_id', 'staff', 'group', 'update_time', 'remark')
    search_fields = ('number', 'product_id', 'staff')
    list_per_page = 20
    actions_on_top = True
    raw_id_fields = ('staff', 'product_id')

    # fieldsets = (
    #     ('基本信息', {
    #         'fields': ('number', 'price')
    #     }),
    #     ('关联信息', {
    #         'fields': ('product_id', 'staff')
    #     }),
    #     (None, {
    #         'fields': ('remark', )
    #     })
    # )


@admin.register(Resource)
class ResourceAdmin(ImportExportActionModelAdmin):
    """
    资源信息表
    包含字段：
        1、基本信息：专线号、套餐带宽、实际带宽
        2、备注
        3、创建时间、更新时间
    """
    list_display = ('product_id', 'bandwidth', 'true_bandwidth')
    search_fields = ('product_id', )
    list_per_page = 20
    actions_on_top = True
    raw_id_fields = ('product_id', )

    fieldsets = (
        ('基本信息', {
            'fields': ('product_id', 'bandwidth', 'true_bandwidth')
        }),
        (None, {
            'fields': ('remark', )
        })
    )


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']