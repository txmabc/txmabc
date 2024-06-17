from django.db import models


class UserGroup(models.Model):
    title = models.CharField(max_length=50, verbose_name="会员组名称", null=True)
    sort = models.IntegerField(default=0, verbose_name="排序")
    page_list = models.TextField(verbose_name="页面权限")
    cate_list = models.TextField(verbose_name="栏目权限")
    pagelever = models.CharField(max_length=50, verbose_name="权限设置", null=True)
    pagelock = models.SmallIntegerField(verbose_name="审核设置", default=0)

    def __str__(self):
        return self.title


class User(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50, verbose_name="用户名")
    upass = models.TextField(max_length=256, verbose_name="密码")
    umoney = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name="余额")
    uemail = models.CharField(blank=True, null=True, max_length=50, verbose_name="邮箱")
    uface = models.CharField(blank=True, null=True, max_length=255, verbose_name="头像")
    group = models.ForeignKey(UserGroup, related_name='users', on_delete=models.SET_DEFAULT, default=0, verbose_name="会员组")
    islock = models.IntegerField(default=0, verbose_name="状态")
    regdate = models.DateTimeField(auto_now_add=True, verbose_name="注册日期")
    regip = models.CharField(blank=True, null=True, max_length=50, verbose_name="注册IP")
    lastlogindate = models.DateTimeField(blank=True, null=True, verbose_name="上次登录日期")
    lastloginip = models.CharField(blank=True, null=True, max_length=50, verbose_name="上次登录IP")
    logintimes = models.IntegerField(default=0, verbose_name="登录次数")

    def __str__(self):
        return self.uname


# 机构
class Institution(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    title = models.CharField(max_length=50, verbose_name="机构名称")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="会员")
    name = models.CharField(max_length=50, verbose_name="联系人")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    sort = models.IntegerField(default=0, verbose_name="排序")
    status = models.IntegerField(default=0, verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.title


# 老师
class Teacher(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=50, verbose_name="老师姓名", null=True)
    mobile = models.CharField(max_length=11, verbose_name="联系方式")
    institution = models.ForeignKey(Institution, related_name='teachers', on_delete=models.CASCADE, verbose_name="机构")
    sort = models.IntegerField(default=0, verbose_name="排序")
    status = models.IntegerField(default=0, verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", null=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", null=True)

    def __str__(self):
        return self.name


# # 班级
# class Grade(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name="ID")
#     title = models.CharField(max_length=50, verbose_name="班级名称", null=True)
#     institution = models.ForeignKey(Institution, related_name='grades', on_delete=models.CASCADE, verbose_name="机构")
#     teacher = models.ManyToManyField(Teacher)
#     remark = models.CharField(max_length=255, verbose_name="备注", null=True, blank=True)
#     sort = models.IntegerField(default=0, verbose_name="排序")
#     status = models.IntegerField(default=0, verbose_name="状态")
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
#
#     def __str__(self):
#         return self.title
