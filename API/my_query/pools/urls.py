# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 12:57
# @Author  : Yuan Bian
# @File    : urls.py

from django.urls import path
from pools import views

urlpatterns = [
    path('pools/', views.pool_list),
    path('pools/<int:pk>/', views.pool_detail),
]