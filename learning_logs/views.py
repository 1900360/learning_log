from django.shortcuts import render #render渲染:根据信息创建一个网页
from.models import Topic,Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
 
#request为请求对象
def index(request):
    #render的两个实参:原始请求对象 以及 一个可用于创建网页的模板
    #模板定义了网页的结构
    return render(request,'learning_logs/index.html')

@login_required  #检查用户是否登录
def topics(request):
    """显示所有主题"""
    
    #按属性date_added排序
    topics = Topic.objects.order_by('date_added')
 
    #将要发送给模板的上下文(字典型),其中的键是我们将在模板中用来访问数据的名称,
    #而值是我们要发送给模板的数据
    context = {'topics':topics}
    
    return render(request,'learning_logs/topics.html',context)

@login_required  #检查用户是否登录
def topic(request,topic_id):
    '''显示单个主题及其所有的条目'''
    
    #topic和entries被称为查询,向数据库查询特定的信息,可以先在Django shell中查询
    topic = Topic.objects.get(id=topic_id)
    
    #根据topic查询与其相关的所有条目（外键）
    entries = topic.entry_set.order_by('-date_added')#减号表示降序,使得先显示最新的条目
    
    context = {'topic':topic,'entries':entries}
    
    return render(request,'learning_logs/topic.html',context)

@login_required  #检查用户是否登录
def new_topic(request):
    '''添加新主题'''
 
    if request.method != 'POST':    #未提交数据则创建一个新表单
        form = TopicForm()          #创建一个新表单
    else:                           #对POST提交的数据进行处理
        form = TopicForm(request.POST)  #用户输入的数据存储在POST中
        if form.is_valid():         #核实用户是否填写了所有必不可少的字段且输入符合要求
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()             #保存表单到数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}         #将表单通过上下文字典发送给模板
    return render(request,'learning_logs/new_topic.html',context)

@login_required  #检查用户是否登录
def new_entry(request,topic_id):
    '''在特定的主题中添加新条目'''
    
    #从数据库根据主题的ID获取特定主题
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()    #未提交数据，创建一个空表单
    else:
        #根据POST提交的数据对数据进行处理
        form = EntryForm(data=request.POST)
        #表单内容是否有效
        if form.is_valid():
            #让Django创建新的条目对象，并存储到new_entry
            new_entry = form.save(commit=False)
            #将该条目与与正确的topic相关联
            new_entry.topic = topic
            #把该条目存储到数据库
            new_entry.save()
            #条目内容有效则创建新条目后回到主题页面
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    
    #GET请求或者POST请求的内容无效 则根据表单内容创建新页面
    context = {'form':form,'topic':topic}
    return render(request,'learning_logs/new_entry.html',context)

@login_required  #检查用户是否登录
def edit_entry(request,entry_id):
    '''编辑既有的条目'''
    entry = Entry.objects.get(id=entry_id)#获取需要修改的条目对象以及相关的主题
    topic = entry.topic
 
    if request.method != 'POST':
        #初次请求时创建一个表单并使用当前条目填充表单:显示条目的现有信息
        form = EntryForm(instance=entry)
    else:
        #POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        
        #表单内容是否有效
        if form.is_valid():
            form.save()
            #条目内容有效则创建新条目后回到主题页面
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
 
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)

