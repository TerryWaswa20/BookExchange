"""
URL configuration for Bookexchange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ThienryBooks import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('parent_form', views.parent, name='parent'),
    path('hiring', views.hire, name='hire'),
    path('books_list', views.books_hire, name='books_list'),
    path('client_dashboard', views.dashboard, name='dashboard_client'),
    path('client_login', views.login_client, name='c_login'),
    path('exchange_list', views.exchange_list, name='exchange_books'),
    path('exchange_form', views.exchange, name='ex_form')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
