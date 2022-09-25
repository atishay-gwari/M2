from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.viewlist,name="view"),
    path('add/',views.addlist,name="add"),
    path('delete/<str:id>/',views.deleteed,name="delete"),
    path('update/<str:id>/',views.updateed,name="update"),
    path('signin/',views.signup,name='signup'),
    path('login/',views.loginuppage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
]
