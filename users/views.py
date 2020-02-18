from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
 
def logout_view(request):
    '''注销用户'''
    #直接调用django.contrib.auth中的Logout函数注销用户
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index")) #执行注销后就重新定向到主页

def register(request):
    '''注册新用户'''
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        #检查用户输入的数据是否有效:是否包含非法字符,输入的两个密码是否相同
        #以及用户有没有试图做恶意的事
        if form.is_valid():
            #save返回新创建的用户对象
            new_user = form.save()
            #用户注册时被要求输入密码两次,当表单是有效时两个密码相同,所以任取其中一个:password1
            #用户名和密码无误时authenticate将返回一个通过了身份验证的用户对象
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            #login登录函数,需要一个HttpRequest对象和一个用户对象
            login(request,authenticated_user)
            #定向到主页
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request,'users/register.html',context)