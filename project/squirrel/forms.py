from django.forms import ModelForm

from .models import Squirrel

class UpdateForm(ModelForm):
    class Meta:
        model=Squirrel
        fields = [
                'Latitude',
                'Longitude',
                'Unique_ID',
                'Shift',
                'Date',
                'Age',
        ]

