from django.contrib import admin
from service.models import Recipient, Message, Newsletter, Attempt


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment')
    search_fields = ('email', 'full_name')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body')
    search_fields = ('subject',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'status', 'message')
    list_filter = ('status',)
    filter_horizontal = ('recipients',)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('newsletter', 'attempt_time', 'status', 'server_response')
    list_filter = ('status',)
    