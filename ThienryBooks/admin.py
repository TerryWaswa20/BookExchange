from django.contrib import admin
from ThienryBooks.models import Parent, Hiring, Purchase

admin.site.register(Parent)
admin.site.register(Hiring)


class HiringAdmin(admin.ModelAdmin):
    list_display = ('official_name', 'contact', 'location')
    ordering = ('official_name',)
    search_fields = ('official_name','location')


admin.site.register(Purchase)



