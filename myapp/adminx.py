# from django.contrib import admin
# Register your models here.

import xadmin
from .models import Vmms,overTime
from xadmin import views
# 用户信息模块
from django.contrib.auth.models import User

# 车辆管理
class VmmsAdmin(object):
    # 数据展示及顺序
    list_display = ('carModel', 'VIN','engineNumber', 'recipient', 'sampleDate', 'returnDate','useTest','parkingLocation','transport', 'testProgress', 'remarks',)
    # 搜索数据
    search_fields =('carModel','VIN')
    # 数据筛选
    list_filter =('sampleDate', 'returnDate','testProgress',)
    # 数据及时编辑
    list_editable =('returnDate','parkingLocation','transport','testProgress',)
    # 显示数据详细
    # show_detail_fields =('carModel')
    # 不可修改的数据
    # readonly_fields =('VIN')

xadmin.site.register(Vmms,VmmsAdmin)

# 加班统计
class overTimeAdmin(object):

    list_display = ('overDate','startTime','endTime','duration','overTimeCause')
    # list_filter = ('duration')


xadmin.site.register(overTime,overTimeAdmin)

# class BaseSetting(object):
#     # 主题修改
#     enable_themes = False
#     use_bootswatch = False

#整体配置
class GlobalSettings(object):
    site_title = "众泰试验室管理系统"
    site_footer = "Disman开发"
    # base_template = 'xadmin/base_site.html'
    # menu_style = "accordion"    #菜单收起
#
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
