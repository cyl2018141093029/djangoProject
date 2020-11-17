from django import forms

class changeInfoForm(forms.Form):
    renew_stucollege = forms.CharField(max_length=30,required=False)
    renew_stumajor = forms.CharField(max_length=15,required=False)
    renew_stuclass = forms.IntegerField(required=False)
    renew_stuphone = forms.CharField(max_length=11,required=False)
    renew_stuqq = forms.CharField(max_length=20,required=False)
    renew_stuemail = forms.EmailField(required=False)

class changePwdForm(forms.Form):
    password = forms.CharField(max_length=12)
    new_password = forms.CharField(max_length=12)
    renew_password = forms.CharField(max_length=12)