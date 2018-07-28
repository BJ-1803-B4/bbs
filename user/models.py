from django.db import models


class UserManager(models.Manager):
    def all(self):
        return super().all().filter(is_delete=False)

    def create_user(self, username, password, email):
        user = self.model()
        user.username = username
        user.email = email
        user.password = password
        return user

    # 在这里添加模型管理方法


class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField()
    is_delete = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        db_table = 'users'



