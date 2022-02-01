# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 21:35:30 2022

@author: naman
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]