# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2/23/20'

import users
import xadmin
from xadmin.plugins.auth import UserAdmin, User
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _
from .models import UserProfile
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    site_title = "酷炫脑后台管理系统"
    site_footer = "CoolBrain"
    menu_style = "accordion"


xadmin.site.register(views.CommAdminView, GlobalSetting)


class UserProfileAdmin(UserAdmin):
    # user_count = 10
    # data_charts = {
    #     "user_count": {'title': u"Server Report", "x-field": 'id', "y-field": "",
    #                    "order": ('register_date',)},
    #    }
    pass


xadmin.site.unregister(User)
xadmin.site.register(UserProfile, UserProfileAdmin)