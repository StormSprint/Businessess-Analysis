from django.apps import AppConfig
import os

default_app_config = 'Business.BusinessConfig'


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class BusinessConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '业务信息'
