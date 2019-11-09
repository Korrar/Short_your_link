from django import forms
from url.models import Links

class UrlForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url_link'].widget.attrs.update(size='60')
    class Meta:
        model = Links
        url = forms.URLField()
        widget = forms.Textarea(attrs={'style': "resize: 50"}),
        exclude = ('url_shorted_link',)

