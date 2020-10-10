from django.contrib import admin

# Register your models here.

from.models import names,subject,marks
admin.site.register(names)
admin.site.register(subject)
admin.site.register(marks)
