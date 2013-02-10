from django.contrib import admin
from tasks.models import *

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Category)