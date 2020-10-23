# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms  import PeopleForm
from .models import People

def index(request):
    people = People.objects.all()
    if request.method == 'Post'
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = PeopleForm()

        context = {
            'people':people,
            'form':form
        }
        return render(request,'index.html',context=context)

#另一种方法
#def index(request): #定义函数index，参数是request
    #people = People.objects.all() #通过People模型拿到所有的people数据
    #return render(request, 'index.html', context={'people':people}) #把数据放到context里传递到模板中
    #if request.method == 'Post'
        #form = PeopleForm(request.POST)
        #if form.is_valid():
            #cleaned_data = form.cleaned_data  #form.cleaned_data对象，是Form根据字段类型对用户提交的数据做完转换之后的结果
            #people = People()
            #people.stu_num = cleaned_data['stu_num']
            #people.stu_name = cleaned_data['stu.name']
            #people.stu_sex = cleaned_data['stu_sex']
            #people.password = cleaned_data['password']
            #people.stu_phone = cleaned_data['stu_phone']
            #people.stu_qq = cleaned_data['stu_qq']
            #people.stu_email = cleaned_data['stu_email']
            #people.stu_major = cleaned_data['stu_major']
            #people.stu_class = cleaned_data['stu_class']
            #people.stu_college = cleaned_data['stu_college']
            #people.save()
            #return HttpResponseRedirect(reverse('index'))  #reverse方法：可以用来拿到对应的URL
        #else:
            #form = PeopleForm()  #提交数据