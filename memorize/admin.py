from django.contrib import admin
from models import Practice

class PracticeAdmin(admin.ModelAdmin):
    """Makes all fields of Practice visible on admin site.

    """
    list_display = Practice._meta.get_all_field_names()


admin.site.register(Practice, PracticeAdmin)