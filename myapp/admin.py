from django.contrib import admin
from .models import Talaba,Guruh

# Register your models here.
@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ('ism', 'familya','guruh','telefon_raqam')
    list_filter = ('ism','familya','guruh','telefon_raqam','yosh')
    list_per_page = 50
    search_fields = ('ism','familya','guruh','telefon_raqam')
    
    
admin.site.register(Guruh)
    
    
