"""lecture URL Configuration

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
from django.urls import path, include
from django.views.generic.base import TemplateView      # template 경로안에서만 html을 찾기위한 패키지와 클래스

# http://localhost:8000/

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),    # 기본화면 : http://localhost:8000/
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls'))
]
