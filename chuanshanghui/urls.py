#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import path
# from django.conf.urls import url
# from rest_framework import routers
from chuanshanghui.views import index, fundapply_check, admin_list, admin_add, fund_apply, money_add, money_list

# from django.contrib import admin

app_name = "chuanshanghui"
urlpatterns = [
    path('index/', index, name="index"),
    path('fund_apply/', fund_apply, name="fund_apply"),
    path('fund_apply/_fundapply_check', fundapply_check, name='fund_apply_state_create'),
    path('fund_apply_state/', fundapply_check, name="fund_apply_state"),
    path('admin_list/', admin_list, name="admin_list"),
    path('admin_add/', admin_add, name="admin_add"),
    path('money_add/', money_add, name='money_add'),
    path('money_list/', money_list, name="money_list")
]
