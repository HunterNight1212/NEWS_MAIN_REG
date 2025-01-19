from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post


class PostFilter(FilterSet):
    time_if = DateFilter(field_name='time_create', lookup_expr='date__gte',
                         widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = {
            'hat': ['icontains'],
            'author': ['exact'],

        }
