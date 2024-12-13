from django import forms





class LoginForm( forms.Form ):
      email = forms.EmailField( label='E-Mail', max_length=100 )
      password = forms.CharField( label='Password', widget=forms.PasswordInput )
