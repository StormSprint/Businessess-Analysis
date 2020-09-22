import datetime
from Business.models import Contract
from .models import Expiration


def contractAnalysis():
    """
    计算合同库中合同时间是否小于120天，如果小于120天，则预警。
    """
    # 先删除Expiration表中的数据
    if Expiration.objects.all():
        for e in Expiration.objects.all():
            e.delete()

    # 读取Contract表中的日期信息，计算到期时间。
    for contract in Contract.objects.all():
        days = (contract.contract_expire - datetime.date.today()).days
        if days <= 120:
            new = Expiration(contract_id=contract.contract_id, contract_amount=contract.contract_amount,
                             contract_date=contract.contract_date, contract_expire=contract.contract_expire,
                             days=days, staff=contract.staff, group=contract.group)
            new.save()

    print('complate!')


if __name__ == "__main__":
    contractAnalysis()
