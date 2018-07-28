from django.db import models


class PostManager(models.Manager):
    def all(self):
        return super().all().filter(is_delete=False)

    def create_post(self, title, content_html, content_str):
        post = self.model()
        post.title = title
        post.content_html = content_html
        post.content_str = content_str
        return post

    # 在这里添加模型管理方法


class Post(models.Model):
    title = models.CharField(max_length=50)
    content_html = models.TextField()
    content_str = models.TextField()
    is_delete = models.BooleanField(default=False)

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    objects = PostManager()
