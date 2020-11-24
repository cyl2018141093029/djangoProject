#!/usr/bin/python #
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
    path('admin-list/', views.admin_list, name="admin_list"),
    path('admin-add/', views.admin_add, name="admin_add"),
    path('money_add/', views.money_add, name='money_add'),
    path('money_list/', views.money_list, name="money_list"),
    # 部门成员信息
    path('dpmembers_list/', views.dpmembers_list, name="dpmembers_list"),   # 列表展示
    path('dpmembers_add/', views.dpmembers_add, name="dpmembers_add"),    # 新增
    # path('dpmembers_list/', views.dpmembers_delete, name="dpmembers_delete"),   # 删除
    # path('dpmembers_list/', views.dpmembers_change, name="dpmembers_change"),   # 修改信息
    # path('dpmembers_read/', views.dpmembers_details, name="dpmembers_details"),   # 展开详细信息
    # 活动信息
    path('article_list/', views.article_list, name="article_list"),  # 列表展示
    path('article_add/', views.article_add, name="article_add"),  # 新增
    # path('article_list/', views.article_delete, name="article_add"),   # 删除
    path('article_read/', views.article_read, name="article_read"),  # 展开详细信息
    # 部门对接
    path('cooperation_alist/', views.cooperation_alist, name="cooperation_alist"),  # 列表展示发布任务
    path('cooperation_blist/', views.cooperation_blist, name="cooperation_blist"),  # 列表展示接收任务
    path('cooperation-add/', views.cooperation_add, name="cooperation_add"),  # 新增
    # path('cooperation-alist/', views.cooperation_delete, name=""),   # 删除
    path('cooperation_read/', views.cooperation_read, name="cooperation_read")  # 展开详细信息
]
