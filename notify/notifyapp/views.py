from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Notification
# Create your views here.
def index(request):
    return render(request, 'notifyapp/index.html')
class NotificationListView(View):
    def get(self, request, *args, **kwargs):
        # Retrieve all notifications from the database
        notifications = Notification.objects.all()
        
        # Create a list to store the notification messages
        notification_messages = []
        
        # Iterate over the notifications and extract the messages
        for notification in notifications:
            notification_messages.append(notification.message)
        
        # Return the notification messages as a JSON response
        return JsonResponse(notification_messages, safe=False)
def poster(request):
    if request.method=='POST':
        message=request.POST.get('message')
        notification=Notification(message=message)
        notification.save()
    return render(request,'notifyapp/writenotification.html')