from django import forms

from mall.models import Cloth


class ClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = "__all__"

