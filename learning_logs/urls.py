from django.urls import path
from . import views    #在当前目录导入视图
#数据库中的视图:把多个表连接起来形成一个新的表
 
app_name = 'learning_logs'
 
#urlpatterns包含了应用程序learning_logs中请求的网页
urlpatterns = [
    #path的参数:第一个参数是路由(一个匹配URL的准则)，通常可为'';
    #第二个参数指定了要调用的视图函数,视图函数接受请求中的信息,准备好生成网页所需的数据,再将这些数据发送给浏览器
    #第三个参数是将这个URL模式的名称指定为index,这样每当需要提供到这个主页的链接时我们可以直接使用这个名称而不用编写URL
    #主页
    path('',views.index,name='index'),
   
    #URL与该模式匹配的请求都将交给views.py中的函数topics()处理
    path('topics/',views.topics,name='topics'),
        
    #特定主题的详细页面:http://localhost:8000/topics/1/
    #/(?P<topic_id>\d+)/与包含在两个斜杠内的整数匹配(如上,为1),并将这个整数存储在一个名为topic_id的实参中
    #()括号捕获了URL中的值,?P<topic_id>将匹配的值存储到topic_id中;
    #\d+与包含在两个斜杆内的任何数字都匹配,不管这个数字为多少位
    #当发现URL与这个模式匹配时,Django将调用视图函数topic(),并将topic_id传给它
 
    path('topics/(?P<topic_id>\d+)/',views.topic,name='topic'),
    
    #用于添加新主题的网页
    path('new_topic/',views.new_topic,name='new_topic'),
    
    #用于添加新条目的页面
    path('new_entry/(?P<topic_id>\d+)/',views.new_entry,name='new_entry'),
    
    #用于编辑条目的页面
    path('edit_entry/(?P<entry_id>\d+)/',views.edit_entry,name='edit_entry')
]
"""两个urls.py的区别是，前者添加了应用程序的所有URL，后者指定应用程序各URL对应的视图"""