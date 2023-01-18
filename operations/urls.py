"""operations URL Configuration

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
from testapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cre/',v.create_view.as_view()),
    path('list/',v.Product_list.as_view(),name='list'),
    path('<int:pk>/details',v.Product_detail.as_view(),name='details'),
    path('<int:pk>/update',v.Product_update.as_view(),name='update'),

]
