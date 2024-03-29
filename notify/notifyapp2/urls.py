from . import views
from django.urls import path
from notifyapp.views import NotificationListView

urlpatterns = [
    path('viewerpost/',views.viewerpost,name='viewerpost'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
]
