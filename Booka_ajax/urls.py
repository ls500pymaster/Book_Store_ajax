"""Booka_ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('', include('app.urls', namespace='app')),
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    path("authors/", views.author_list, name="author_list"),
    path("authors/create/", views.author_create, name="author_create"),
    path("authors/<int:pk>/update/", views.author_update, name="author_update"),
    path("authors/<int:pk>/delete/", views.author_delete, name="author_delete"),


    path("contact/", views.contact, name="contact"),
    path("contact/success/", views.contact_success, name="contact_success"),





    path('admin/', admin.site.urls),
]