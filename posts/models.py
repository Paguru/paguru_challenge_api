from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):

    content = models.CharField(max_length=280)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    @property
    def author_name(self):
        return self.author.username
