from django import forms
from .models import AddModel


# creating a form
class AddForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = AddModel

        # specify fields to be used
        fields = [
            "description",
        ]