"""Hotel_Managment_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from Hotel import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^result/$',views.result,name="result"),
    url(r'^test/$',views.test,name="test"),
    url(r'^show_data/$',views.print_data,name="print_data"),
    url(r'^search/$',views.search,name="search"),
    path('admin/', admin.site.urls),
]
