from django import forms
from registration_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
        widgets = {
            'student_id': forms.TextInput(attrs={'class': "wrap-input100 validate-input", 'class':"input100",}),
            'name': forms.TextInput(attrs={'class': "wrap-input100 validate-input",'class':"input100",}),
            'email': forms.TextInput(attrs={'class': "wrap-input100 validate-input",'class':"input100",}),
            'phone_no': forms.TextInput(attrs={'class': "wrap-input100 validate-input",'class':"input100",}),
        }
