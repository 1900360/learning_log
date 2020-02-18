from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    '''用户学习的主题'''
    
    #设置文本属性
    #text:由字符或文本组成的数据,需要存储少量的文本(名称、标题等)
    #CharField表示设置字符串字段,需要预设要最大长度
    text = models.CharField(max_length=200)
    
    #设置时间戳
    #DateTimeField用于记录日期和时间的数据
    #有两个bool型参数:auto_now表示保存时自动设置该字段为当前时间(最后修改日期)
    #auto_now_add表示当对象第一次被创建时自动设置该字段为当前日期(创建时间戳)
    date_added = models.DateTimeField(auto_now_add=True)
    app_name='learning_logs'
    owner = models.ForeignKey(User,on_delete=models.CASCADE)  #建立Topic与User的外键关系
    def __str__(self):
        '''返回模型的字符串(text中的字符串)表示'''
        #__str__(self)告诉Django默认应使用哪个属性来显示有关主题的信息，Django将调用该函数来显示模型的简单表示
        return self.text

class Entry(models.Model):
    '''在学习的有关某个主题的知识'''
    #下面的代码将每个条目(entry)关联到特定的主题。每个主题创建时都给它分配了一个键(ID)
    #需要在两项数据之间建立联系时,Django使用与每项信息相关联的键
    
    #ForeignKey:外键,是一个数据库术语,引用了数据库中的另一条记录
    #django2.0之后,定义外键和一对一关系的时候需要加on_delete选项,此参数为了避免两个表里的数据不一致的问题
    #一般情况下使用models.CASCADE:级联删除
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
 
    #text是一个TextField实例,不需要限制长度，可创建一个可编辑文本框
    text = models.TextField()
 
    #date_added让我们能够按创建顺序呈现条目,并在每个条目旁边放置时间戳
    date_added = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        '''存储用于管理模型的额外信息'''
        #设置verbose_name_plural属性,让Django在需要时使用Entries来表示多个条目
        #如果没有这个类,Django将使用Entrys来表示多个条目
        verbose_name_plural = 'entries'
    
    def __str__(self):
        '''返回模型的字符串表示'''
        #如果条目包含的文本过长,则我们只显示前50个字符
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text
