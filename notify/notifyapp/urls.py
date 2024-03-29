from django.urls import path
from . import views
from .views import NotificationListView
urlpatterns = [
    path('', views.index, name='index'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('poster/',views.poster,name='poster'),
]