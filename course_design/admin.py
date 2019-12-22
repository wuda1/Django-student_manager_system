from django.contrib import admin
from .models import Course, Students, SC

# Register your models here.


class StudentsInfo(admin.TabularInline):  # 和继承admin.StackedInline一样，只是页面样式不同
    model = Students
    extra = 2


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def pk(self):
        return self.pk
    pk.short_description = '课程号'

    def cname(self):
        return self.cname
    cname.short_description = '课程名称'

    def ccredit(self):
        return self.ccredit
    ccredit.short_description = '课程学分'

    def isDelete(self):
        return self.isDelete
    isDelete.short_description = '是否删除'
    list_display = [pk, cname, ccredit, isDelete]
    list_filter = ['cname']
    search_fields = ['cname']
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True


@admin.register(Students)          # 使用装饰器注册管理器
class StudentsAdmin(admin.ModelAdmin):
    def pk(self):
        return self.pk
    pk.short_description = '学号'

    def sname(self):
        return self.sname
    sname.short_description = '姓名'

    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    # 设置页面列的名称
    gender.short_description = '性别'  # 设置字段显示的描述

    def sbirth(self):
        return self.sbirth
    sbirth.short_description = '生日'

    def sphone(self):
        return self.sphone
    sphone.short_description = '电话'

    def sdate(self):
        return self.sdate
    sdate.short_description = '入学日期'

    def saddress(self):
        return self.saddress
    saddress.short_description = '家庭地址'

    def isDelete(self):
        return self.isDelete
    isDelete.short_description = '是否删除'
    list_display = [pk, sname, gender, sbirth, sphone,
                    sdate, saddress, isDelete]
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 10
    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True


@admin.register(SC)          # 使用装饰器注册管理器
class SCAdmin(admin.ModelAdmin):
    def sno(self):
        return self.sno
    sno.short_description = '学号'

    def cno(self):
        return self.cno
    cno.short_description = '课程号'

    def grade(self):
        return self.grade
    grade.short_description = '成绩'
    list_display = [sno, cno, grade]
    list_filter = ['sno']
    search_fields = ['sno']
    list_per_page = 10
    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True