from django.contrib import admin
# Register your models here.

# 注册
from .models import People

# 自定义管理页面,属性说明,列表页属性:list_display、显示字段:list_filter、过滤字段:search_fields、
# 搜索字段:list_per_page、分页、添加、修改页属性：fields、属性的先后顺序：fieldsets、给属性分组  注意：fields与fieldsets不能同时使用


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('stu_num', 'stu_name', 'password', 'stu_sex', 'stu_phone', 'stu_qq',
                    'stu_email', 'stu_major', 'stu_class', 'stu_college')
    list_filter = ('stu_num', 'stu_name', 'password', 'stu_sex', 'stu_phone', 'stu_qq',
                   'stu_email', 'stu_major', 'stu_class', 'stu_college')
    search_fields = 'stu_name'
    # 添加、修改页属性
    fieldsets = (
        (None, {
            'fields': (
                'stu_num',
                ('stu_name', 'password', 'stu_sex'),
                ('stu_phone', 'stu_qq', 'stu_email'),
                ('stu_major', 'stu_class', 'stu_college'),
            )
        }),
    )


admin.site.register(People, PeopleAdmin)
