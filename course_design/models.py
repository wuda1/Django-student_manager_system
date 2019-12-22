from django.db import models

# Create your models here.


class Course(models.Model):                                 # 课程表
    cno = models.CharField(max_length=15, primary_key=True)
    cname = models.CharField(max_length=22)
    ccredit = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = '课程管理'           # admin界面显示模型的名称
        verbose_name_plural = '课程管理'    # admin界面显示模型的名称的复数
        db_table = 'course'      # 定义数据表名，推荐使用小写字母，如果不写数据表名默认为项目名小写_类名小写
        ordering = ['cno']        # 对象的默认排序字段，获取对象的列表时使用 ordering['id'] id按升序排列，ordering['-id'] id按降序排列，注意：排序会增加数据库开销


class Students(models.Model):                                   # 学生表
    sno = models.CharField(max_length=15, primary_key=True)
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sbirth = models.DateTimeField()
    sphone = models.CharField(max_length=11)
    sdate = models.DateTimeField()
    saddress = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = '学生管理'
        verbose_name_plural = '学生管理'
        db_table = 'students'      # 定义数据表名，推荐使用小写字母，如果不写数据表名默认为项目名小写_类名小写
        ordering = ['sno']


class SC(models.Model):
    sno = models.ForeignKey('Students', on_delete=models.CASCADE)
    cno = models.ForeignKey('Course', on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return self.sno_id

    class Meta:
        verbose_name = '成绩管理'
        verbose_name_plural = '成绩管理'
        db_table = 'sc'
        unique_together = ('sno', 'cno')
        ordering = ['sno']


class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.pk

    class Meta:
        db_table = 'user'      # 定义数据表名，推荐使用小写字母，如果不写数据表名默认为项目名小写_类名小写
        ordering = ['username']
