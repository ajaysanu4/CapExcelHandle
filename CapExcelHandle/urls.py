"""CapExcelHandle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import include, path
from CapExcelHandleApp import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('show', views.show, name='show'),
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('export/csv/', views.export_users_csv, name='export_users_csv'),
    path('import/csv/', views.index, name='import_users_csv'),
    path('logout', views.user_logout, name='logout'),
    path('emp', views.emp, name='emp'),
    path('show', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]