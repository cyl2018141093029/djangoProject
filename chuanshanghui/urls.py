#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import path
import chuanshanghui.views as views

app_name = "chuanshanghui"
urlpatterns = [
    path('login/', views.login, name='login'),  # 登录（用于跳转的时候）
    path('index/', views.index, name='index'),  # 首页
    path('index_banner/',views.index_banner.as_view(), name='index_banner'),
    path('logout/', views.logout,name='logout'),  # 登出
    path('userInfo/', views.userInfoView.as_view(), name='userInfo'),  # 个人中心
    path('info_changePassword/', views.info_changePassword, name='changePwd'),  # 个人中心-修改密码
    path('info_changeInfo/', views.info_changeInfo, name='changeInfo'),  # 个人中心-修改信息
    path('fund_apply/', views.fund_apply, name="fund_apply"),
    path('fund_apply/_fundapply_check', views.fundapply_check, name='fund_apply_state_create'),
    path('fund_apply_state/', views.fundapply_check, name="fund_apply_state"),
    path('admin_list/', views.admin_list, name="admin_list"),
    path('admin_add/', views.admin_add, name="admin_add"),
    path('money_add/', views.money_add, name='money_add'),
    path('money_list/', views.money_list, name="money_list")
]
