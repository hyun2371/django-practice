from django import forms
from shortener.models import ShortURL

class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ["original_url"]
        labels = { # 사용자에게 어떻게 보일지
            "original_url": "Redirect URL",
        }

