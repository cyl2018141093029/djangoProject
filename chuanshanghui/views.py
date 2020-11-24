#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your views here.
from django.db.models import F
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from chuanshanghui.models import FundRecord, Reimbursement, DpMembers, ActivityInfo, People, Department,Goodslist, Cooperation,Banner
from datetime import datetime, timedelta
from django import forms

from utils import constants
from utils import json_res
from .form import changeInfoForm, changePwdForm


name = "chuanshanghui"


def login(request):#登录
    if request.session.get('is_login', None):
        return redirect("/chuanshanghui/index/")

    if request.method == "GET":
        if 'usernum' in request.COOKIES and 'password' in request.COOKIES:
            usernum =request.COOKIES.get('usernum')
            password =request.COOKIES.get('password')
            checked = 'checked'
        else:
            usernum = ''
            checked = ''
            password=''
        return render(request,
                      'login.html',
                      {'usernum':usernum, 'checked':checked, 'password':password})

    elif request.method == "POST":
        usernum = request.POST.get('usernum')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        people = People.objects.filter(stu_num=usernum)

        if not people.exists():
            message = '账户不存在'
            return render(request, 'login.html', {'message': message, })


        person=people.last()

        if person.password == password:
            request.session['is_login'] = True
            request.session['person_num'] = person.stu_num
            request.session['person_name'] = person.stu_name
            response = redirect('/chuanshanghui/index/')
            if remember == 'on':
                response.set_cookie('usernum',usernum, expires=datetime.now() + timedelta(days=14))
                response.set_cookie('password',password,expires=datetime.now() + timedelta(days=14))
            return response
        else:
            message='密码错误'
            return render(request,'login.html',{'message': message,})


def index(request):#首页
    if not request.session.get('is_login', None):
        return render(request,'404.html')
    else:
        usernum = request.session.get('person_num')
        people = People.objects.filter(stu_num=usernum)
        person = people.last()
        return render(request,'index.html',{'person':person})

class index_banner(View):
    def get(self,request):
        banners = Banner.objects.values('image_url','article__act_num').annotate(
            article_title=F('article__act_name')).filter(is_delete=False)[:constants.SHOW_BANNER_COUNT]
        data = {'banners':list(banners)}
        return json_res.json_response(data=data)

def logout(request):#退出
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")

class userInfoView(View):#显示个人信息
    def get(self,request):
        if not request.session.get('is_login', None):
            return render(request, '404.html')
        usernum = request.session.get('person_num')
        people = People.objects.filter(stu_num=usernum)
        person = people.last()
        dpmember = (DpMembers.objects.filter(stu_num=usernum)).last()
        dpnum = dpmember.dp_num_id
        department = (Department.objects.filter(dp_num=dpnum)).last()
        return render(request,'info_user.html',{'person':person, 'dpmember':dpmember,'department':department})


def info_changePassword(request):#修改密码
    if not request.session.get('is_login', None):
        return render(request,'404.html')

    if request.method == 'POST':
        usernum = request.session.get('person_num')
        people = People.objects.filter(stu_num=usernum)
        person = people.last()
        changePwd_form = changePwdForm(request.POST)
        if changePwd_form.is_valid():
            changePwd_cd = changePwd_form.cleaned_data
            print(changePwd_cd['password'],person.password,changePwd_cd['new_password'],changePwd_cd['renew_password'])
            if changePwd_cd['password'] == person.password:
                if changePwd_cd['new_password'] == changePwd_cd['renew_password']:
                    if changePwd_cd['new_password'] != changePwd_cd['password']:
                        person.password = changePwd_cd['new_password']
                        person.save()
                        return HttpResponse('修改成功！')

                    else:
                        return render(request,'info_changePassword.html',{'message':'新密码应与旧密码不同！'})
                else:
                    return render(request,'info_changePassword.html',{'message':'两次输入密码不一致！'})
            else:
                return render(request,'info_changePassword.html',{'message':'原密码错误，请重新输入！'})
        else:
            return render(request,'info_changePassword.html',{'message':'表单无效，请重新输入！'})
    else:
        return render(request,'info_changePassword.html')

def info_changeInfo(request):#修改个人信息
    if not request.session.get('is_login', None):
        return render(request,'404.html')

    if request.method == 'POST':
        usernum = request.session.get('person_num')
        people = People.objects.filter(stu_num=usernum)
        person = people.last()
        changeInfo_form = changeInfoForm(request.POST)
        if changeInfo_form.is_valid():
            changeInfo_cd = changeInfo_form.cleaned_data
            if changeInfo_cd['renew_stucollege'] != '':
                person.stu_college = changeInfo_cd['renew_stucollege']
            if changeInfo_cd['renew_stumajor'] != '':
                person.stu_major = changeInfo_cd['renew_stumajor']
            person.stu_class = changeInfo_cd['renew_stuclass']
            person.stu_phone = changeInfo_cd['renew_stuphone']
            person.stu_qq = changeInfo_cd['renew_stuqq']
            person.stu_email = changeInfo_cd['renew_stuemail']
            person.save()
            return HttpResponse('修改成功')
        else:
            return render(request,'info_changeInfo.html',{'message':'修改失败'})
    else:
        usernum = request.session.get('person_num')
        people = People.objects.filter(stu_num=usernum)
        person = people.last()
        return render(request, 'info_changeInfo.html', {'person': person})

class FundApplyState(forms.Form):
    reim_to = forms.CharField(label="reim_to", max_length="30")
    fund_for_dp = forms.CharField(label="fund_for_dp", max_length="30")
    fund_for_act = forms.CharField(label="fund_for_act", max_length="200")
    fund_pincharge = forms.IntegerField(label="fund_pincharge")
    stu_name = forms.CharField(label="stu_name", max_length="8")
    reim_amount = forms.FloatField(label="fund_amount")
    fund_for_matt = forms.CharField(label="fund_for_matt", max_length="200")


def fundapply_check(request):
    usernum = request.session.get('person_num')
    people = People.objects.filter(stu_num=usernum)
    person = people.last()

    # 检验登陆状态
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")

    # 如果检验通过，则运行下面的代码

    obj = FundApplyState(request.POST)
    if request.method == "POST":
        # 获取前端POST过来的数据
        reim_to = request.POST.get("reim_to")
        fund_for_dp = request.POST.get("fund_for_dp")
        fund_for_act = request.POST.get("fund_for_act")
        fund_pincharge = request.POST.get("fund_pincharge")
        stu_name = request.POST.get("stu_name")
        reim_amount = request.POST.get("reim_amount")
        fund_for_matt = request.POST.get("fund_for_matt")

        # 实例化报账对象
        reimbursement = Reimbursement()
        reim_to_ = Department(dp_num=reim_to)
        # 处理reim_to字段
        reimbursement.reim_to = reim_to_
        # 处理fund_pincharge字段
        reimbursement.fund_pinchrage = fund_pincharge
        # 保存一个reimbursement记录
        reimbursement.save()

        # 实例化资金对象
        fundrecord = FundRecord()

        # 处理fund_for_dp字段
        # Department实例
        fund_for_dp_ = Department(dp_num=fund_for_dp)
        fundrecord.fund_for_dp = fund_for_dp_

        # 处理fund_for_act字段
        fund_for_act_ = ActivityInfo(act_num=fund_for_act)
        fundrecord.fund_for_act = fund_for_act_


        # 处理fund_for_matt字段
        fundrecord.fund_for_matt = fund_for_matt

        # 处理fund_amount字段
        fundrecord.fund_amount = reim_amount

        # 处理reim_to字段
        reim_to_ = Department(dp_num=reim_to)
        reim_num_ = Reimbursement(reim_to=reim_to_)
        fundrecord.reim_num = reim_num_.reim_num

        # 保存一条fundrecord记录
        fundrecord.save()

        ff_act = ActivityInfo.objects.get(act_num=fund_for_act)
        fund_for_act = ff_act.act_name
        dp = Department.objects.get(dp_num=fund_for_dp)
        fund_for_dp = dp.dp_name

        reim_to_dp = Department.objects.get(dp_num=reim_to)
        reim_to = reim_to_dp.dp_name

        dp_member = People.objects.get(stu_num=fund_pincharge)


        if dp_member.stu_name == stu_name:
            return render(request, "_fundapply_check.html", {"reim_to": reim_to,
                                                             "fund_for_dp": fund_for_dp,
                                                             "fund_for_act": fund_for_act,
                                                             "fund_pincharge": fund_pincharge,
                                                             "stu_name": stu_name,
                                                             "reim_amount": reim_amount,
                                                             "fund_for_matt": fund_for_matt,
                                                             'person': person
                                                             })
        else:
            return "部门成员身份验证不通过，请联系系统管理员进行身份验证。"



    else:
        return HttpResponse("页面找不到了 404")


def admin_add(request):
    usernum = request.session.get('person_num')
    people = People.objects.filter(stu_num=usernum)
    person = people.last()
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    return render(request, 'admin-add.html', {'person': person})


def admin_list(request):
    usernum = request.session.get('person_num')
    people = People.objects.filter(stu_num=usernum)
    person = people.last()
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    return render(request, "admin-list.html", {'person': person})


def fund_apply(request):
    usernum = request.session.get('person_num')
    people = People.objects.filter(stu_num=usernum)
    person = people.last()
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    else:
        return render(request, "fund_apply.html", {'person': person})


def money_add(request):
    usernum = request.session.get('person_num')
    people = People.objects.filter(stu_num=usernum)
    person = people.last()
    Goods__name = request.POST.get('Goodsname')
    Goods__price = request.POST.get('Goodsprice')
    Goods__qua = request.POST.get('Goodsqua')
    Goods__total = request.POST.get('Goodstotal')
    bei__zhu = request.POST.get('bei_zhu')
    fund__for_act = request.POST.get('fundfor_act')
    # 数据库操作
    result = Goodslist(Goods_name=Goods__name, Goods_price=Goods__price, Goods_qua=Goods__qua, Goods_total=Goods__total,beizhu=bei__zhu, fund_for_act=fund__for_act)
    if result:
        return render(request, 'money-add.html', {'result': 1, 'person': person})
    else:
        return HttpResponse('插入失败！')
        # return render(request, 'money-add.html', {'result': 2, 'person': person})


def money_list(request):
    return render(request, "money-list.html")




# 部门成员信息管理
def dpmembers_list(request):   # 展示部门成员信息
    all_dpm = DpMembers.objects.all()
    return render(request, 'dpmembers_list.html', context={'all_dpm': all_dpm})   # 传递到模板中的数据是dpmembers_list

def dpmembers_add(request):  # 增加新部门成员
    if request.method == "POST":
        stunum = request.POST.get('stu_num')
        dpm1 = DpMembers.objects.create(stu_num=stunum)
        dpnum = request.POST.get('dpnum')
        dpnum = chr(dpnum)    # 传入数据库有问题
        dpm2 = DpMembers.objects.create(dp_num_id=dpnum)
        stupost = request.POST.get('stupost')
        dpm3 = DpMembers.objects.create(stu_num_id=stupost)
        return redirect('/admin-list/')
    return render(request, 'dpmembers_add.html')


# 活动信息展示管理
def article_list(request):  # 展示活动信息列表
    all_article = ActivityInfo.objects.all().order_by('act_num')  # 获取活动信息（单表）;降序
    # dp = all_article.dp_num_id.dp_name
    # return render(request, 'article-list.html', {'all_article': all_article, 'dp':dp})  # 多表查询尝试
    return render(request, 'article_list.html', {'all_article': all_article})  # 暂时只能实现单表查询


def article_add(request):  # 新增
    if request.method == 'POST':   # post请求
        # 获取用户数据
        actname = request.POST.get('actname')  # 后一变量对应html文档name
        if not actname:  # 输入为空
            return render(request, 'article_add.html', {'error1': '活动标题不能为空'})
        else:
            act1 = ActivityInfo.objects.create(act_name=actname)  # 数据库列名=用户输入变量
            dpnum = request.POST.get('dpnum')
            if dpnum == "0":
                return render(request, 'article_add.html', {'error2': '请选择所在部门！'})
            else:
                act2 = ActivityInfo.objects.create(dp_num=dpnum)
                acttype = request.POST.get('acttype')
                if acttype == "0":
                    return render(request, 'article_add.html', {'error3': '请选择活动类型！'})
                else:
                    act3 = ActivityInfo.objects.create(act_type=acttype)
                    actheldtime = request.POST.get('actheldtime')
                    act4 = ActivityInfo.objects.create(act_held_time=actheldtime)
                    actheldloca = request.POST.get('actheldloca')
                    act5 = ActivityInfo.objects.create(act_held_loca=actheldloca)
                    actparticipant = request.POST.get('actparticipant')
                    act6 = ActivityInfo.objects.create(act_participant=actparticipant)
                    numberofplimit = request.POST.get('numberofplimit')
                    act7 = ActivityInfo.objects.create(numberofp_limit=numberofplimit)
                    actdetails = request.POST.get('actdetails')
                    if not actdetails:
                        return render(request, 'article_add.html', {'error8': '活动详情不能为空'})
                    else:
                        act8 = ActivityInfo.objects.create(act_details=actdetails)
                        return redirect('/article-list/')   # 重定向
    return render(request, 'article_add.html')  # get请求返回页面，页面中包含form表单


def article_details(request):   # 详情
    article = ActivityInfo.objects.get(act_num="20001")    # 获取活动信息（单表）;降序
    return render(request, 'article-list.html', {'article': article})  # 暂时只能实现单表查询


def article_read(request):
    usernum = request.session.get('person_num')
    people = People.objects.filter(stu_num=usernum)
    person = people.last()
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    return render(request, 'article_read.html')


# 部门对接管理
def cooperation_alist(request):   # 展示信息
    all_cooa = Cooperation.objects.all()
    return render(request, 'cooperation_alist.html', context={'all_coo': all_cooa})

def cooperation_blist(request):   # 展示信息
    all_coob = Cooperation.objects.all()
    return render(request, 'cooperation_blist.html', context={'all_coo': all_coob})

def cooperation_add(request):  # 增加任务
    return render(request, 'cooperation_add.html')

def cooperation_read(request):  # 查看详情
    return render(request, 'cooperation_read.html')