from django.contrib import admin
from sender.models import EmailSender

@admin.register(EmailSender)
class EmailSenderAdmin(admin.ModelAdmin):
    pass
