# Generated by Django 2.2.2 on 2019-09-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0002_auto_20190911_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.PositiveIntegerField(choices=[(0, '互联网'), (1, 'MPLS'), (2, 'MSTP'), (3, 'IPRAN'), (4, '数字中继'), (5, 'IPVPN'), (6, '纯光纤出租'), (7, 'VPND'), (8, '其他')], default=8, verbose_name='产品类型'),
        ),
    ]