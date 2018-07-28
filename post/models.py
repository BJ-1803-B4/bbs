from django.db import models

from user.models import User


# 帖子管理
class PostManager(models.Manager):
    def all(self):
        return super().all().filter(is_delete=False)

    def create_post(self, title, content_html, content_str):
        post = self.model()
        post.title = title
        post.content_html = content_html
        post.content_str = content_str
        post.save()
        return post

    # 在这里添加模型管理方法


# 帖子
class Post(models.Model):
    title = models.CharField(max_length=50)
    cont_html = models.TextField()
    cont_str = models.TextField()
    view_count = models.IntegerField()
    like_count = models.IntegerField()
    coll_count = models.IntegerField()
    comm_count = models.IntegerField()
    is_delete = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete=models.CASCADE含义：删除关联数据,与之关联也删除
    like = models.ManyToManyField(User, through='Like')
    collection = models.ManyToManyField(User, through='Collection')
    comment = models.ManyToManyField(User, through='Comment')

    objects = PostManager()


# 点赞
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_like = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)


# 收藏
class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_coll = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)


# 评论
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    cont_str = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


# 回复
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comm = models.ForeignKey(Comment, on_delete=models.CASCADE)
    cont_str = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)





