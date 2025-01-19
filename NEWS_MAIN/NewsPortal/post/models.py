from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reit = models.IntegerField(default=0)

    def update_rating(self):
        if self.user == Post.author:
            self.reit += int(Post.reit * 3)
        self.reit.save()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_news = models.BooleanField(default=True)  # True - статья False - новость
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    hat = models.CharField(max_length=100)
    text = models.TextField()
    reit = models.IntegerField(default=0)

    def like(self):
        reit = self.reit
        reit += 1
        reit.save()

    def dislike(self):
        reit = self.reit
        reit -= 1
        reit.save()

    def preview(self):
        return self.text[:125] + '...'

    def __str__(self):
        return f'{self.hat.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    reit = models.IntegerField(default=0)


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
