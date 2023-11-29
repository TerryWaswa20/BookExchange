from django.contrib import admin
from ThienryBooks.models import Hiring, Purchase,Exchange,Order

admin.site.register(Hiring)
admin.site.register(Purchase)
admin.site.register(Exchange)
admin.site.register(Order)


class HiringAdmin(admin.ModelAdmin):
    list_display = ('official_name', 'contact', 'location','price','description')
    ordering = ('official_name',)
    search_fields = ('official_name','location')






