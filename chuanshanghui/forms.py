from django import forms   # 输出

from .models import People


class PeopleForm(forms.ModelForm):
    def clean_stu_qq(self):
        cleaned_data = self.cleaned_data['stu_qq']
        if not cleanede_data.isdigit():
            raise forms.ValidationError('请填写数字。')
        return int(cleaned_data)   # QQ号必须为纯数字的校验。clean_stu_qq是From会自动用来处理每个字段的方法。还可以定义clean_stu_num等

    class Meta:
        model = People
        fields = (
            'stu_num', 'stu_name', 'password', 'stu_sex', 'stu_phone', 'stu_qq',
            'stu_email', 'stu_major', 'stu_class', 'stu_college'
        )
