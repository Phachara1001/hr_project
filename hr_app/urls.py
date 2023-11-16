from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('add',views.add),
    path('list',views.list),
    path('manage',views.manage),
    path('login',views.custom_login),
    path('logout',views.logout_view),
]