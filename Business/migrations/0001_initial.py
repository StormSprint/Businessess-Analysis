# Generated by Django 2.2.2 on 2019-09-03 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_id', models.CharField(max_length=32, unique=True, verbose_name='合同编码')),
                ('contract_amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='合同金额')),
                ('contract_date', models.DateField(verbose_name='合同签订时间')),
                ('contract_expire', models.DateField(verbose_name='合同到期时间')),
                ('customer_name', models.CharField(max_length=128, verbose_name='客户名称')),
                ('address', models.CharField(max_length=256, verbose_name='安装地址')),
                ('linkman', models.CharField(max_length=128, verbose_name='联系人')),
                ('phone', models.CharField(max_length=32, verbose_name='联系电话')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='支局(行客中心)')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='客户经理')),
            ],
            options={
                'verbose_name': '合同信息',
                'verbose_name_plural': '合同信息',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=32, unique=True, verbose_name='专线号')),
                ('status', models.PositiveIntegerField(choices=[(0, '正常'), (1, '拆机'), (2, '单停'), (3, '双停'), (4, '停机保号'), (5, '其他')], default=0, verbose_name='状态')),
                ('bandwidth', models.CharField(help_text='带宽单位为M', max_length=16, verbose_name='带宽(M)')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='计费金额(￥)')),
                ('product_type', models.PositiveIntegerField(choices=[(0, '互联网'), (1, 'MPLS'), (2, 'MSTP'), (3, 'IPRAN'), (4, '数字中继'), (5, 'IPVPN'), (6, '其他')], default=6, verbose_name='产品类型')),
                ('area', models.PositiveIntegerField(blank=True, choices=[(0, '本地'), (1, '市级'), (2, '集团一站'), (3, '其他分公司'), (4, '测试')], default=0, verbose_name='地域标识')),
                ('customer_name', models.CharField(max_length=128, verbose_name='客户名称')),
                ('address', models.CharField(max_length=256, verbose_name='安装地址')),
                ('linkman', models.CharField(max_length=128, verbose_name='联系人')),
                ('phone', models.CharField(max_length=32, verbose_name='联系电话')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('contract_id', models.ForeignKey(blank=True, help_text='没有合同可不填', null=True, on_delete=django.db.models.deletion.CASCADE, to='Business.Contract', verbose_name='合同编码')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='支局(行客中心)')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='客户经理')),
            ],
            options={
                'verbose_name': '专线信息',
                'verbose_name_plural': '专线信息',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bandwidth', models.CharField(max_length=16, verbose_name='套餐带宽')),
                ('true_bandwidth', models.IntegerField(verbose_name='实际带宽')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Business.Product', verbose_name='专线号')),
            ],
            options={
                'verbose_name': '资源信息',
                'verbose_name_plural': '资源信息',
            },
        ),
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32, verbose_name='设备号')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='计费金额')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='支局(行客中心)')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Business.Product', verbose_name='专线号')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='客户经理')),
            ],
            options={
                'verbose_name': '交叉补贴',
                'verbose_name_plural': '交叉补贴',
            },
        ),
    ]
