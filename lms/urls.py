"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from students.views import create_student
from students.views import get_students
from students.views import index
from students.views import update_student

# CRUD - Create, Read, Update, Delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),                # Read
    path('students/create/', create_student),       # Create
    path('students/update/<int:pk>/', update_student),       # Update
]