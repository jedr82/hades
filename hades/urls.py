"""hades URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.homepage.views import HomePage
from core.erp.views import Dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='homepage'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('', include('core.erp.urls','erp_app')),
    path('', include('core.login.urls','login_app')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)