from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic,Entry#导入我们注册的模型
admin.site.register(Topic)
admin.site.register(Entry)