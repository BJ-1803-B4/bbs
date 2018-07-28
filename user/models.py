from django.contrib.auth.hashers import make_password, check_password
from django.db import models


class UserManager(models.Manager):
    def all(self):
        return super().all().filter(is_delete=False)

    def create_user(self, username, password):
        user = self.model()
        user.username = username
        user.password = make_password(password)
        return user

    # 通过加密算法验证密码
    def valid_password(self, password):
        return check_password(password, self.model().password)

    # 在这里添加模型管理方法


class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=256)
    img = models.CharField(max_length=256)
    post_count = models.IntegerField(default=0)
    comm_count = models.IntegerField(default=0)
    follower_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        db_table = 'users'



