from django.db import models

# Create your models here.


class SysUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    avatar = models.CharField(max_length=255, null=True, verbose_name="用户头像")
    email = models.EmailField(max_length=50, null=True, verbose_name="用户邮箱")
    phonenumber = models.CharField(max_length=11, null=True, verbose_name="用户手机")
    login_date = models.DateTimeField(null=True, verbose_name="登录时间")
    status = models.BooleanField(null=True, verbose_name="用户状态")
    create_time = models.DateTimeField(null=True, verbose_name="创建时间")
    update_time = models.DateTimeField(null=True, verbose_name="更新时间")
    remask = models.CharField(max_length=255, null=True, verbose_name="备注")

    class Meta:
        db_table = "sys_user"
        verbose_name = "用户表"
