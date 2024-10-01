from django.urls import path
from .views import MessageCreateAPIView

urlpatterns = [
    path('message/create/', MessageCreateAPIView.as_view(), name='create-contact'),
]