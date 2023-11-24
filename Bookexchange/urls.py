from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ThienryBooks', include('ThienryBooks.urls')),
]
admin.site.site_header = "Thienry Books Program"
admin.site.site_title = "Thienry Bookexchange"
admin.site.index_title = "Welcome To Thienry Books Admin Site"