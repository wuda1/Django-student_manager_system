from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Students, Course, SC, User

# Create your views here.


def index(request):
    return render(request, 'course_design/index.html')


def course(request):
    sid = request.GET.get('sid')
    if sid:
        print('sid=', sid)
        try:
            sname = Students.objects.filter(sno=sid)[0].sname
            sclist = SC.objects.filter(sno=sid)
            return render(request, 'course_design/stu_course.html',
                          {'sclist': sclist, 'sno': sid, 'sname': sname})
        except:
            return HttpResponse('学号错误')
    courseslist = Course.objects.all()
    return render(request, 'course_design/course.html', {'courses': courseslist})


def students(request):
    studentnumber = request.GET.get('studentnumber')
    if studentnumber:
        try:
            studentslist = Students.objects.filter(sno=studentnumber)
            print(studentslist)
            return render(request, 'course_design/students.html', {'students': studentslist})
        except:
            studentslist = Students.objects.all()
            return render(request, 'course_design/students.html', {'students': studentslist})
    studentslist = Students.objects.all()
    return render(request, 'course_design/students.html', {'students': studentslist})


def target(request):
    if request.method == 'POST':
        identification = request.POST.get('identification')
        studentnumber = request.POST.get('studentnumber')
        password = request.POST.get('password')
        print(studentnumber)
        print(password)
        if identification == 'student':
            try:
                pswd = User.objects.filter(username=studentnumber)[0].password
            except:
                return HttpResponse('用户名错误')
            if password == pswd:
                studentname = Students.objects.filter(sno='20'+studentnumber)[0].sname
                return render(request, 'course_design/target.html', {'studentname': studentname, 'sno': studentnumber})
            else:
                return HttpResponse('密码错误')
        else:
            return redirect('/admin/login/?next=/admin')
    return HttpResponse('不是正常请求')



def verifycode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色，宽，高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画面对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    font = ImageFont.truetype('C:/Windows/Fonts/Arial/arial.ttf', 40)
    # 构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    # 释放画笔
    del draw
    # 存入session,用于做进一步的验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')