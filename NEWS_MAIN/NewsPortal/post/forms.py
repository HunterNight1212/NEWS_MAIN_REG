from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class FilterPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'category',
            'hat',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        hat = cleaned_data.get('hat')
        if hat is not None and len(hat) >= 30:
            raise ValidationError({'hat': 'Ограниение количества символов'})
        return cleaned_data


class CommonGroupForm(SignupForm):
    def save(self, request):
        user = super(CommonGroupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
