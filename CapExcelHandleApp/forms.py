from django import forms
from CapExcelHandleApp.models import Employee
from django.core.validators import validate_email
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('eid','ename','eemail','econtact')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

    # def clean_username(self):
    #     user=self.cleaned_data['username']
    #     try:
    #         match=User.objects.get(username=user)
    #     except:
    #         self.cleaned_data['username']
    #     raise forms.ValidationError("Username already Exist")
    #
    # def clean_email(self):
    #     email=self.cleaned_data['email']
    #     try:
    #         mt=validate_email(email)
    #     except:
    #         return forms.ValidationError("Email is not in correct format")
    #     return email
    #
    # def clean_confirm_password(self):
    #     pas=self.cleaned_data['password']
    #     cpas=self.cleaned_data['confirm_password']
    #     MIN_LENGTH=8
    #     if pas and cpas:
    #         if pas!=cpas:
    #             raise forms.ValidationError("password and confirm password not matched")
    #         else:
    #             if len(pas)<MIN_LENGTH:
    #                 raise forms.ValidationError("password should have atleast %d characters"%MIN_LENGTH)
    #             if pas.isdigit():
    #                 raise forms.ValidationError("Password should not all numeric")
