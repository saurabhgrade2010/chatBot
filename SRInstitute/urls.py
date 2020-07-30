"""SRInstitute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include,url
from django.conf.urls.static import static
#from SRInstitute import settings
from institute.views import home_view,register_user,user_login,user_login_fun,main_page_view,user_msg_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('register_user/',register_user,name='register'),
    path('user_login/',user_login,name='login'),
    path('user_login_fun/',user_login_fun,name='login'),
    path('main_page/',main_page_view,name='main_page'),
    path('user_msg/',user_msg_view,name='user_msg'),
]
