from django import forms
from tinymce.widgets import TinyMCE

from events.models import Event


class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(mce_attrs={
        'menubar': True,
        "theme": "silver",
        'height': '350px',
        'width': '1000px',
    }), required=True)

    class Meta:
        model = Event
        fields = '__all__'
