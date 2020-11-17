"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from chuanshanghui import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),  # 登录(系统默认的‘首页’)
    path('login/', views.login, name='login'),  # 登录（用于跳转的时候）
    path('index/', views.index),  # 首页
    path('logout/', views.logout),  # 登出
    path('userInfo/', views.userInfoView.as_view(), name='userInfo'),  # 个人中心
    path('info_changePassword/', views.info_changePassword, name='changePwd'),  # 个人中心-修改密码
    path('info_changeInfo/', views.info_changeInfo, name='changeInfo'),  # 个人中心-修改信息
    path('chuanshanghui/', include("chuanshanghui.urls", namespace='chuanshanghui')),

# 活动信息
    path('article_list/', views.article_list, name="article_list"),  # 列表展示
    path('article_add/', views.articles_add, name="article_add"),  # 新增
    # url(r'^article-list/$', views.article_delete),   # 删除
    path('article_read/', views.article_details, name="article_read"),  # 展开详细信息

    # 部门成员信息
    path('admin_list/', views.dpmembers_list,name="admin_list"),  # 列表展示
    path('admin_add/', views.dpmembers_add ,name ="admin_add"),   # 新增
    # url(r'^admin-list/$', views.dpmembers_delete)   # 删除
    # path('admin-list/', views.dpmembers_details)   # 展开详细信息

    # 部门对接 新页面需要增加base文件
    path('cooperation_alist/', views.cooperation_alist, name="cooperation_alist"),  # 列表展示发布任务
    path('cooperation_blist/', views.cooperation_blist, name="cooperation_blist")  # 列表展示接收任务
    # url(r'^cooperation-add/$', views.cooperation_add),  # 新增
    # url(r'^cooperation-alist/$', views.cooperation_delete),   # 删除
    # url(r'^cooperation-blist/$', views.cooperation_delete),   # 删除
    # url(r'^cooperation-read/$', views.cooperation_details)  # 展开详细信息
]