from django.contrib import admin
from aliss.models import Claim

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_filter = ['status']
    list_display = ['organisation', 'status']
    search_fields = ['organisation__name']
