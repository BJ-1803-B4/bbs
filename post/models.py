from django.db import models

from user.models import User


# 帖子管理
class PostManager(models.Manager):
    def all(self):
        return super().all().filter(is_delete=False)

    def create(self, title, content_html, content_str):
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
    timestamp = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    coll_count = models.IntegerField(default=0)
    comm_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    user = models.ForeignKey(User)

    likes = models.ManyToManyField(User, through='Like', related_name='likes')
    colls = models.ManyToManyField(User, through='Collection', related_name='colls')
    comms = models.ManyToManyField(User, through='Comment', related_name='comms')

    objects = PostManager()

    class Meta:
        db_table = 'posts'


# 点赞
class Like(models.Model):
    is_list = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uid = models.ForeignKey(User, related_name='like')
    pid = models.ForeignKey(Post, related_name='like')


# 收藏
class Collection(models.Model):
    is_coll = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uid = models.ForeignKey(User, related_name='coll')
    pid = models.ForeignKey(Post, related_name='coll')


# 评论
class Comment(models.Model):
    cont_str = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    uid = models.ForeignKey(User, related_name='comm')
    pid = models.ForeignKey(Post, related_name='comm')
    replys = models.ManyToManyField(User, through='Reply', related_name='replys')


# 回复
class Reply(models.Model):
    cont_str = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    uid = models.ForeignKey(User, related_name='reply')
    cid = models.ForeignKey(Comment, related_name='reply')

