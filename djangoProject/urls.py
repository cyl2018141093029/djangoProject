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

# from django.conf.urls import url
from django.contrib import admin
from django.urls import path
admin.autodiscover()
# from chuanshanghui.views import index  # 首页链接新增行

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$',index, name='index'),   # 首页链接新增行
    # url('admin/', admin.site.urls),   # 首页链接新增行
]
