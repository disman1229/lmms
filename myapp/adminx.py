# from django.contrib import admin
# Register your models here.

import xadmin
from .models import Vmms
from xadmin import views

class VmmsAdmin(object):
    list_display = ('id', 'carModel','useTest','testProgress', 'VIN','engineNumber', 'mileage', 'recipient', 'sampleDate', 'returnDate', 'transport', 'parkingLocation', 'remarks')
    search_fields =('carModel','VIN')
    list_filter =('sampleDate', 'returnDate','testProgress',)



xadmin.site.register(Vmms,VmmsAdmin)


# class BaseSetting(object):
#     # 主题修改
#     enable_themes = False
#     use_bootswatch = False
#
class GlobalSettings(object):
    #整体配置
    site_title = "众泰试验室管理系统"
    site_footer = "Disman开发"
    # menu_style = "accordion"    #菜单收起
#
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)