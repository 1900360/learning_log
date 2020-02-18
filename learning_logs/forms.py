from django import forms
from .models import Topic,Entry
 
class TopicForm(forms.ModelForm):
    #Meta高数Django根据哪个模型创建表单以及表单中包含哪些字段
    #我们根据Topic模型创建一个表单,该表单只包含字段text
    class Meta:
        model = Topic
        fields = {'text'}
        labels = {'text':''}    #让Django不要为字段text生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {'text'}
        labels = {'text': ''}
        #widgets(小部件)是一个HTML表单元素,如单行文本框等
        #forms.Textarea将文本区域设置为80列
        widgets = {'text':forms.Textarea(attrs={'cols':80})}