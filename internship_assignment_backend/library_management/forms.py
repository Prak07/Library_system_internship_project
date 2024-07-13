from django import forms


class EditForm(forms.Form):
    id=forms.CharField(label="id",max_length=20,widget=forms.TextInput(attrs={'readonly': 'readonly'}),initial=None)
    Title=forms.CharField(label="Title",max_length=20,initial=None)
    Author = forms.CharField(label="Author",max_length=20,initial=None)
    ISBN = forms.CharField(label="ISBN",max_length=20,initial=None)

class AddForm(forms.Form):
    Title=forms.CharField(label="Title",max_length=40)
    Author = forms.CharField(label="Author",max_length=30)
    ISBN = forms.CharField(label="ISBN",max_length=20)

