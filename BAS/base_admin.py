from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin


class BaseAdmin(ImportExportActionModelAdmin):
    """
        用来针对queryset过滤当前用户的数据
    """
    def get_queryset(self, request):
        qs = super(BaseAdmin, self).get_queryset(request)
        #  判断是否为超级用户，超级用户可查看所有用户的内容
        if request.user.is_superuser:
            return qs
        # 判断加入了组（支局）的用户，能够查看当前组的所有内容，同时加入了多个组的，可以查看多个组的内容。
        elif request.user.groups.all():
            return qs.filter(group__in=request.user.groups.all())
        else:
            return qs.filter(staff=request.user)


class FilterAdmin(BaseAdmin):
    """
        扩展：普通用户不需要对关键字‘staff’进行编辑和显示，保存时自动保存当前登录的用户。
    """
    # 普通用户不显示staff（客户经理）这一关键字
    exclude = ('staff', )

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.groups.all():
            self.exclude = ()  # 超级用户可以对‘staff’进行编辑
        return super(FilterAdmin, self).get_queryset(request)

    # 对于普通用户，在进行数据的编辑时，不需要对客户经理这一关键字段进行编辑，自动添加当前登录用户。
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser or request.user.groups.all():
            return super(BaseAdmin, self).save_model(request, obj, form, change)
        else:
            obj.staff = request.user
            return super(BaseAdmin, self).save_model(request, obj, form, change)
