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
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    coll_count = models.IntegerField(default=0)
    comm_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete=models.CASCADE含义：删除关联数据,与之关联也删除

    objects = PostManager()

    class Meta:
        db_table = 'posts'


# 点赞
class Like(models.Model):
    is_list = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    like_mtm = models.ManyToManyField(User, through='LikeMTM')


# 收藏
class Collection(models.Model):
    is_coll = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    coll_mtm = models.ManyToManyField(User, through='CollectionMTM')


# 评论
class Comment(models.Model):
    cont_str = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    comm_mtm = models.ManyToManyField(User, through='CommentMTM')


# 回复
class Reply(models.Model):
    cont_str = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    reply_mtm = models.ManyToManyField(User, through='ReplyMTM')


# 点赞多对多
class LikeMTM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


# 收藏多对多
class CollectionMTM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


# 评论多对多
class CommentMTM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


# 回复多对多
class ReplyMTM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)





