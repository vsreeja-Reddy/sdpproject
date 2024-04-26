from django.contrib import admin
from .models import DonationCard
from .models import Feedback


@admin.register(DonationCard)
class DonationCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'feedback', 'created_at']
    search_fields = ['name', 'email', 'feedback']
    list_filter = ['created_at']



