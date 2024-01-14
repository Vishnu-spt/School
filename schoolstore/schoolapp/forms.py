# schoolapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, Material, Course, Department

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'purpose', 'materials_provide']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'materials_provide': forms.CheckboxSelectMultiple,  # Use CheckboxSelectMultiple for the materials_provide field
        }

    PURPOSE_CHOICES = Order.PURPOSE_CHOICES  # Reference the choices from the model

    purpose = forms.ChoiceField(choices=PURPOSE_CHOICES)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Order.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Order.objects.filter(department_id=department_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set
