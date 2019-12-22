# Django-student_manager_system
实现了学生登陆，查看信息，admin后台管理
使用方法：
  首先pip install Django，然后配置database_course_design目录下的setting目录中的DATABASES,内容如下，本项目使用的是SQL server数据库，
  创建好数据库后，在cmd中进入到工程目录下执行迁移命令python manage.py migrate
  DATABASES = {
    'default': {
        'NAME': 'student',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': '127.0.0.1',
        'PORT': '1433',
        'USER': 'seq',
        'PASSWORD': '1234567890',
        'OPTIONS':{
             'driver': 'SQL Server Native Client 11.0',
         }
    }
}
  
  
  最后执行python manage.py runserver就可以启动项目
