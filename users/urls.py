'''为应用程序users定义URL模式'''
 
from django.urls import path 
from django.contrib.auth.views import LoginView
from . import views
 
LoginView.template_name = 'users/login.html'
app_name = 'users'
 
urlpatterns =[
    #登录页面
    #导入视图login,使得登录页面的URL模式与'http://localhost:8000/users/login/'匹配
    #'template_name':'users/login.html'告诉Django去哪里查找我们将编写的模板
    #视图实参为login,使Django使用默认视图login,而不是views.login
    path('login/',LoginView.as_view(),name='login'),
    
    #注销功能
    path('logout/',views.logout_view,name="logout"),
    
    #注册页面
    path('register/',views.register,name='register'),
]
 