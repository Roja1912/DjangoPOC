from users.models import User
from django.contrib.auth.forms import AuthenticationForm, \
    PasswordChangeForm



from django import forms
from django.contrib.auth.forms import UserCreationForm


class ClientAgentForm(UserCreationForm):
    print("111111333333333333")
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Password Confirmation",
                                widget=forms.PasswordInput, required=False,
                                help_text="Enter the same password as above, for verification.",)
    username = forms.CharField(label="Email", required=False)
    email = forms.EmailField(label="Email", required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


#Login using class based views
class CustomLoginForm(AuthenticationForm):
    """
    CustomLoginForm class define login form fields
    """
    class Meta:
        model = User
        fields = ['username', 'password', ]

    def __init__(self, *args, **kwargs):
        """
        Add form-control to fields class
        :param args:
        :param kwargs:
        """
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


